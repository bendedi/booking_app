from django.shortcuts	import render
from django.template	import loader
from django.http		import HttpResponse, HttpResponseRedirect

def		index(request):
	# return (HttpResponse("salut"))
	return (render(request, "booking_tool/index.html"))

def		send(request):
	pass
# Create your views here.
