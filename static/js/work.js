function wait()
{
	var t;
		$.ajax({
            url:"/bot/wait/",
            type:'GET',
            success: function (data) {
                
                data = JSON.parse(data)
                if(data["status"] == "two")
                {
					
					clearTimeout(t);
					postMessage("hello","*");
                    window.location.href='bot/qrcode';
					
					$.ajax({
                                url:"/bot/check/",
                                type:'GET',
                            success: function (data) {
                                
                            }});    
                }
				else if(data["status"] == "one"){
					var dialog = bootbox.dialog({
    				message: data["arg"],
   					closeButton: false,
					className: 'bb-alternate-modal'
					});
// do something in the background
				//	dialog.modal('hide');
					t = setTimeout("wait()",3000);
				}
                else if(data["status"] == "three")
				{
					bootbox.alert(data["arg"]);
					t = setTimeout("wait()",4000);
                }
				else{
					
				}
            }

})
}
wait()
