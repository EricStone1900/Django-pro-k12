from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # previous login view
    path('home/', views.home_page, name='homepage'),
    path('about/',views.about_page,name='aboutpage'),
    path('service/',views.service_page,name='servicepage'),
    path('project/',views.project_page,name='projectpage'),
    path('course/',views.course_page,name='coursepage'),
    path('contact/',views.contact_page,name='contactpage'),
    path('location/',views.location_page,name='locationpage'),
    path('hometest/',views.home_test,name='hometest'),
    path('',views.home_page, name='homepage'),
]
