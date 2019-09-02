document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});

function clickFocus(id) {
  document.getElementById(id).focus();
}

function setYear() {
  let date = new Date();
  let copyrigth_text = 'TG FATEC SOROCABA 2015 >>> 2019 - Grupo 3 - Almoxarifado - Todos os direitos reservados - ' + date.getFullYear() + ' ©';
  document.getElementById('copyrigth').innerHTML = copyrigth_text;
}

var $doc = $('html, body');
$('.menu-link').click(function() {
  $doc.animate({
    scrollTop: $( $.attr(this, 'href') ).offset().top
  }, 1000);
  return false;
});
