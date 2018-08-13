from django.shortcuts	import render
from django.http		import HttpResponse, HttpResponseRedirect

def		index(request):
	return render(request, "booking_tool/index.html")

def		send(request):
	pass
# Create your views here.
