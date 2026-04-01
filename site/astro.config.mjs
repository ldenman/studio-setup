import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://buffalo-shoals.pages.dev',
  content: {
    collections: {
      blog: {
        schema: ({ z }) => ({
          title: z.string(),
          date: z.date(),
          description: z.string(),
          tags: z.array(z.string()).optional(),
        }),
      },
    },
  },
});
