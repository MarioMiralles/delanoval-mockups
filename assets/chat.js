/*
 * Mockup of the SiteStaffr widget (launcher, "How would you like to connect?" card,
 * text chat panel and a demo voice state), styled after the plugin's own CSS.
 * Configure on the script tag:
 *   data-accent    brand color for the launcher, headers and visitor bubbles
 *   data-teaser    tooltip text above the launcher (default "Talk to AI Assistant")
 *   data-business  business name shown in the card and chat header
 *   data-style     "refined" for the plugin's Refined chat preset (default: Signature)
 */
(function () {
  var tag = document.currentScript;
  var accent = tag.getAttribute('data-accent') || '#3957ff';
  var tip = tag.getAttribute('data-teaser') || 'Talk to AI Assistant';
  var biz = tag.getAttribute('data-business') || 'De La Noval, P.A.';
  var variant = tag.getAttribute('data-style') || '';
  var greeting = 'Hi! Thanks for reaching out to ' + biz + (/\.$/.test(biz) ? '' : '.') + ' How can I help you today? También hablamos español.';

  var css = '' +
    '.ssw{--ss-accent:' + accent + ';--ss-deep:color-mix(in srgb,var(--ss-accent) 84%,#000);--ss-lift:color-mix(in srgb,var(--ss-accent) 94%,#fff);--ss-soft:color-mix(in srgb,var(--ss-accent) 11%,#fff);' +
      '--ss-ink:#0f172a;--ss-muted:#64748b;--ss-rule:#e7e9ee;--ss-surface:#f6f7f9;' +
      'font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased;color:var(--ss-ink)}' +
    '.ssw *{box-sizing:border-box}' +
    '.ssw button{font-family:inherit}' +
    '.ssw-launch-wrap{position:fixed;right:20px;bottom:20px;z-index:60}' +
    '.ssw-launch{position:relative;width:60px;height:60px;padding:0;border:0;border-radius:20px 20px 20px 0;background:var(--ss-accent);display:flex;align-items:center;justify-content:center;cursor:pointer;' +
      'box-shadow:0 10px 24px -8px color-mix(in srgb,var(--ss-accent) 60%,transparent),0 4px 10px -4px rgba(15,23,42,.25),inset 0 1px 0 rgba(255,255,255,.18);transition:transform .3s ease,box-shadow .3s ease}' +
    '.ssw-launch:hover{transform:translateY(-2px)}' +
    '.ssw-launch:focus-visible{outline:2px solid var(--ss-accent);outline-offset:3px}' +
    '.ssw-launch .ssw-ico{width:26px;height:26px;color:#fff}' +
    '.ssw-wave{display:none;align-items:center;gap:3px;color:#fff}' +
    '.ssw-wave span{width:3px;border-radius:2px;background:currentColor;animation:sswWave 1s ease-in-out infinite}' +
    '.ssw-wave span:nth-child(1){height:8px}.ssw-wave span:nth-child(2){height:14px;animation-delay:.2s}.ssw-wave span:nth-child(3){height:10px;animation-delay:.4s}' +
    '@keyframes sswWave{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.5)}}' +
    '.ssw-ring{position:absolute;inset:0;border-radius:20px 20px 20px 0;border:2px solid #e74c3c;opacity:0;pointer-events:none}' +
    '.ssw.listening .ssw-launch{background:#e74c3c}' +
    '.ssw.listening .ssw-launch .ssw-ico{display:none}.ssw.listening .ssw-wave{display:flex}' +
    '.ssw.listening .ssw-ring{animation:sswPulse 1.5s ease-out infinite}' +
    '@keyframes sswPulse{0%{transform:scale(1);opacity:.8}100%{transform:scale(1.5);opacity:0}}' +
    '.ssw-tip{position:absolute;bottom:calc(100% + 10px);right:0;background:var(--ss-accent);color:#fff;padding:9px 13px;border-radius:10px;font-size:13px;font-weight:500;white-space:nowrap;box-shadow:0 10px 24px -10px rgba(15,23,42,.45);opacity:0;transform:translateY(4px);transition:opacity .3s ease,transform .3s ease;pointer-events:none}' +
    '.ssw-tip::after{content:"";position:absolute;top:100%;right:24px;border:6px solid transparent;border-top-color:var(--ss-accent)}' +
    '.ssw.tip-on .ssw-tip,.ssw-launch:hover+.ssw-tip{opacity:1;transform:none}' +
    '.ssw.listening .ssw-tip{background:#0f172a}.ssw.listening .ssw-tip::after{border-top-color:#0f172a}' +
    '.ssw-card,.ssw-panel{position:fixed;right:20px;bottom:90px;z-index:61;width:384px;max-width:calc(100vw - 24px);background:var(--ss-surface);border-radius:20px;overflow:hidden;' +
      'box-shadow:0 32px 64px -24px rgba(15,23,42,.38),0 12px 28px -12px rgba(15,23,42,.18),0 0 0 1px rgba(15,23,42,.06);opacity:0;transform:translateY(12px) scale(.95);transform-origin:bottom right;transition:opacity .2s ease,transform .2s ease;pointer-events:none}' +
    '.ssw-card.open,.ssw-panel.open{opacity:1;transform:none;pointer-events:auto}' +
    '.ssw-head{color:#fff;background:radial-gradient(120% 140% at 0% 0%,var(--ss-lift) 0%,transparent 55%),linear-gradient(135deg,var(--ss-accent) 0%,var(--ss-deep) 100%)}' +
    '.ssw-card .ssw-head{position:relative;padding:22px 56px 20px 22px}' +
    '.ssw-eyebrow{display:block;margin:0 0 10px;font-size:12px;font-weight:600;letter-spacing:.02em}' +
    '.ssw-card h3{margin:0 0 4px;font-size:20px;font-weight:700;line-height:1.25;letter-spacing:-.015em;color:#fff;font-family:inherit}' +
    '.ssw-card p{margin:0;font-size:13.5px;line-height:1.4;color:#fff}' +
    '.ssw-x{position:absolute;top:14px;right:14px;width:32px;height:32px;border:0;border-radius:50%;background:transparent;color:#fff;cursor:pointer;display:grid;place-items:center}' +
    '.ssw-x:hover{background:rgba(255,255,255,.16)}' +
    '.ssw-tiles{display:flex;flex-direction:column;gap:10px;padding:16px}' +
    '.ssw-tile{display:flex;align-items:center;gap:14px;width:100%;padding:14px 16px;background:#fff;border:1px solid var(--ss-rule);border-radius:14px;cursor:pointer;text-align:left;transition:border-color .15s ease,box-shadow .15s ease,transform .1s ease}' +
    '.ssw-tile:hover{border-color:color-mix(in srgb,var(--ss-accent) 40%,var(--ss-rule));box-shadow:0 6px 16px -10px rgba(15,23,42,.3)}' +
    '.ssw-tile-ico{flex:none;width:44px;height:44px;border-radius:14px;background:var(--ss-soft);color:var(--ss-accent);display:grid;place-items:center}' +
    '.ssw-tile-text{flex:1;display:flex;flex-direction:column;gap:2px}' +
    '.ssw-tile-label{font-size:15px;font-weight:600;color:var(--ss-ink)}' +
    '.ssw-tile-desc{font-size:13px;color:var(--ss-muted);line-height:1.35}' +
    '.ssw-chev{flex:none;color:#94a3b8;transition:transform .15s ease,color .15s ease}' +
    '.ssw-tile:hover .ssw-chev{color:var(--ss-accent);transform:translateX(2px)}' +
    '.ssw-panel{height:540px;max-height:calc(100vh - 120px);display:flex;flex-direction:column}' +
    '.ssw-panel .ssw-head{display:flex;align-items:center;gap:12px;padding:16px 14px 16px 18px;flex-shrink:0}' +
    '.ssw-av{flex:none;width:38px;height:38px;border-radius:50%;display:grid;place-items:center;font-size:15px;font-weight:700;background:rgba(255,255,255,.18);box-shadow:inset 0 0 0 1px rgba(255,255,255,.28)}' +
    '.ssw-id{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}' +
    '.ssw-id b{font-size:15.5px;font-weight:650;letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
    '.ssw-id span{font-size:12px;font-weight:500}' +
    '.ssw-panel .ssw-x{position:static}' +
    '.ssw-msgs{flex:1;overflow-y:auto;padding:18px 16px;display:flex;flex-direction:column;gap:10px}' +
    '.ssw-msg{max-width:82%;padding:11px 15px;border-radius:17px;font-size:14.5px;line-height:1.55;animation:sswIn .2s ease}' +
    '.ssw-bot{align-self:flex-start;background:#fff;color:var(--ss-ink);border-bottom-left-radius:6px;box-shadow:0 1px 2px rgba(15,23,42,.06),0 0 0 1px rgba(15,23,42,.05)}' +
    '.ssw-me{align-self:flex-end;background:var(--ss-accent);color:#fff;border-bottom-right-radius:6px}' +
    '.ssw-typing{display:flex;gap:4px;align-items:center;padding:14px 16px}' +
    '.ssw-typing i{width:7px;height:7px;border-radius:50%;background:#94a3b8;animation:sswDot 1.2s ease-in-out infinite}' +
    '.ssw-typing i:nth-child(2){animation-delay:.15s}.ssw-typing i:nth-child(3){animation-delay:.3s}' +
    '@keyframes sswDot{0%,60%,100%{opacity:.35;transform:none}30%{opacity:1;transform:translateY(-3px)}}' +
    '@keyframes sswIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}' +
    '.ssw-input{display:flex;align-items:center;gap:6px;margin:0 14px 14px;padding:5px 5px 5px 8px;border:1px solid #e2e5ea;border-radius:40px;background:#fff;box-shadow:0 1px 2px rgba(15,23,42,.04);transition:border-color .15s ease,box-shadow .15s ease}' +
    '.ssw-input:focus-within{border-color:var(--ss-accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--ss-accent) 18%,transparent)}' +
    '.ssw-input textarea{flex:1;min-width:0;min-height:38px;max-height:100px;padding:9px 8px;border:0;background:transparent;resize:none;outline:none;font-family:inherit;font-size:14.5px;line-height:1.4;color:var(--ss-ink)}' +
    '.ssw-input textarea::placeholder{color:#9ca3af}' +
    '.ssw-send{flex:none;width:38px;height:38px;border:0;border-radius:50%;background:var(--ss-accent);color:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 4px 10px -4px color-mix(in srgb,var(--ss-accent) 70%,transparent)}' +
    '.ssw-send:hover{background:var(--ss-deep)}' +
    '@media (prefers-reduced-motion:reduce){.ssw *{animation:none!important;transition:none!important}}';

  // data-style="refined": the plugin's Refined chat preset (light header, no avatar,
  // outlined visitor, plain assistant, brand tint, 0 corners, site font, spaced caps).
  var R = '.ssw[data-style="refined"] ';
  if (variant === 'refined') css += '' +
    '.ssw[data-style="refined"]{--ss-surface:color-mix(in srgb,var(--ss-accent) 3%,#fff);--ss-ink:color-mix(in srgb,var(--ss-accent) 12%,#1d2327);--ss-muted:color-mix(in srgb,var(--ss-accent) 8%,#5c6166);--ss-rule:color-mix(in srgb,var(--ss-accent) 16%,#e6e6e6);font-family:inherit}' +
    R + '.ssw-card,' + R + '.ssw-panel{border-radius:0}' +
    R + '.ssw-head{background:transparent;color:var(--ss-ink)}' +
    R + '.ssw-card .ssw-head{padding-bottom:8px}' +
    R + '.ssw-eyebrow{margin-bottom:12px;font-size:10.5px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--ss-accent)}' +
    R + '.ssw-card h3{font-size:22px;font-weight:400;letter-spacing:.005em;color:var(--ss-ink)}' +
    R + '.ssw-card p{color:var(--ss-muted)}' +
    R + '.ssw-x{color:var(--ss-muted)}' + R + '.ssw-x:hover{background:var(--ss-rule);color:var(--ss-ink)}' +
    R + '.ssw-tiles{gap:0;padding:12px 0 8px}' +
    R + '.ssw-tile{background:transparent;border:0;border-top:1px solid var(--ss-rule);border-radius:0;padding:18px 22px;box-shadow:none}' +
    R + '.ssw-tile:hover{background:color-mix(in srgb,var(--ss-accent) 6%,transparent);box-shadow:none}' +
    R + '.ssw-tile-ico{width:28px;height:28px;background:transparent;color:var(--ss-accent)}' +
    R + '.ssw-tile-ico svg{stroke-width:1.5}' +
    R + '.ssw-tile-label{font-size:12px;font-weight:600;letter-spacing:.2em;text-transform:uppercase}' +
    R + '.ssw-tile-desc{font-size:14px;color:color-mix(in srgb,var(--ss-muted) 80%,var(--ss-ink))}' +
    R + '.ssw-chev{color:var(--ss-accent)}' +
    R + '.ssw-panel .ssw-head{background:var(--ss-surface);border-bottom:1px solid var(--ss-rule);padding:18px 14px 16px 20px}' +
    R + '.ssw-av{display:none}' +
    R + '.ssw-id{flex-direction:column-reverse;gap:6px}' +
    R + '.ssw-id span{font-size:10.5px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--ss-accent)}' +
    R + '.ssw-id b{font-size:19px;font-weight:500;letter-spacing:.01em}' +
    R + '.ssw-msgs{padding:22px 20px;gap:16px}' +
    R + '.ssw-msg{border-radius:0;font-weight:400}' +
    R + '.ssw-bot{background:transparent;box-shadow:none;border-left:1px solid var(--ss-accent);padding:2px 0 2px 16px;max-width:88%}' +
    R + '.ssw-me{background:#fff;color:var(--ss-ink);box-shadow:0 0 0 1px var(--ss-rule),0 1px 0 1px var(--ss-rule)}' +
    R + '.ssw-typing{padding:6px 0 6px 16px}' +
    R + '.ssw-input{margin:0;padding:12px 12px 12px 18px;border:0;border-top:1px solid var(--ss-rule);border-radius:0;background:transparent;box-shadow:none}' +
    R + '.ssw-input:focus-within{box-shadow:none;border-top-color:var(--ss-accent)}' +
    R + '.ssw-input textarea{font-weight:400}' +
    R + '.ssw-send{width:42px;height:42px;border-radius:0;box-shadow:none}';

  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  var chev = '<svg class="ssw-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>';
  var xIcon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>';

  var root = document.createElement('div');
  root.className = 'ssw';
  if (variant) root.setAttribute('data-style', variant);
  root.innerHTML = '' +
    '<div class="ssw-card" role="dialog" aria-label="How would you like to connect?">' +
      '<div class="ssw-head"><span class="ssw-eyebrow">' + biz + '</span><h3>How would you like to connect?</h3><p>Choose your preferred way to chat</p>' +
      '<button type="button" class="ssw-x" data-close aria-label="Close">' + xIcon + '</button></div>' +
      '<div class="ssw-tiles">' +
        '<button type="button" class="ssw-tile" data-choice="voice"><span class="ssw-tile-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v4M8 23h8"/></svg></span>' +
          '<span class="ssw-tile-text"><span class="ssw-tile-label">Voice</span><span class="ssw-tile-desc">Talk with our AI assistant</span></span>' + chev + '</button>' +
        '<button type="button" class="ssw-tile" data-choice="text"><span class="ssw-tile-ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span>' +
          '<span class="ssw-tile-text"><span class="ssw-tile-label">Text</span><span class="ssw-tile-desc">Type your questions</span></span>' + chev + '</button>' +
      '</div>' +
    '</div>' +
    '<div class="ssw-panel" role="dialog" aria-label="Chat with ' + biz + '">' +
      '<div class="ssw-head"><span class="ssw-av" aria-hidden="true">DN</span><span class="ssw-id"><b>' + biz + '</b><span>AI assistant · English &amp; Español</span></span>' +
      '<button type="button" class="ssw-x" data-close aria-label="Close chat">' + xIcon + '</button></div>' +
      '<div class="ssw-msgs" aria-live="polite"></div>' +
      '<form class="ssw-input" onsubmit="return false"><label for="ssw-text" style="position:absolute;left:-9999px">Message</label><textarea id="ssw-text" rows="1" placeholder="Type your message..."></textarea>' +
      '<button type="submit" class="ssw-send" aria-label="Send message"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/></svg></button></form>' +
    '</div>' +
    '<div class="ssw-launch-wrap">' +
      '<button type="button" class="ssw-launch" aria-label="Talk to AI Assistant" aria-expanded="false"><svg class="ssw-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-9.1 8.5 8.9 8.9 0 0 1-3.5-.8L3 21l1.8-5.4a8.5 8.5 0 0 1-.8-3.6 8.5 8.5 0 0 1 8.5-8.5 8.5 8.5 0 0 1 8.5 8.5z"/><circle cx="8.5" cy="11.5" r="0.9" fill="currentColor" stroke="none"/><circle cx="12" cy="11.5" r="0.9" fill="currentColor" stroke="none"/><circle cx="15.5" cy="11.5" r="0.9" fill="currentColor" stroke="none"/></svg><span class="ssw-wave" aria-hidden="true"><span></span><span></span><span></span></span><span class="ssw-ring"></span></button>' +
      '<div class="ssw-tip" role="status">' + tip + '</div>' +
    '</div>';
  document.body.appendChild(root);

  var card = root.querySelector('.ssw-card'), panel = root.querySelector('.ssw-panel');
  var launch = root.querySelector('.ssw-launch'), tipEl = root.querySelector('.ssw-tip');
  var msgs = root.querySelector('.ssw-msgs'), input = root.querySelector('#ssw-text');
  var greeted = false, voiceTimer;

  function closeAll() {
    card.classList.remove('open'); panel.classList.remove('open');
    launch.setAttribute('aria-expanded', 'false');
  }
  function add(text, me) {
    var m = document.createElement('div');
    m.className = 'ssw-msg ' + (me ? 'ssw-me' : 'ssw-bot');
    m.textContent = text; msgs.appendChild(m); msgs.scrollTop = msgs.scrollHeight;
    return m;
  }
  function botReply(text) {
    var t = document.createElement('div');
    t.className = 'ssw-msg ssw-bot ssw-typing'; t.innerHTML = '<i></i><i></i><i></i>';
    msgs.appendChild(t); msgs.scrollTop = msgs.scrollHeight;
    setTimeout(function () { t.remove(); add(text); }, 1100);
  }
  function stopVoice() {
    clearTimeout(voiceTimer); root.classList.remove('listening', 'tip-on'); tipEl.textContent = tip;
  }

  launch.addEventListener('click', function () {
    if (root.classList.contains('listening')) { stopVoice(); return; }
    var open = card.classList.contains('open') || panel.classList.contains('open');
    root.classList.remove('tip-on');
    if (open) { closeAll(); return; }
    card.classList.add('open'); launch.setAttribute('aria-expanded', 'true');
  });
  root.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', closeAll); });

  root.querySelector('[data-choice="text"]').addEventListener('click', function () {
    card.classList.remove('open'); panel.classList.add('open');
    if (!greeted) { greeted = true; botReply(greeting); }
    setTimeout(function () { input.focus(); }, 250);
  });
  root.querySelector('[data-choice="voice"]').addEventListener('click', function () {
    closeAll();
    tipEl.textContent = 'Connecting to AI Assistant...'; root.classList.add('tip-on');
    voiceTimer = setTimeout(function () {
      root.classList.add('listening'); tipEl.textContent = 'Listening...';
      voiceTimer = setTimeout(stopVoice, 6000);
    }, 1200);
  });

  root.querySelector('.ssw-input').addEventListener('submit', function () {
    var v = input.value.trim(); if (!v) return;
    add(v, true); input.value = '';
    botReply(/espa|hola|abogad|ayuda/i.test(v)
      ? 'Con gusto. Cuéntenos brevemente qué pasó y el mejor número para comunicarnos con usted. Un abogado le dará seguimiento.'
      : 'I am sorry you are dealing with that. Could you tell me a little more about what happened and the best number to reach you? An attorney will follow up.');
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); root.querySelector('.ssw-send').click(); }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeAll(); stopVoice(); } });

  setTimeout(function () { if (!card.classList.contains('open') && !panel.classList.contains('open')) root.classList.add('tip-on'); }, 2500);
  setTimeout(function () { if (!root.classList.contains('listening')) root.classList.remove('tip-on'); }, 11000);
})();
