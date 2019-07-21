from django.urls import path, include
from django.urls import reverse_lazy
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
]