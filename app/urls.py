from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.TeacherData.as_view(), name='teacher'),
    
]
