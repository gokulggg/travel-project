from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    a=Team.objects.all()
    return render(request,"index.html",{'result':obj,'answer':a})

#def arithametic(request):
   # a=int(request.GET['n1'])
   # b=int(request.GET['n2'])
   # w=a+b
   # x=a-b
   # y=a*b
   # z=a/b
   #return render(request,"result.html",{'result':w,'output':x,'answer':y,'value':z})

