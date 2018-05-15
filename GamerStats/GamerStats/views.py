from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class BaseView(View):
    pass

class HomePage(BaseView):
    def get(self,request):
        return render(request,'HomePage.html',{})
    

class FortNiteHome(BaseView):
    def get(self,request):
        return HttpResponse("Hey Inside Fortnite")