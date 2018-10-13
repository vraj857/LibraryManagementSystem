from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, UpdateView
from user_authentication.models import User

from .forms import UserUpdateForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class UserListView(LoginRequiredMixin, ListView):
    context_object_name = 'user_list'
    template_name = 'users_list.html'

    def get_queryset(self):
        return User.objects.all()


#
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = '/my_view/user_details/'
    object = None

    def get_form_kwargs(self):
        kwargs = super(UserUpdateView, self).get_form_kwargs()
        # self.print_keyword_args()
        user_id = self.kwargs['pk']
        user = User.objects.get(pk=user_id)
        user_locked = self.is_locked(user)
        kwargs['user'] = user
        kwargs['user_locked'] = user_locked
        return kwargs

    # def print_keyword_args(self):
    #     for key, value in self.kwargs.items():
    #         print("%s = %s" % (key, value))

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # checks whether the current user is locked or not by checking login_attempts,account_locked_dt and is_active
    def is_locked(self, user):
        if user.is_active is True and user.login_attempts == 0 and user.account_locked_dt is None:
            return False
        return True
