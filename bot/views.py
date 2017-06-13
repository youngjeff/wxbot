# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from wxbot import *
import ConfigParser
import json
from robot import *
from django.shortcuts import render
import time
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
import thread
from django.urls import reverse
myrobot = TulingWXBot()

UNKONWN = 'unkonwn'
SUCCESS = '200'
SCANED = '201'
TIMEOUT = '408'
FAILED = '400'
def index(request):
	return render(request, 'bot/index.html')

def getwx(request):
	
	if request.method == "GET":
		myrobot.DEBUG = True
		myrobot.conf['qr'] = 'png'
		myrobot.runinit()
        

	return render(request, 'bot/index.html')		
def wait(request):
	if request.method == "GET":
		try:
			LOGIN_TEMPLATE = 'https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s'
			tip = 1

			try_later_secs = 1
			MAX_RETRY_TIMES = 10

			code = UNKONWN
			if myrobot.flag:
				print "66666666666"
			else:
				return HttpResponse(json.dumps({"status":"five","arg":"xxxxx"}))
			retry_time = MAX_RETRY_TIMES
			if myrobot.uuid != '':
				print "77777777777"
			else:
				return HttpResponse(json.dumps({"status":"five","arg":"xxxxx"}))
			url = LOGIN_TEMPLATE % (tip, myrobot.uuid, int(time.time()))
			code, data = myrobot.do_request(url)
			print code
			if code == SCANED:
				tip = 0
				print "11111111111"
				return HttpResponse(json.dumps({"status":"one","arg":"请在手机端验证登陆！"}))
			if code == SUCCESS:
				print "222222222222"
				param = re.search(r'window.redirect_uri="(\S+?)";', data)
				redirect_uri = param.group(1) + '&fun=new'
				myrobot.redirect_uri = redirect_uri
				myrobot.base_uri = redirect_uri[:redirect_uri.rfind('/')]
				temp_host = myrobot.base_uri[8:]
				myrobot.base_host = temp_host[:temp_host.find("/")]
				myrobot.flag = False
				return HttpResponse(json.dumps({"status":"two" ,"arg":"恭喜登陆成功微信机器人！"}))
			if code == TIMEOUT:
				print "333333333333333"
				return HttpResponse(json.dumps({"status":"three","arg":"请在10s内登陆微信机器人，否则请刷新！"}))
			if code == FAILED:
				print "444444444444444"
				return HttpResponse(json.dumps({"status":"four","arg":"微信机器人登陆失败，请重试！"}))
		except:
			print "555555555555555"
			return HttpResponse(json.dumps({"status":"five","arg":"xxxxx"}))
def qrcode(request):
	
	return render(request,"bot/qrcode.html")

def check(request):
	if request.method == "GET":
			myrobot.run();
			return render(request, 'bot/qrcode.html')	
