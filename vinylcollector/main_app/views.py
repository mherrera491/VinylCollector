from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from.models import Vinyl
from .forms import PurchaseForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyl_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyl/index.html', { 'vinyls': vinyls })
        
def vinyl_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    purchase_form = PurchaseForm()
    return render(request, 'vinyl/detail.html', { 'vinyl': vinyl, 'purchase_form': purchase_form })

class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'

class VinylUpdate(UpdateView):
    model = Vinyl
    fields = '__all__'

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyl/'

def add_purchase(request, vinyl_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.vinyl_id = vinyl_id
        new_purchase.save()
    return redirect('detail', vinyl_id=vinyl_id)