from django.shortcuts import render
from django.views import generic
from .models import PoolCab as Cab
from .models import PoolResource as Other
from .models import PoolFood as Food
from .models import StoreResource
from django.contrib.auth.models import User

class Pool(generic.TemplateView):
    template_name = "pool.html"


class PoolCab(generic.TemplateView):
    template_name = "poolcab.html"
    http_method_names = ['get', 'post']
    def get(self,request):
        data = Cab.objects.all();
        return render(request, 'list.html', {'data': data, })

class PoolFood(generic.TemplateView):
    template_name = "poolfood.html"
    def get(self,request):
        data = Cab.objects.all();
        return render(request, 'list2.html', {'data': data, })

class PoolMisc(generic.TemplateView):
    template_name = "poolmisc.html"
    def get(self,request):
        data = Cab.objects.all();
        return render(request, 'list3.html', {'data': data, })

class Find(generic.TemplateView):
    template_name = "find.html"

class Store(generic.TemplateView):
    template_name = "store.html"

