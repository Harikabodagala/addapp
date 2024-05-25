from django.shortcuts import render
#create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    con_dic = {"sum":z}
    return render(request,'result.html',context=con_dic)