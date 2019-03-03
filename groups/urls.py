from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users',views.users,name="users"),
    path('members',views.members,name="members"),
    path('create_group',views.create_group, name="create_group")
]