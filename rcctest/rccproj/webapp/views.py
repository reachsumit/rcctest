from django.shortcuts import render
from django.http import HttpResponse
import datetime
from rccproj.webapp.models import Bikes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from rccproj.webapp.addnew import bikeForm
from django.shortcuts import redirect

def add_bike(request):
    if request.method == 'POST':
        form = bikeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = bikeForm()
    return render(request, 'add_bike.html', {'form': form})

ITEMS_PER_PAGE = 10

def delete(request):
    delete_id = request.GET.get('delete')
    Bikes.objects.filter(pk=delete_id).delete()
    return redirect('/')
    pass

# Create your views here.
def show(request):
    show = request.GET.get('show')
    print(show)
    res = Bikes.objects.get(pk=show)
    #html = "<html><body>Now I'll pop the display of item SKU: %s.</body></html>" %show
    return render(request,'prod.html',{'res':res})

def home_page(request):
    global ITEMS_PER_PAGE
    allBikes = Bikes.objects.all()
    paginator = Paginator(allBikes,ITEMS_PER_PAGE)

    page = request.GET.get('page')
    try:
        thisPage = paginator.page(page)
    except PageNotAnInteger:
        thisPage = paginator.page(1)
    except EmptyPage:
        thisPage = paginator.page(paginator.num_pages)

    return render(request,'bike.html',{'thisPage':thisPage})
