from django.conf.urls import url

from .views import SignUpView,LoginView,DashboardView,LogoutView

urlpatterns = [

    url(r'^signup/',SignUpView.as_view(),name='signup'),
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^logout/',LogoutView.as_view(),name='logout'),
    url(r'^dashboard',DashboardView.as_view(),name='dashboard'),
    # url(r'^dashboard/userlistdetails',UserListView.as_view(),name='users_list')

]
