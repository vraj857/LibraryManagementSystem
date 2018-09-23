from django.conf.urls import url,include
from django.contrib import admin
from .views import DashboardView,UserListView,UserListUpdateView


urlpatterns = [
    url(r'^Dashboard/',DashboardView.as_view(),name= 'dashboard'),
    url(r'^User_Details/',UserListView.as_view(),name = 'user_list'),
    url(r'^user_list_update/(?P<pk>[\w-]+)$', UserListUpdateView.as_view(), name='user_list_update'),
]
