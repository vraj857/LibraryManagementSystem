from django.conf.urls import url

from .views import DashboardView, UserListView, UserUpdateView

urlpatterns = [
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^user_details/', UserListView.as_view(), name='user_list'),
    url(r'^user_update/(?P<pk>[\w-]+)$', UserUpdateView.as_view(), name='user_update'),
]