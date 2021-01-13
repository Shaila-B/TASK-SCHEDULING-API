from django.shortcuts import render, redirect
from accounts.models import Account
from api.models import Task,Organization
def index(request):
    context = {}
    user_data = Account.objects.all()
    users_list = []
    for i in user_data:
        username = i.username
        users_list.append({'username':username,'userid':i.id})

    
    user_data = Account.objects.all()
   
    users_dict ={}
    for i in user_data:
        username = i.username
        #Working Code For Username
        users_dict[str(i.id)]=username
        #############################
    
    context['usersdata'] = users_dict
    context['accounts'] = users_list
    tasks = Task.objects.all()
    context['tasks'] = tasks
    organization = Organization.objects.all()
    

    context['organization'] = organization
    return render(request, 'frontend/index.html', context)

def create_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        assignee = request.POST.get('assignee')
        status=request.POST.get('status')
        tasks=Task.objects.create(title=title,assignee=assignee,status=status) 
        user=tasks.users.add(assignee)
        print(user)
        print(tasks)
    return redirect('index')
def edit_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        assignee = request.POST.get('assignee')
        status=request.POST.get('status')
        tasks=Task.objects.create(title=title,assignee=assignee,status=status) 
        user=tasks.users.add(assignee)
        print(user)
        print(tasks)
    return redirect('index')
