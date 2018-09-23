from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView, ListView
from django.views.generic.edit import FormView, CreateView
from .models import User
from . import forms
# Create your views here.
from .forms import SignUpForm, LoginForm
from django.contrib import auth


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = 'dashboard'
    # #
    #     model = User

    # def login(request):
    #
    #     if request.method == 'POST':
    #
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')
    #
    #         user = auth.authenticate(username=username,password=password)
    #
    #         if user is not None:
    #
    #             auth.login(request,user)
    #             return redirect('dashboard')
    #
    #         else:
    #             messages.error(request,'Error wrong username/password')
    #     return render(request,'login')
    #


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

#
# @login_required
# def logout(request):
#     return render(request,'login')

# class UserListView(ListView):
#     context_object_name = 'users_list'
#     template_name = 'users_list.html'
#
#
#     def get_queryset(self):
#         return User.objects.all()
#
