from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('users',views.users,name="users"),
    path('members',views.members,name="members"),
    path('create_group',views.create_group, name="create_group"),
    path('save_group',views.save_group, name="save_group"),
    path('create_user',views.create_user, name="create_user"),
    path('create_member',views.create_member, name="create_member"),
    path('login',LoginView.as_view(template_name="groups/login.html"),name="group_login"),
    path('logout',LogoutView.as_view(),name="group_logout"),
    path('group_detail/<id>/',views.group_detail,name="group_detail")
]