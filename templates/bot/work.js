{% extends "bot/base.html" %}
{% load staticfiles %}
<script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/tether/1.4.0/js/tether.min.js"></script>
<script src="http://v4-alpha.getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
<link href="http://v4-alpha.getbootstrap.com/examples/signin/signin.css" rel="stylesheet">
function wait()
{
	var t;
		$.ajax({
            url:"/bot/wait/",
            type:'GET',
            success: function (data) {
                alert("hhehehhe");
                data = JSON.parse(data)
                if(data["status"])
                {
                    alert(data["arg"]);
					postMessage(data["arg"]);
					clearTimeout(t);
                    window.location.href='bot/qrcode';
                }
                else{
                    alert(data["arg"]);
					postMessage(data["arg"]);
					t = setTimeout("wait()",1000);

                }
            }

})
}
wait()
