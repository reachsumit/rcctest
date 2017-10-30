from django.shortcuts import render
from django.http import HttpResponse
import datetime
from rccproj.webapp.models import Bikes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def add(request):
    now = datetime.datetime.now()
    html = "<html><body>We will add bike here. It is now %s.</body></html>" %now
    return HttpResponse(html)

def home_page(request):
    #b = Bikes(SKU="123",name="meri bike",description="sahi chalti hai",rating=5,price=100,quantity=10,type='0')
    allBikes = Bikes.objects.all()
    paginator = Paginator(allBikes,1)

    page = request.GET.get('page')
    try:
        thisPage = paginator.page(page)
    except PageNotAnInteger:
        thisPage = paginator.page(1)
    except EmptyPage:
        thisPage = paginator.page(paginator.num_pages)

    return render(request,'bike.html',{'thisPage':thisPage})
    html1 = "<html><body>"
    html3 ="</body></html>"
    html2 = ""
    for qres in qqres:
        html2 += "We will add bike here. It is now %s %s %s %d %d %d %s &nbsp " % (qres.SKU, qres.name,qres.description, qres.rating, qres.price, qres.quantity, qres.type)
    return HttpResponse(html1+html2+html3)
