from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rooftop

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def rooftops_index(request):
  rooftops = Rooftop.objects.all()
  return render(request, 'rooftops/index.html', { 'rooftops': rooftops })

def rooftops_detail(request, rooftop_id):
  rooftop = Rooftop.objects.get(id=rooftop_id)
  return render(request, 'rooftops/detail.html', { 'rooftop': rooftop })

class RooftopCreate(CreateView):
  model = Rooftop
  fields = '__all__'
  success_url = '/rooftops/'

class RooftopUpdate(UpdateView):
  model = Rooftop
  # Let's disallow the renaming of a Rooftop by excluding the name field!
  fields = ['name', 'description', 'price']

class RooftopDelete(DeleteView):
  model = Rooftop
  success_url = '/rooftops/'