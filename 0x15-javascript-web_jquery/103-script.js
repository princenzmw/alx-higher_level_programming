/* global $ */
$(function () {
  function translate () {
    const langCode = $('#language_code');
    const language = langCode.val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;

    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
      langCode.val('');
    });
  }

  $('#btn_translate').click(translate);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      translate();
    }
  });
});
