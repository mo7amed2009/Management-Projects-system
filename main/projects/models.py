from django.db import models
from accounts.models import User
# Create your models here.


class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=250,verbose_name='Description Of Project')
    manager=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Manger Of The Project',related_name='manager_project')
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='The Time Of Project')
    members=models.ManyToManyField(User,verbose_name='Responsible Of The Group',related_name='members_project')

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name=models.CharField(max_length=30)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Manger Of The Group',related_name='manager_group')
    description=models.TextField(max_length=250,verbose_name='Description Of Project')
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='The Time Of Project')
    members=models.ManyToManyField(User,verbose_name='Responsible Of The Group',related_name='members_group')
    
    def __str__(self):
        return self.name
    




class Task(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=250,verbose_name='Description Of Task')
    group=models.ForeignKey(Group,on_delete=models.CASCADE,related_name='task_group',null=True,blank=True)
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='The Time Of Task')
    resposible=models.ManyToManyField(User,verbose_name='Responsible Of The Task',related_name='members_task')

    def __str__(self):
        return self.title
    