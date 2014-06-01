from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from todo.models import main

class IndexView(generic.ListView):
	template_name = 'todo/index.html'
	context_object_name = 'latest_todo_list'

	def get_queryset(self):
		"""Return all published todo."""
		return main.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
	model = main
	template_name = 'todo/detail.html'

@login_required
def add(request):
	if request.method == 'POST':
		description = request.POST['description']
		amount = request.POST['amount']
		pub_date = request.POST['pub_date']
		ready = False
		user = User.objects.get(id=request.POST['user'])
		id_user = user
		obj = main(description=description, amount=amount, pub_date=pub_date, ready=ready, id_user=id_user)
		obj = obj.save()		
		return HttpResponseRedirect('/todo-list/')
	else:
		context = {
			'main': User.objects.all()
		}
		return render(request, 'todo/add.html', context)

