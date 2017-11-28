from django.shortcuts import render
from django.views.generic import View


def home(request):
	template="index.html"
	context={}
	return render(request, template, context)

def profile(request):
    return render(request, 'profile.html',{})
