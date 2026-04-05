export function getTemplate({ redirectPath, withError }) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lake's Studio</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #1a1a1a; color: #eee; font-family: 'Courier New', monospace; display: flex; align-items: center; justify-content: center; min-height: 100vh; }
    .login { text-align: center; max-width: 320px; width: 100%; padding: 2rem; }
    .logo { color: #d4a574; font-size: 1.4rem; margin-bottom: 2rem; letter-spacing: 0.1em; }
    input[type="password"] { background: #2a2a2a; border: 1px solid #555; color: #eee; padding: 0.6rem 1rem; font-family: inherit; font-size: 1rem; width: 100%; margin-bottom: 0.5rem; }
    input[type="password"]:focus { outline: none; border-color: #d4a574; }
    button { background: #d4a574; color: #1a1a1a; border: none; padding: 0.6rem 1.5rem; font-family: inherit; font-size: 1rem; cursor: pointer; width: 100%; }
    button:hover { background: #e0b584; }
    .error { color: #c33; margin-bottom: 1rem; font-size: 0.85rem; }
  </style>
</head>
<body>
  <div class="login">
    <div class="logo">// LAKE'S STUDIO</div>
    ${withError ? '<p class="error">wrong password</p>' : ''}
    <form method="post" action="/cfp_login">
      <input type="hidden" name="redirect" value="${redirectPath}" />
      <input type="password" name="password" placeholder="password" autocomplete="current-password" required autofocus>
      <button type="submit">enter</button>
    </form>
  </div>
</body>
</html>`;
}
