/* global $ */
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url, function (data) {
  $('#character').html(data.name);
});
