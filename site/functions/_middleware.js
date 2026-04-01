const CREDENTIALS_HEADER = "Authorization";
const CREDENTIALS_COOKIE = "cfp_auth";

async function handleRequest(context) {
  const { request, env, next } = context;

  const password = env.CFP_PASSWORD;
  if (!password) {
    return next();
  }

  const credentials = request.headers.get(CREDENTIALS_HEADER);
  const cookie = parseCookie(request.headers.get("Cookie") || "");

  if (cookie[CREDENTIALS_COOKIE]) {
    const decoded = atob(cookie[CREDENTIALS_COOKIE]);
    if (decoded === password) {
      return next();
    }
  }

  if (credentials) {
    const [scheme, encoded] = credentials.split(" ");
    if (scheme === "Basic") {
      const decoded = atob(encoded);
      const [, pass] = decoded.split(":");
      if (pass === password) {
        const response = await next();
        const newResponse = new Response(response.body, response);
        newResponse.headers.set(
          "Set-Cookie",
          `${CREDENTIALS_COOKIE}=${btoa(password)}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=86400`
        );
        return newResponse;
      }
    }
  }

  return new Response("Authentication required", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="Buffalo Shoals"',
    },
  });
}

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

export const onRequest = handleRequest;
