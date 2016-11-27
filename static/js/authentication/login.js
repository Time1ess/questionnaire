$('.js-captcha-refresh').click(function(){
    $form = $(this).parents('form');
    var url = '/captcha/refresh';
    $.getJSON(url, {}, function(json) {
        $('#id_captcha_0').attr('value', json['key']);
        // alert(json['image_url']);
        $('.captcha').attr('src', json['image_url']);
        // This should update your captcha image src and captcha hidden input
    });

    return false;
});
function security_hash()
{
    return true;
}
