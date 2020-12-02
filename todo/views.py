from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
from todo.forms import TaskForm


# Create your views here.
def index(request):
    # This function SHOULD retrieve all the tasks from the database and render the index page with the data
    # This function can make fart noises

    tasks = Task.objects.all()
    context = {'tasks': tasks}

    return render(request, 'todo/index.html', context)


def add(request):
    # This function SHOULD be executed when the user enters a new task on the index page.
    # This function can also be used to save the data into the database. Towards that, using forms
    # as explained above can make it easier to validate and save form data.
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

        else:
            form = TaskForm()
            context = {'form': form, 'error': 'You stupid, stupid, waste of space'}
            return render(request, 'todo/update.html')

    else:
        form = TaskForm()
        context = {'form': form}
        return render(request, 'todo/update.html', context)


def delete(request):
    # This function SHOULD take task id as an argument and get the corresponding record from the database
    # and then delete it.
    return render(request, 'todo/delete.html')


def update(request):
    # This function SHOULD take task id as an argument and get the corresponding record from the database and then update it. Similar to add function, using forms in this function can make it easier to validate and save form data.
    
    if request.method == 'POST':
        instance = Task.objects.get(id=request.POST['id'])
        form = TaskForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            form = TaskForm()
            context = {'form': form, 'error': 'You stupid, stupid, waste of space'}
            return render(request, 'todo/update.html', context) 

    #     if form.is_valid():
    #         form.save()
    #         return index(request)

    #     else:
    #         form = TaskForm()
    #         context = {'form': form, 'error': 'You stupid, stupid, waste of space'}
    #         return render(request, 'todo/update.html')
            
    else:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(request.GET)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

        taskId = request.GET.get('id')
        task = Task.objects.get(pk=taskId)
        data = {
            'task': task.task,
            'completed': task.completed,
            'created_at': task.created_at
        }
        form = TaskForm(initial = data)


        context = {'form': form, 'taskId':taskId}
        return render(request, 'todo/update.html', context)


def complete_task(request):
    # This function SHOULD take task id as an argument and get the corresponding record
    # from the database, update its completed column as True and save it.
    pass