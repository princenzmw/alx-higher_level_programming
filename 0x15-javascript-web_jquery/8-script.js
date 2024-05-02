/* global $ */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (data) {
  const movies = data.results;
  $.each(movies, function (key, movie) {
    console.log(key, movie.title);
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
