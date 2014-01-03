(function($){
    var readJson = function(jsonURL){
	$.ajax({
	    type: 'GET',
	    url: jsonURL,
	    dataType: 'json',
	    success: function(json){
		var mylist = json['datas'];
		var len = mylist.length;
		for(var i=0; i<len; i++){
		    var sm = mylist[i];
		    var linkTemp = $('<a />').attr({
			'href':sm['link'],
		    });
		    var imgTemp = $('<img />').attr({
			'src':'http://tn-skr4.smilevideo.jp/smile?i='+sm['Sm'],
			'alt':sm['title'],
			'width':94,
			'height':70,
		    });
		    if ($('#sm0 > #sm'+sm['month']).size() == 0){
			$('#sm0').prepend($('<div/>').attr({
			    'id':"sm"+sm['month'],
			}).prepend($('<h2>'+sm['month']+'月に聞いてた</h2>')));
		    }
		    linkTemp.prepend(imgTemp);
		    linkTemp.appendTo($('#sm0 > #sm'+sm['month']));
		}
	    },
	    error: function(){
		console.log("Error");
	    },
	});
    };
    $(document).ready(function(){
	readJson($.smNumber);
    });
})(jQuery);
