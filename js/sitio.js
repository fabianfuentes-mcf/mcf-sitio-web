(function () {
  'use strict';

  /* ---------- menu en pantalla chica ---------- */

  var btn = document.getElementById('btn-menu');
  var menu = document.getElementById('menu');
  if (!btn || !menu) return;

  var chico = function () { return window.matchMedia('(max-width: 900px)').matches; };

  var ajustar = function () {
    if (chico()) {
      menu.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
    } else {
      menu.hidden = false;
    }
  };

  ajustar();
  window.addEventListener('resize', ajustar);

  btn.addEventListener('click', function () {
    var abierto = !menu.hidden;
    menu.hidden = abierto;
    btn.setAttribute('aria-expanded', String(!abierto));
  });

  // al tocar un enlace del menu en el telefono, se cierra
  menu.addEventListener('click', function (e) {
    if (e.target.tagName === 'A' && chico()) {
      menu.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
    }
  });
})();
