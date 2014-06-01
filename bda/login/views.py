from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def index(request):
	if request.method == 'POST':
		username = request.POST['username']	
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/todo-list/')
		else:
			return render(request, 'login/index.html', {})	
	else:
		return render(request, 'login/index.html', {})
		