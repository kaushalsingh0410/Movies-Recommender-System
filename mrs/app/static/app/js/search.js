$(document).ready(function(){

$(document).on('click','.pagination a', function(e) {
e.preventDefault();
    const pageUrl = $(this).attr('href');

    $.get(pageUrl,function(data){
        $('.result').html(data);
    })
})
})