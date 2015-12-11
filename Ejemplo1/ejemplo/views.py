from django.shortcuts import render
# Create your views here.

def fsumar(request):
    return render(request,'fsuma.html')

def sumar(request):
    if request.method == 'GET':
        if 'n1' in request.GET and 'n2' in request.GET:
            num1 = request.GET['n1']
            num2 = request.GET['n2']
            suma = int(num1) + int(num2)
            return render(request,'fsuma.html',{'res': suma,'n1':num1,'n2':num2})
        else:
            return render(request,'fsuma.html')
    else:
        if 'n1' in request.POST and 'n2' in request.POST:
            num1 = request.POST['n1']
            num2 = request.POST['n2']
            suma = int(num1) + int(num2)
            return render(request,'fsuma.html',{'res': suma,'n1':num1,'n2':num2})
        else:
            return render(request,'fsuma.html')

def esclava(request):
    return render(request,'esclava.html')

def index(request):
    variable = range(5)
    num = 1
    return render(request, 'index.html',
    {'cadena':'ITSH','variable':variable
    , 'n':num})

def handler404(request):
    return render(request,'error/404.html')
