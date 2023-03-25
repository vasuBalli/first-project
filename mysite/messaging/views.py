from django.shortcuts import render
from django.http import HttpResponse
msgs_list = []
x = {'user2':"hi"}
def home(request):
    msg=request.GET.get("user")
    msgs_list.append(str(msg))
    return render(request,'home.html',{'msgs':msgs_list})
def client1(request):
    msg = request.GET.get("client1")
    msgs_list.append("_"+str(msg))
      
    return render(request,"client.html",{'msgss':msgs_list})