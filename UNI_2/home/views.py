from re import X
from django.shortcuts import render
from django.http import HttpResponse
import UNI_task1_back 
# Create your views here.
def tp(request,a,b):
    x=UNI_task1_back.adj(a,b)
    return HttpResponse ("%s"%x)
    