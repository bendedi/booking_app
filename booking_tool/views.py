from django.shortcuts	import render
from django.template	import loader
from django.http		import HttpResponse, HttpResponseRedirect
from django.urls 		import reverse
from re					import match

from booking_tool.authhelper	import get_signin_url, get_access_token, get_token_from_code
from booking_tool.outlook		import get_me

import datetime, time

MIN = 2
MAX = 80

# remplir > verif > connexion > envoyer > fini

def		index(request):
	# return (HttpResponse("salut"))
	# return (render(request, "booking_tool/index.html"))
	redirect_uri = request.build_absolute_uri(reverse('gettoken'))
	signin_url = get_signin_url(redirect_uri)
	context = {'signin_url' : signin_url}
	return (render(request, "booking_tool/index2.html", context))

#		^[\w .-]+@capgemini\.[a-z]{2,4}$		regex mail

def		check(mail, number, week):
	r1 = True
	r2 = True
	r3 = True
	if (match('^[\w .-]+@capgemini\.[a-z]{2,4}$', mail) == None):
		r1 = False
	try:
		number = int(number)
		if (number < MIN or number > MAX):
			r2 = False
	except ValueError:
			r2 = False
	try:
		cur_year = int(datetime.datetime.now().strftime('%Y'))
		cur_week = int(datetime.datetime.now().strftime('%U')) + 1
		year = int(week[0:4])
		week2 = int(week[6:8])
	except ValueError:
		r3 = False
	else:
		if ((cur_year > year) or (cur_week >= week2)):
			r3 = False
			
	return ({'r1':r1, 'r2':r2, 'r3':r3})

def		send(request):
	mail = request.POST['contact']
	number = request.POST['number']
	week = request.POST['week']				# forme: 20XX-WXX

	results = check(mail, number, week)
	if ((results['r1'] == False) or (results['r2'] == False) or (results['r3'] == False)):
		context = {
			'mail': results['r1'],
			'number': results['r2'],
			'week': results['r3'],
		}
		return (render(request, "booking_tool/error.html", context))
	return (render(request, "booking_tool/success.html"))

def		gettoken(request):
	auth_code = request.GET['code']
	redirect_uri = request.build_absolute_uri(reverse('gettoken'))
	token = get_token_from_code(auth_code, redirect_uri)
	access_token = token['access_token']
	user = get_me(access_token)
	refresh_token = token['refresh_token']
	expires_in = token['expires_in']
	expiration = int(time.time()) + expires_in - 300

	request.session['access_token'] = access_token
	request.session['refresh_token'] = refresh_token
	request.session['token_expires'] = expiration
	return (HttpResponse('User: {0}, Access token: {1}'.format(user['displayName'], access_token)))

def		mail(request):
	access_token = get_access_token(request, request.build_absolute_uri(reverse('booking_tool:gettoken')))
	
	if not access_token:
		return (render(request, "booking_tool/error.html"))
	else:
		return (HttpResponse('Access Found in session {0}'.format(access_token)))



