/* global $ */
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.getJSON(url, function (data) {
  const hello = data.hello;
  $('#hello').text(hello);
});
