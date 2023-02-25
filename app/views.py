from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Teacher

# Create your views here.

class TeacherData(TemplateView):
    template_name = 'app/home.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        teacher = Teacher.objects.all()
        context = {'teacher':teacher}
        return context