$(document).ready(function () {
  $('input#btn_search').click(function () {
    $.ajax({
      url: 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + $('input#city_search').val() + '%22)&format=json',
      type: 'GET',
      success: result => {
	$('div#wind_speed').text(result.query.results.channel.wind.speed);
      }
    });
  });
});
