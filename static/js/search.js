// search.js

$(document).ready(function () {
    var searchUrl = $('script[src*="search.js"]').data('url');

    $('#search-form').submit(function (e) {
        e.preventDefault();
        search();
    });

    $('#search-input').on('input', function () {
        search();
    });

    function search() {
        var keyword = $('#search-input').val();
        $.ajax({
            url: searchUrl,
            data: { 'keyword': keyword },
            dataType: 'json',
            success: function (data) {
                var resultsDiv = $('#search-results');
                resultsDiv.empty();

                if (data.products && data.products.length > 0) {
                    for (var i = 0; i < data.products.length; i++) {
                        var product = data.products[i];
                        resultsDiv.append('<p>' + product.product_name + ': ' + product.description + '</p>');
                    }
                } else {
                    resultsDiv.append('<p>No results found</p>');
                }
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
});
