export default {
  async fetch(request, env) {
    const password = env.CFP_PASSWORD;
    if (!password) {
      return env.ASSETS.fetch(request);
    }

    const cookie = parseCookie(request.headers.get("Cookie") || "");
    if (cookie["cfp_auth"]) {
      try {
        const decoded = atob(cookie["cfp_auth"]);
        if (decoded === password) {
          return env.ASSETS.fetch(request);
        }
      } catch (e) {}
    }

    const credentials = request.headers.get("Authorization");
    if (credentials) {
      const [scheme, encoded] = credentials.split(" ");
      if (scheme === "Basic") {
        try {
          const decoded = atob(encoded);
          const [, pass] = decoded.split(":");
          if (pass === password) {
            const response = await env.ASSETS.fetch(request);
            const newResponse = new Response(response.body, response);
            newResponse.headers.set(
              "Set-Cookie",
              `cfp_auth=${btoa(password)}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=86400`
            );
            return newResponse;
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
  },
};

function parseCookie(cookieHeader) {
  const cookies = {};
  cookieHeader.split(";").forEach((cookie) => {
    const [name, ...rest] = cookie.trim().split("=");
    if (name) {
      cookies[name] = rest.join("=");
    }
  });
  return cookies;
}
