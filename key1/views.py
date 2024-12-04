from django.shortcuts import render

# Create your views here.
def key3(request):
    d={'name':'Thunder','age':30}
    return render(request,'key3.html',context=d)