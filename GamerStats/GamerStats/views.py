from django.http import HttpResponse
from django.views.generic import View


class BaseView(View):
    pass

class HomePage(BaseView):
    def get(self,request):
        return HttpResponse("<h1>Hey</h1>")
    

