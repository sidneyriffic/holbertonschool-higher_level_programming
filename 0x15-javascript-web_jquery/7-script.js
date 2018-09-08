$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET',
  success: result => {
    $('div#character').text(result.name);
  }
});
