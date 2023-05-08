/* 

$(document).ready(function () {
  $(".btn-primary").click(function () {
    var movie = $(".form-control").val();
    var category = $(".form-select").val();
    $.ajax({
      url: "/search",
      method: "POST",
      data: {
        movie: movie,
        category: category
      },
      success: function (response) {
        console.log(response);
      }
    });
  });
});

*/

// Query Selectors to call results from movies.session.sql database
