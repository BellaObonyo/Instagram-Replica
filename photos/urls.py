from django.conf.urls import url
from django.urls import re_path,path
from django.contrib.auth import views as auth_views
from . import views as app_views
from . import views


urlpatterns = [
  path('index/',views.index,name='home'),
  path('accounts/register/',app_views.register,name='register'),
  path('',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('accounts/profile/',views.profile,name='profile'),
  path('update/',app_views.update_profile,name='update_profile'),
  path('post/',app_views.post,name='post'),
  path('photo/<int:photo_id>',views.detail,  name='photo.detail'),
  re_path(r'^comment/(?P<photo_id>\d+)$',app_views.commentFunction,name='commentFunction'),
  re_path(r'^like/(?P<image_id>\d+)', app_views.like, name='like'),
  re_path(r'^allcomments/(?P<photo_id>\d+)$',app_views.allcomments,name='allcomments'),
  re_path(r'^search/$',app_views.search,name='search'),
  re_path(r'^feeds_profile/(?P<pk>\d+)$',app_views.users_profile,name='users_profile'),
  re_path(r'^follow/(?P<user_id>\d+)$',app_views.follow,name='follow'),
  re_path(r'^unfollow/(?P<user_id>\d+)$',app_views.unfollow,name='unfollow'),
  re_path(r'^delete/(?P<photo_id>\d+)$',app_views.delete,name='delete'),


]