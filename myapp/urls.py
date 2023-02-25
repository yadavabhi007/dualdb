from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentData.as_view(), name='student'),
    
]
