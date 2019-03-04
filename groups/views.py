from django.shortcuts import render, redirect
from django.http import HttpResponse
from groups.models import Groups, Members
from django.contrib.auth.models import User
from .forms import GroupForm, UserForm, MemberForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    groups = Groups.objects.all()
    return render(request, "groups/index.html",{
        "active" : "index",
        'groups' : groups
    })

def users(request):
    users = User.objects.all()
    return render(request,'groups/users.html',{
        "active" : "users",
        'users' : users
    })

def members(request):
    members = Members.objects.all()
    return render(request, 'groups/members.html',{
        "active" : "members",
        'members' : members
    })

@login_required
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

@login_required
def save_group(request):
    if request.method == "POST":
        form = GroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else: 
        form = GroupForm()
        return render(request,'groups/save_group.html',{'form':form})

@login_required
def create_user(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid:
            new_user = User.objects.create_user(username=request.POST.get("username"),
                email=request.POST.get("email"),
                password=request.POST.get("password"))
            return redirect("index")
    else:
        form = UserForm()
        return render(request, 'groups/create_user.html',{'form':form})

@login_required
def create_member(request):
    if request.method == "POST":
        form = MemberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MemberForm()
        return render(request, 'groups/create_member.html',{'form':form})

@login_required
def group_detail(request, id):
    group = Groups.objects.get(pk=id)
    return render(request,'groups/group_detail.html',{'model':group})