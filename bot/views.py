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
			myrobot.run()
			return render(request, 'bot/index.html')
		except:
   			print "Error: unable to start"

def qrcode(request):
	return render(request,"bot/qrcode.html")

def check(request):
	if request.method == "GET":
			if myrobot.login_bool == False:
				print "11111"
				return HttpResponse(json.dumps({"status":"error"}))
		 	else:
				print "22222"
				return HttpResponse(json.dumps({"status":"sucess!"}))
	else:
		return render(request, 'bot/qrcode.html')
