from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'tassu','age':24}
    return render(request,'wish.html',context=d)