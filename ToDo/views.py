from django.shortcuts import render, HttpResponseRedirect
from .models import Todo_app
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def home(request):
    todotext = Todo_app.objects.all().order_by("addDate")
    context = {
        'todo': todotext
    }
    return render(request, 'home.html', context)


@csrf_exempt
def addtodo(request):
    current_date = timezone.now()
    content = request.POST['content']
    create_obj = Todo_app.objects.create(addDate=current_date, text=content)
    todo_lenght = Todo_app.objects.all().count()
    return HttpResponseRedirect('/')


@csrf_exempt
def delete(request, iditem):
    Todo_app.objects.get(id=iditem).delete()
    return HttpResponseRedirect('/')
