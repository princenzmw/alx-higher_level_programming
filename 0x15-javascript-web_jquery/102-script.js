/* global $ */
$(function () {
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;

    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
