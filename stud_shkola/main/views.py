from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def menu(request):
    return render(request,'main/menu.html')
def mirea(request):
    return HttpResponse("<h4>МИРЭА</h4>")