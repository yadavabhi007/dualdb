from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Student
# Create your views here.

class StudentData(TemplateView):
    template_name = 'myapp/home.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        student = Student.objects.all()
        context = {'student':student}
        return context