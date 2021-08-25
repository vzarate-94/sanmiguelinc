from django.shortcuts import render
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