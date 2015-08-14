from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import ChoreList, Chore

def index(request):
	lists = ChoreList.objects.all()
	return render(request, 'chores/index.html', { 'chorelists': lists })

def detail(request, chorelist_id):
	list = get_object_or_404(ChoreList, pk=chorelist_id)
	return render(request, 'chores/detail.html', {'chorelist': list})

def choredetail(request, chorelist_id, chore_id):
	list = get_object_or_404(ChoreList, pk=chorelist_id)
	chore = get_object_or_404(Chore, pk=chore_id)
	return render(request, 'chores/choredetail.html', {'chorelist': list, 'chore': chore})
	
def newlist(request):
	if request.POST:
		list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
		list.save()
		return HttpResponseRedirect('/chores')
	else:
		return render(request, 'chores/newlist.html', {})
		
def deletelist(request, chorelist_id):
	list = get_object_or_404(ChoreList, pk=chorelist_id)
	if request.POST:
		list.delete()
		return HttpResponseRedirect('/chores')
	else:
		return render(request, 'chores/deletelist.html', {'chorelist': list})
		
def addchore(request, chorelist_id):
	list = get_object_or_404(ChoreList, pk=chorelist_id)
	if request.POST:
		chore = Chore(name=request.POST['name'], due_date=request.POST['duedate'])
		if 'complete' in request.POST:
			chore.complete = True
		else:
			chore.complete = False
		list.chore_set.add(chore)
		list.save()
		return HttpResponseRedirect('/chores/' + chorelist_id)
	else:
		return render(request, 'chores/addchore.html', {'chorelist': list})
		

def updatechore(request, chorelist_id, chore_id):
	chore = get_object_or_404(Chore, pk=chore_id)
	if 'complete' in request.POST:
		chore.complete = True
	else:
		chore.complete = False
	
	chore.save()
	
	return HttpResponseRedirect('/chores/' + chorelist_id + '/chores/' + chore_id)
	