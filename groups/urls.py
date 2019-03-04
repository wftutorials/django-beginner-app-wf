from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users',views.users,name="users"),
    path('members',views.members,name="members"),
    path('create_group',views.create_group, name="create_group"),
    path('save_group',views.save_group, name="save_group"),
    path('create_user',views.create_user, name="create_user"),
    path('create_member',views.create_member, name="create_member")
]