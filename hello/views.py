from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
  return HttpResponse('Hi')

def say_test(request):
  return HttpResponse('Hi test')