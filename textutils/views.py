#I have created this file -Larsen
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'Lawrence','place':'Kolalgiri Laximinagar'}
    return render(request,'index.html',params)
#
# def Home(request):
#     return render(request,'home.html')
#     return HttpResponse("Home")
def analyze(request):
    djtext=(request.GET.get('analyze','default'))
    print(analyze)
    print(djtext)
    return HttpResponse("Your form is submitted ")
def GABRIALFURNITURE(request):
    GABRIALFURNITURE={'dark':'Larsen'}
    return render(request,'GABRIALFURNITURE.html',GABRIALFURNITURE)
def LeeshaLarsenGarments(request):
    leesha={'name':'Lawrence','place':'kolalgiri'}
    return render(request,'LeeshaLarsenGarments.html',leesha)
def home(request):
    home = {'dark': 'Larsen'}
    return render(request,'home.html',home)
def chickenshop(request):
    return render(request,'chickenshop.html')
def ContactKrishna(request):
    return render(request,'ContactKrishna.html')
# def capfirst(request):
#     return HttpResponse("Capitalize first ")
#def home(request):
    #return HttpResponse("<h1> This complex has cloths,Furnitures,Printer to print banners machine<h2> Press back to go back to main Menue <a href='/'> back</a>")
 #def capfirst(request):
#     return HttpResponse("Capitalize first ")
# def Newlineremover(request):
#     return HttpResponse("Newlineremover ")

# def home(request):
#     sites = ['''<h1>For cloths </h1><a href = "" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))
def ContactAldron(request):
    ald = {'name': 'Aldron', 'shop': 'GabrialFurniture'}
    return render(request,'ContactAldron.html')
def DigitalPrinting(request):
    return render(request,'DigitalPrinting.html')
def ContactRajath(request):
    ald = {'name': 'Rajath', 'shop': 'DigitalPrinting'}
    return render(request,'ContactRajath.html')
# def zir(request):
#     return render(request,'zir.jpeg')
def contactus(request):
    res = {'name': 'Rajath', 'shop': 'DigitalPrinting'}
    return render(request,'contactus.html')





