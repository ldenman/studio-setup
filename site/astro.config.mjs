import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://studio.lakedenman.com',
  devToolbar: { enabled: false },
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
