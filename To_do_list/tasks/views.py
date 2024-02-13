from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):

        return reverse_lazy('list')
    
class RegisterPage(FormView):
    form_class=UserCreationForm
    template_name='tasks/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)



    
    
@login_required
def index(request):
    tasks = task.objects.filter(user=request.user)
    count = tasks.filter(completed=False).count()
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')           
        
    context = {'tasks':tasks, 'form':form, 'count': count}
    return render(request, 'tasks/list.html',context)

@login_required
def updateTask(request, pk):
    #task = get_object_or_404(task, id=pk)
    Task = task.objects.get(id=pk)
    form = TaskForm(instance=Task)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=Task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)
@login_required
def deleteTask(request, pk):
    item = task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')


    context = {'item':item}
    return render(request, 'tasks/delete.html', context)




