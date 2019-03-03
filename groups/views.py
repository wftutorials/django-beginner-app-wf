from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'groups/create_group.html',{
    
    })