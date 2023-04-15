from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
def homeView(request):
    project = Project.objects.all()
    context ={'project':project}
    return render(request,'project/home.html',context)

def projectView(request,pk):
    project = Project.objects.get(id = pk)
    context ={'project':project}
    return render(request,'project/single-project.html',context)


def createView(request):
    form = ProjectForm()
    if request.method== 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'project/form-template.html',context)

def updateView(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST' :
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'project/form-template.html',context)

def deleteView(request,pk):
    project = Project. objects.get(id= pk)
    if request.method =='POST':
        project.delete()
        return redirect('home')
    context ={}
    return render(request,'project/delete-template.html',context)