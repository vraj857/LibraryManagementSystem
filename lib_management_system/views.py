from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.views.generic import ListView



class MyView(TemplateView):
    template_name = 'index.html'
