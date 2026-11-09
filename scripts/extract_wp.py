#!/usr/bin/env python3
"""
WordPress REST API Extractor for benmorristech.com
Safely archives all posts, pages, categories, tags, and media from WordPress before decommissioning Lightsail.
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
from datetime import datetime

BASE_URL = "https://www.benmorristech.com/wp-json/wp/v2"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

BACKUP_DIR = "/Users/agentbond/Desktop/NewWebsite/backup"
MEDIA_DIR = os.path.join(BACKUP_DIR, "media")
MD_POSTS_DIR = os.path.join(BACKUP_DIR, "markdown_posts")
MD_PAGES_DIR = os.path.join(BACKUP_DIR, "markdown_pages")

os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs(MD_POSTS_DIR, exist_ok=True)
os.makedirs(MD_PAGES_DIR, exist_ok=True)

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8")), resp.headers

def fetch_all(endpoint):
    items = []
    page = 1
    while True:
        url = f"{BASE_URL}/{endpoint}?per_page=100&page={page}"
        print(f"Fetching {endpoint} page {page}...")
        try:
            data, headers = fetch_json(url)
            if not data:
                break
            items.extend(data)
            total_pages = int(headers.get("X-WP-TotalPages", 1))
            if page >= total_pages:
                break
            page += 1
        except urllib.error.HTTPError as e:
            if e.code == 400: # past last page
                break
            print(f"Error fetching {url}: {e}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Total {endpoint} fetched: {len(items)}")
    return items

def html_to_markdown(html_content):
    if not html_content:
        return ""
    text = html_content
    # Clean up WP comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Headings
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    # Links
    text = re.sub(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.IGNORECASE | re.DOTALL)
    # Images
    text = re.sub(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', r'![\2](\1)', text, flags=re.IGNORECASE)
    text = re.sub(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', r'![](\1)', text, flags=re.IGNORECASE)
    # Strong / B
    text = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', text, flags=re.IGNORECASE | re.DOTALL)
    # Em / I
    text = re.sub(r'<(em|i)[^>]*>(.*?)</\1>', r'*\2*', text, flags=re.IGNORECASE | re.DOTALL)
    # Paragraphs and line breaks
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    # Blockquotes
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1\n\n', text, flags=re.IGNORECASE | re.DOTALL)
    # Strip remaining tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Replace common HTML entities
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#8217;', "'").replace('&#8220;', '"').replace('&#8221;', '"').replace('&#8211;', '-').replace('&#8212;', '--').replace('&#8230;', '...')
    # Normalize multiple newlines and spaces
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def main():
    print("=== Starting WP Extraction for benmorristech.com ===")
    
    # 1. Categories & Tags
    categories = fetch_all("categories")
    tags = fetch_all("tags")
    cat_map = {c["id"]: c["name"] for c in categories}
    tag_map = {t["id"]: t["name"] for t in tags}
    
    with open(os.path.join(BACKUP_DIR, "categories.json"), "w") as f:
        json.dump(categories, f, indent=2)
    with open(os.path.join(BACKUP_DIR, "tags.json"), "w") as f:
        json.dump(tags, f, indent=2)

    # 2. Posts
    posts = fetch_all("posts")
    with open(os.path.join(BACKUP_DIR, "posts.json"), "w") as f:
        json.dump(posts, f, indent=2)

    # 3. Pages
    pages = fetch_all("pages")
    with open(os.path.join(BACKUP_DIR, "pages.json"), "w") as f:
        json.dump(pages, f, indent=2)

    # 4. Convert posts to Markdown
    print("Converting posts to Markdown...")
    extracted_summary = []
    
    for p in posts:
        slug = p.get("slug")
        title = p.get("title", {}).get("rendered", "Untitled")
        date = p.get("date", "")
        link = p.get("link", "")
        raw_content = p.get("content", {}).get("rendered", "")
        excerpt = p.get("excerpt", {}).get("rendered", "")
        cat_names = [cat_map.get(cid, str(cid)) for cid in p.get("categories", [])]
        tag_names = [tag_map.get(tid, str(tid)) for tid in p.get("tags", [])]
        featured_media_id = p.get("featured_media", 0)

        md_content = html_to_markdown(raw_content)
        md_excerpt = html_to_markdown(excerpt)

        safe_title = title.replace('"', '\\"')
        safe_excerpt = md_excerpt.replace('"', '\\"').replace('\n', ' ')
        frontmatter = f"""---
title: "{safe_title}"
slug: "{slug}"
date: "{date}"
original_url: "{link}"
categories: {json.dumps(cat_names)}
tags: {json.dumps(tag_names)}
featured_media_id: {featured_media_id}
excerpt: "{safe_excerpt}"
---

# {title}

{md_content}
"""
        filename = f"{date[:10]}-{slug}.md" if date else f"{slug}.md"
        with open(os.path.join(MD_POSTS_DIR, filename), "w") as f:
            f.write(frontmatter)

        extracted_summary.append({
            "id": p["id"],
            "title": title,
            "slug": slug,
            "date": date,
            "categories": cat_names,
            "filename": filename
        })

    # 5. Convert pages to Markdown
    print("Converting pages to Markdown...")
    for p in pages:
        slug = p.get("slug")
        title = p.get("title", {}).get("rendered", "Untitled")
        date = p.get("date", "")
        raw_content = p.get("content", {}).get("rendered", "")
        md_content = html_to_markdown(raw_content)

        safe_title = title.replace('"', '\\"')
        frontmatter = f"""---
title: "{safe_title}"
slug: "{slug}"
date: "{date}"
---

# {title}

{md_content}
"""
        with open(os.path.join(MD_PAGES_DIR, f"{slug}.md"), "w") as f:
            f.write(frontmatter)

    # 6. Save manifest
    with open(os.path.join(BACKUP_DIR, "manifest.json"), "w") as f:
        json.dump({
            "extracted_at": datetime.utcnow().isoformat() + "Z",
            "total_posts": len(posts),
            "total_pages": len(pages),
            "total_categories": len(categories),
            "total_tags": len(tags),
            "posts_summary": extracted_summary
        }, f, indent=2)

    print(f"=== Extraction Complete! Total {len(posts)} posts and {len(pages)} pages archived! ===")

if __name__ == "__main__":
    main()
