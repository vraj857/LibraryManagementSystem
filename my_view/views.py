from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView,UpdateView

from user_authentication.models import User


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'


class UserListView(LoginRequiredMixin,ListView):

    context_object_name = 'user_list'
    template_name = 'users_list.html'


    def get_queryset(self):
        return User.objects.all()
#
class UserListUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['login_attempts','is_active','user_role','account_locked_dt']
    template_name = 'user_list_update.html'
    success_url = '/my_view/User_Details/'
    # slug_field = 'user_role_id'
    #
    # def get_success_url(self):
    #     return reverse_lazy('dashboard', kwargs={'pk': self.get_object().id})
    # def set_active(self,active):
    #     if active is True:
    #         sel

