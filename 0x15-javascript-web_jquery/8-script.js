$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  success: result => {
    result.results.forEach(element => {
      $('ul#list_movies').append('<li>' + element.title + '</li>');
    });
  }
});
