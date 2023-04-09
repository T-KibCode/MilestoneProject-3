const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://moviesdatabase.p.rapidapi.com/titles/x/titles-by-ids?idsList=tt0001702%2Ctt0001856%2Ctt0001856",
	"method": "GET",
	"headers": {
		"X-RapidAPI-Key": "ad2be7f88amshb389857c019ff11p12d386jsn9fa9dc12feb9",
		"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
});