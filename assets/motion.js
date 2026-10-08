/*
 * Shared motion for every concept.
 *   data-reveal            fade up when scrolled into view ("fade", "mask", "line" for variants)
 *   data-stagger="90"      on a parent: children with data-reveal get increasing delays (ms)
 *   data-count="1000"      count up when visible; data-prefix / data-suffix wrap the number
 *   data-header            gets .is-scrolled once the page scrolls past 40px
 *   data-parallax="0.12"   drifts the element slower than the page
 *   .line > span           headline lines revealed on load (set --d for delay)
 */
(function () {
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function onReady(fn) {
    if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn);
  }

  onReady(function () {
    requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('is-loaded'); }); });

    document.querySelectorAll('[data-stagger]').forEach(function (parent) {
      var step = parseInt(parent.getAttribute('data-stagger'), 10) || 90;
      parent.querySelectorAll('[data-reveal]').forEach(function (el, i) {
        if (!el.style.getPropertyValue('--d')) el.style.setProperty('--d', (i * step) + 'ms');
      });
    });

    var counters = document.querySelectorAll('[data-count]');
    function format(n) { return Math.round(n).toLocaleString('en-US'); }
    function runCount(el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var pre = el.getAttribute('data-prefix') || '', suf = el.getAttribute('data-suffix') || '';
      if (reduce) { el.textContent = pre + format(target) + suf; return; }
      var start = null, dur = 1800;
      function tick(t) {
        if (!start) start = t;
        var p = Math.min(1, (t - start) / dur), eased = 1 - Math.pow(1 - p, 4);
        el.textContent = pre + format(target * eased) + suf;
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }

    var revealEls = document.querySelectorAll('[data-reveal]');
    if (reduce || !('IntersectionObserver' in window)) {
      revealEls.forEach(function (el) { el.classList.add('is-in'); });
      counters.forEach(runCount);
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-in');
          if (e.target.hasAttribute('data-count')) runCount(e.target);
          io.unobserve(e.target);
        });
      }, { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
      revealEls.forEach(function (el) { io.observe(el); });
      counters.forEach(function (el) { if (!el.hasAttribute('data-reveal')) io.observe(el); });
    }

    var header = document.querySelector('[data-header]');
    var parallax = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
    var ticking = false;
    function onScroll() {
      if (header) header.classList.toggle('is-scrolled', window.scrollY > 40);
      parallax.forEach(function (el) {
        var r = el.getBoundingClientRect(), speed = parseFloat(el.getAttribute('data-parallax')) || 0.1;
        var limit = r.height * 0.1;
        var offset = Math.max(-limit, Math.min(limit, (r.top + r.height / 2 - window.innerHeight / 2) * -speed));
        el.style.transform = 'translate3d(0,' + offset.toFixed(1) + 'px,0)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
    onScroll();
  });
})();
