from django.conf.urls import url
from bot import views

urlpatterns = [
	url(r'^index/$',views.index, name='index'),
	url(r'^getwx/$',views.getwx,name='getwx'),
	url(r'^wait/$',views.wait,name='wait'),
	url(r'^qrcode/$',views.qrcode,name='qrcode'),
	url(r'^check/$',views.check,name='check'),
]
