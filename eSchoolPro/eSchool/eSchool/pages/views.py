from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	return render(request,'homepage.html',
				{'section': 'homepage'})

def about_page(request):
	return render(request,'aboutpage.html',
				{'section': 'aboutpage'})	

def service_page(request):
	return render(request,'servicepage.html',
				{'section': 'servicepage'})	

def project_page(request):
	return render(request,'projectpage.html',
				{'section': 'projectpage'})

def course_page(request):
	return render(request,'coursepage.html',
				{'section': 'coursepage'})

def contact_page(request):
	return render(request,'contactpage.html',
				{'section': 'contactpage'})

def location_page(request):
	return render(request,'baidumap.html')

def home_test(request):
	return render(request,'hometest.html')