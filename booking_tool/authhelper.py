from urllib.parse	import quote, urlencode
import requests, base64, json, time

client_id = '49f2667b-1659-4766-87b2-ef8a27dc1034'
client_secret = 'sMHCA6114:%)bwmjqnPMP3['

authority = 'https://login.microsoftonline.com'

authorize_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/authorize?{0}')

token_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/token')

scopes = [
	'openid',
	'offline_access',
	'User.Read',
	'Mail.Read' 
]

def		get_signin_url(redirect_uri):
	params = {
		'client_id': client_id,
		'redirect_uri': redirect_uri,
		'response_type': 'code',
		'scope': ' '.join(str(i) for i in scopes)
	}
	signin_url = authorize_url.format(urlencode(params))

	return (signin_url)

def		get_token_from_code(auth_code, redirect_uri):
	post_data = { 
		'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': redirect_uri,
        'scope': ' '.join(str(i) for i in scopes),
        'client_id': client_id,
        'client_secret': client_secret,
	}

	r = requests.post(token_url, data = post_data)
	try:
		return (r.json())
	except:
		return ('Error retrieving token: {0} - {1}'.format(r.status_code, r.text))

def		get_token_from_refresh_token(refresh_token, redirect_uri):
	post_data = {
		'grant_type': 'refresh_token',
		'refresh_token': refresh_token,
		'redirect_uri': redirect_uri,
		'scope': ' '.join(str(i) for i in scopes),
		'client_id': client_id,
		'client_secret': client_secret,
	}
	r = requests.post(token_url, data=post_data)

	try:
		r.json()
	except:
		return ('Error retrieving token: {0} - {1}'.format(r.status_code, r.text))

def		get_access_token(request, redirect_uri):
	cur_token = request.session['access_token']
	expiration = request.session['token_expires']
	now = int(time.time())
	if (cur_token and now < expiration):
		return (cur_token)
	else:
		refresh_token = request.session['refresh_token']
		new_token = get_token_from_refresh_token(refresh_token, redirect_uri)
		expiration = int(time.time()) + new_token['expires_in'] - 300
		request.session['access_token'] = new_token['access_token']
		request.session['refresh_token'] = new_token['refresh_token']
		request.session['token_expires'] = expiration
		return (new_token['access_token'])

