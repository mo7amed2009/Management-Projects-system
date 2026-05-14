from django.shortcuts import render
from .models import *
from .forms import *
from django.views import View 
from django.views.generic import *
from accounts.views import *
from django.contrib.auth.decorators import user_passes_test ,login_required
from django.db.models import Count ,Q
from django.core.paginator import Paginator
from accounts.permisions import can_edit_group_post
from .filters import ProjectFilter
# Create your views here.


# This For all Projects
@login_required
def all_projects (request):
    query=Project.objects.all().order_by('-create_date').annotate(count_group=Count('group'))
   
    my_filter=ProjectFilter(request.GET,queryset=query)
    
    paginator=Paginator(my_filter.qs,3)
    
    
    page=request.GET.get('page')
    
    projects=paginator.get_page(page)
    
    return render(request,'projects/projects.html',{'projects':projects,
                                                    'filter':my_filter})

def groups(request,project_id):
    try:
        # project=Project.objects.get(id=project_id)
        query=Group.objects.filter(project__id=project_id)
        
        
    except project.DoesNotExist :
        return render(request,'404.html')
    
    
    context={
        # 'project':project,
        'groups':query,
    }
    return render(request,'projects/groups.html',context)

def members(request,project_id,group_id):
    project=Project.objects.get(id=project_id)
    group=Group.objects.get(id=group_id,project__id=project_id)
    
    
    return render(request,'projects/members.html',{'group':group,"project":project})



def all_tasks(request,project_id,group_id,user_id):
    
    project=Project.objects.get(id=project_id)
    
    group=Group.objects.get(project=project,id=group_id)
    
    member=User.objects.get(id=user_id)
    
    task=Task.objects.filter(group=group,resposible=member)
    
    context={
        'project':project,
        'group':group,
        'member':member,
        'task':task,
    }
    return render(request,'projects/tasks.html',context)


def task(request,project_id,group_id,user_id):
    
    project=Project.objects.get(id=project_id)
    
    group=Group.objects.get(project=project,id=group_id)
    
    member=User.objects.get(id=user_id)
    
    task=Task.objects.get(group=group,resposible=member)
    
    context={
        'project':project,
        'group':group,
        'member':member,
        'task':task,
    }
    return render(request,'projects/one_task.html',context)



##########################################
##########################################
##########################################


def add_project(request):
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_projects')
            
    else:
        form=ProjectForm()
    return render(request,'projects/forms/project_form.html',{'form':form})
@user_passes_test(can_edit_group_post)
def add_group(request):
    if request.method == 'POST':
        form=GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_projects')
    else:
        form=GroupForm()
    return render(request,'projects/forms/group_form.html',{'form':form})
@user_passes_test(can_edit_group_post)
def add_task(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_projects')
            
    else:
        form=TaskForm()
    return render(request,'projects/forms/task_form.html',{'form':form})
@user_passes_test(can_edit_group_post)
def update_project(request,project_id):
    project=Project.objects.get(id=project_id)
    
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('all_projects')
    else:
        form=ProjectForm(instance=project)
    
    return render(request,'projects/forms/update_project_form.html',{'form':form})
    
@user_passes_test(can_edit_group_post)
def update_group(request,project_id,group_id):
    
    project=Project.objects.get(id=project_id)
    
    group=Group.objects.get(id=group_id,project=project)

    if request.method == 'POST':
        form=GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('all_projects')
    else:
        form=GroupForm(instance=group)
        
    return render(request,'projects/forms/update_group_form.html',{'form':form})
@user_passes_test(can_edit_group_post)
def update_task(request,project_id,group_id,task_id):
    
    project=Project.objects.get(id=project_id)
    
    group=Group.objects.get(id=group_id,project=project)
    
    task=Task.objects.get(id=task_id,group=group)

    if request.method == 'POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('all_projects')
    else:
        form=TaskForm(instance=task)

    return render(request,'projects/forms/update_task_form.html',{'form':form})
