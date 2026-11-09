import glob
import re
import json

files = glob.glob('/Users/agentbond/Desktop/NewWebsite/src/content/blog/*.mdx')
print(f"Processing {len(files)} files...")

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    parts = content.split('---', 2)
    if len(parts) >= 3:
        fm = parts[1]
        body = parts[2]
        
        title_m = re.search(r'title:\s*(.*)', fm)
        date_m = re.search(r'date:\s*"?([^\n"]+)"?', fm)
        excerpt_m = re.search(r'excerpt:\s*(.*)', fm)
        cat_m = re.search(r'categories:\s*(\[.*?\])', fm)
        tag_m = re.search(r'tags:\s*(\[.*?\])', fm)
        
        # Clean title
        title_raw = title_m.group(1).strip() if title_m else 'Untitled'
        title_raw = re.sub(r'^["\']|["\']$', '', title_raw)
        title_raw = title_raw.replace("\\'", "'").replace('\\"', '"').replace('\\', '')
        
        # Clean excerpt
        excerpt_raw = excerpt_m.group(1).strip() if excerpt_m else ''
        excerpt_raw = re.sub(r'^["\']|["\']$', '', excerpt_raw)
        excerpt_raw = excerpt_raw.replace("\\'", "'").replace('\\"', '"').replace('\\', '')
        
        date_val = date_m.group(1).strip() if date_m else '2021-01-01'
        date_val = date_val.replace('"', '').replace("'", "")[:10]
        
        cats = cat_m.group(1) if cat_m else '[]'
        tags = tag_m.group(1) if tag_m else '[]'
        
        new_fm = f"""
title: {json.dumps(title_raw)}
date: {json.dumps(date_val)}
excerpt: {json.dumps(excerpt_raw)}
categories: {cats}
tags: {tags}
featured: false
"""
        new_content = '---' + new_fm + '---' + body
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)

print("Frontmatter clean completed!")
