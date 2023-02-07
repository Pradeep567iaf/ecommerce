from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View

class home(View):
    def get(self,request):
        return render(request, 'home.html')
        # return HttpResponse("welcome to home page")
