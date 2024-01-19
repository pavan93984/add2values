from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def second(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    if 'add' in request.POST:
        res = n1 + n2
    elif 'sub' in request.POST:
        res = n1 - n2
    elif 'mul' in request.POST:
        res = n1 * n2
    elif 'div' in request.POST:
        res = n1 // n2
    elif 'mod' in request.POST:
        res = n1 % n2

    return render(request,"second.html",{'res':res})


