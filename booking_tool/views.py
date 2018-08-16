from django.shortcuts	import render
from django.template	import loader
from django.http		import HttpResponse, HttpResponseRedirect
from re					import match

MIN = 2
MAX = 80

def		index(request):
	# return (HttpResponse("salut"))
	return (render(request, "booking_tool/index.html"))

def		success(request):
	return (render(request, "booking_tool/success.html"))

def		failure(request):
	return (render(request, "booking_tool/failure.html"))

#		^[\w .-]+@[\w .-]{2,}\.[a-z]{2,4}$		mail
def		check(mail, number, week):
	r1 = True
	r2 = True
	r3 = True
	if (match('^[\w .-]+@[\w .-]{2,}\.[a-z]{2,4}$', mail) == None):
		r1 = False
	print(number)
	try:
		print(number)
		number = int(number)
		if (number < MIN or number > MAX):
			r2 = False
	except:
			r2 = False
	print(r2)
	# date = datetime.date
	# if ():
	# 	r3 = False
	return ({'r1':r1, 'r2':r2, 'r3':r3})

def		send(request):
	mail = request.POST['contact']
	number = request.POST['number']
	week = request.POST['week']				# forme: 20XX-WXX

	results = check(mail, number, week)
	if (results['r1'] == False or results['r2'] == False or results['r3'] == False):
		return (render(request, "booking_tool/error.html", results))
	return (HttpResponse())

# Create your views here.
