(function($){
    $(document).ready(function(){
	$('#jquery_practice').submit(function(event){
	    event.preventDefault();
	    var $form = $(this);
	    var $button = $form.find('button');
	    $.ajax({
		url: $form.attr('action'),
		type: $form.attr('method'),
		data: $form.serialize(),
		timeout: 10000,
		beforeSend: function(xhr,settings){
		    $button.attr('disabled',true);
		},
		complete: function(xhr, textStatus) {
                    $button.attr('disabled', false);
		},
		// 通信成功時の処理
		success: function(result, textStatus, xhr) {
                    $form[0].reset();
                    $('#result').text('OK');
		    $('#result').html($('#result').text()+result);
		},
		error: function(xhr, textStatus, error) {},
	    });
	});
    });

})(jQuery);
