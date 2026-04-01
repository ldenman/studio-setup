import { defineMiddleware } from "astro:middleware";

export const onRequest = defineMiddleware(async (context, next) => {
  const password = context.locals.runtime?.env?.CFP_PASSWORD;
  if (!password) {
    return next();
  }

  const cookie = context.cookies.get("cfp_auth");
  if (cookie && cookie.value) {
    try {
      const decoded = atob(cookie.value);
      if (decoded === password) {
        return next();
      }
    } catch (e) {}
  }

  const credentials = context.request.headers.get("Authorization");
  if (credentials) {
    const [scheme, encoded] = credentials.split(" ");
    if (scheme === "Basic") {
      try {
        const decoded = atob(encoded);
        const [, pass] = decoded.split(":");
        if (pass === password) {
          const response = await next();
          response.headers.set(
            "Set-Cookie",
            `cfp_auth=${btoa(password)}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=86400`
          );
          return response;
        }
      } catch (e) {}
    }
  }

  return new Response("Authentication required", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="Buffalo Shoals"',
    },
  });
});
