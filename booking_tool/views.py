from django.shortcuts	import render
from django.template	import loader
from django.http		import HttpResponse, HttpResponseRedirect
from re					import match

MIN = 2
MAX = 80

def		index(request):
	# return (HttpResponse("salut"))
	return (render(request, "booking_tool/index.html"))

def		send(request):
	mail = request.POST['contact']
	number = request.POST['number']
	week = request.POST['week']				# forme: 20XX-WXX

# Create your views here.
