import { defineConfig } from 'astro/config';

import cloudflare from '@astrojs/cloudflare';

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

  adapter: cloudflare(),
});