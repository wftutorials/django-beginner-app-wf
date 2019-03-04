from django.shortcuts import render, redirect
from django.http import HttpResponse
from groups.models import Groups
from .forms import GroupForm

# Create your views here.
def index(request):
    return render(request, "groups/index.html",{
        "active" : "index"
    })

def users(request):
    return render(request,'groups/users.html',{
        "active" : "users"
    })

def members(request):
    return render(request, 'groups/members.html',{
        "active" : "members"
    })

def create_group(request):
    if request.method == "POST":
        group = Groups()
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")
        author = request.POST.get("author")
        group.name = name
        group.description = description
        group.status = status
        group.author = author
        group.save()
        return HttpResponse("post submitted" + name )
    else:
        return render(request,'groups/create_group.html',{})

def save_group(request):
    if request.method == "POST":
        form = GroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else: 
        form = GroupForm()
        return render(request,'groups/save_group.html',{'form':form})

def create_user(request):
    return render(request, 'groups/create_user.html')

def create_member(request):
    return render(request, 'groups/create_member.html')