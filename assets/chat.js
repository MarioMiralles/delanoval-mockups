/*
 * Mockup of the SiteStaffr chat widget, shared by every concept.
 * Configure on the script tag:
 *   data-accent   button and header color
 *   data-ink      text color on the accent
 *   data-font     font-family for the widget
 *   data-open     "true" to start with the panel open
 *   data-radius   corner radius in px
 *   data-teaser   greeting bubble shown after a short delay
 */
(function () {
  var tag = document.currentScript;
  var accent = tag.getAttribute('data-accent') || '#3957ff';
  var ink = tag.getAttribute('data-ink') || '#ffffff';
  var font = tag.getAttribute('data-font') || 'Rubik, system-ui, sans-serif';
  var radius = parseInt(tag.getAttribute('data-radius') || '16', 10);
  var startOpen = tag.getAttribute('data-open') === 'true';
  var teaser = tag.getAttribute('data-teaser');

  var css = '' +
    '.ssw{position:fixed;right:20px;bottom:20px;z-index:50;font-family:' + font + ';color:#051b34}' +
    '.ssw *{box-sizing:border-box}' +
    '.ssw-launch{display:flex;align-items:center;gap:10px;min-height:52px;padding:0 20px 0 16px;border:0;border-radius:999px;background:' + accent + ';color:' + ink + ';font:500 15px/1 ' + font + ';cursor:pointer;box-shadow:0 12px 32px rgba(5,27,52,.28)}' +
    '.ssw-launch:focus-visible,.ssw button:focus-visible,.ssw input:focus-visible{outline:3px solid #8da0ff;outline-offset:2px}' +
    '.ssw-panel{position:absolute;right:0;bottom:66px;width:min(360px,calc(100vw - 40px));background:#fff;border-radius:' + radius + 'px;overflow:hidden;box-shadow:0 24px 60px rgba(5,27,52,.3);display:none}' +
    '.ssw.open .ssw-panel{display:block}' +
    '.ssw-head{display:flex;align-items:center;gap:12px;padding:16px 18px;background:#051b34;color:#fff}' +
    '.ssw-av{width:40px;height:40px;border-radius:50%;background:' + accent + ';display:grid;place-items:center;font-weight:600;color:' + ink + ';flex:none}' +
    '.ssw-head strong{display:block;font-size:15px}' +
    '.ssw-head span{font-size:13px;opacity:.8}' +
    '.ssw-x{margin-left:auto;background:none;border:0;color:#fff;width:44px;height:44px;cursor:pointer;font-size:22px;line-height:1}' +
    '.ssw-body{padding:18px;display:flex;flex-direction:column;gap:10px;background:#f5f7ff;max-height:340px;overflow:auto}' +
    '.ssw-msg{background:#fff;border:1px solid #dde3f0;border-radius:14px 14px 14px 4px;padding:12px 14px;font-size:15px;line-height:1.45;max-width:90%}' +
    '.ssw-me{align-self:flex-end;background:#051b34;color:#fff;border-color:#051b34;border-radius:14px 14px 4px 14px}' +
    '.ssw-quick{display:flex;flex-wrap:wrap;gap:8px}' +
    '.ssw-quick button{min-height:40px;padding:0 14px;border-radius:999px;border:1px solid ' + accent + ';background:#fff;color:#051b34;font:500 14px ' + font + ';cursor:pointer}' +
    '.ssw-quick button:hover{background:' + accent + ';color:' + ink + '}' +
    '.ssw-form{display:flex;gap:8px;padding:12px;border-top:1px solid #dde3f0}' +
    '.ssw-form input{flex:1;min-width:0;min-height:44px;padding:0 12px;border:1px solid #c8d0e2;border-radius:10px;font:15px ' + font + '}' +
    '.ssw-form button{min-width:44px;min-height:44px;border:0;border-radius:10px;background:' + accent + ';color:' + ink + ';cursor:pointer}' +
    '.ssw-foot{padding:0 12px 10px;font-size:11px;color:#5c6878;text-align:center}' +
    '.ssw-teaser{position:absolute;right:0;bottom:66px;width:min(280px,calc(100vw - 40px));background:#fff;border:1px solid #dde3f0;border-radius:14px 14px 4px 14px;padding:14px 40px 14px 16px;font-size:15px;line-height:1.45;box-shadow:0 16px 40px rgba(5,27,52,.2);cursor:pointer}' +
    '.ssw-teaser button{position:absolute;top:2px;right:2px;width:36px;height:36px;border:0;background:none;color:#5c6878;font-size:18px;cursor:pointer}' +
    '.ssw.open .ssw-teaser{display:none}' +
    '@media (prefers-reduced-motion:no-preference){.ssw.open .ssw-panel{animation:sswIn .18s ease-out}}' +
    '@keyframes sswIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}';

  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  var root = document.createElement('div');
  root.className = 'ssw' + (startOpen ? ' open' : '');
  root.innerHTML = '' +
    '<div class="ssw-panel" role="dialog" aria-label="Chat with De La Noval, P.A.">' +
      '<div class="ssw-head"><div class="ssw-av" aria-hidden="true">DN</div><div><strong>De La Noval, P.A.</strong><span>Online now · English / Español</span></div>' +
      '<button class="ssw-x" type="button" aria-label="Close chat">&times;</button></div>' +
      '<div class="ssw-body" aria-live="polite">' +
        '<div class="ssw-msg">Hi, thanks for reaching out. What can we help you with today?</div>' +
        '<div class="ssw-msg">Hola, ¿prefiere continuar en español?</div>' +
        '<div class="ssw-quick">' +
          '<button type="button">I was injured</button>' +
          '<button type="button">My insurance claim was denied</button>' +
          '<button type="button">Family or immigration</button>' +
          '<button type="button">Español</button>' +
        '</div>' +
      '</div>' +
      '<form class="ssw-form" onsubmit="return false"><label class="ssw-sr" for="ssw-in" style="position:absolute;left:-9999px">Message</label><input id="ssw-in" type="text" placeholder="Type your message"><button type="submit" aria-label="Send"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg></button></form>' +
      '<div class="ssw-foot">AI assistant · Powered by SiteStaffr</div>' +
    '</div>' +
    '<button class="ssw-launch" type="button" aria-expanded="' + startOpen + '"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg><span>Chat with us</span></button>';
  document.body.appendChild(root);

  if (teaser && !startOpen) {
    setTimeout(function () {
      if (root.classList.contains('open')) return;
      var t = document.createElement('div');
      t.className = 'ssw-teaser';
      t.textContent = teaser;
      var x = document.createElement('button'); x.type = 'button'; x.setAttribute('aria-label', 'Dismiss'); x.innerHTML = '&times;';
      t.appendChild(x);
      x.addEventListener('click', function (e) { e.stopPropagation(); t.remove(); });
      t.addEventListener('click', function () { t.remove(); setOpen(true); });
      root.insertBefore(t, launch);
    }, 2500);
  }

  var launch = root.querySelector('.ssw-launch');
  var body = root.querySelector('.ssw-body');
  function setOpen(v) { root.classList.toggle('open', v); launch.setAttribute('aria-expanded', String(v)); }
  launch.addEventListener('click', function () { setOpen(!root.classList.contains('open')); });
  root.querySelector('.ssw-x').addEventListener('click', function () { setOpen(false); });

  function say(text, me) {
    var m = document.createElement('div');
    m.className = 'ssw-msg' + (me ? ' ssw-me' : '');
    m.textContent = text;
    body.appendChild(m);
    body.scrollTop = body.scrollHeight;
  }
  root.querySelectorAll('.ssw-quick button').forEach(function (b) {
    b.addEventListener('click', function () {
      say(b.textContent, true);
      setTimeout(function () {
        say(b.textContent === 'Español'
          ? 'Con gusto. Cuéntenos brevemente qué pasó y le conectamos con un abogado.'
          : 'I am sorry you are dealing with that. Can you tell me briefly what happened and the best number to reach you?');
      }, 500);
    });
  });
  root.querySelector('.ssw-form').addEventListener('submit', function () {
    var input = root.querySelector('#ssw-in');
    if (!input.value.trim()) return;
    say(input.value.trim(), true);
    input.value = '';
    setTimeout(function () { say('Thank you. An attorney from our team will follow up shortly.'); }, 500);
  });
})();
