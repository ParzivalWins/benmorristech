import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('blog');
  const sortedPosts = posts.sort(
    (a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
  );

  return rss({
    title: 'The Ben Morris Experience // Field Notes',
    description: 'Product Leadership, Commerce Architecture, and Emerging Tech Insights.',
    site: context.site || 'https://www.benmorristech.com',
    items: sortedPosts.map((post) => ({
      title: post.data.title,
      pubDate: new Date(post.data.date),
      description: post.data.excerpt || post.data.title,
      link: `/blog/${post.id}/`,
    })),
  });
}
