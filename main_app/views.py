from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Rooftop, Photo
import uuid
import boto3

S3_BASE_URL = "https://s3.us-east-1.amazonaws.com/"
BUCKET = 'sanmiguelinc-bucket'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Login(LoginView):
  template_name = 'login.html'

def rooftops_index(request):
  rooftops = Rooftop.objects.all()
  return render(request, 'rooftops/index.html', { 'rooftops': rooftops })

def rooftops_detail(request, rooftop_id):
  rooftop = Rooftop.objects.get(id=rooftop_id)
  return render(request, 'rooftops/detail.html', { 'rooftop': rooftop })

class RooftopCreate(CreateView):
  model = Rooftop
  fields = ['name', 'description', 'price']
  success_url = '/rooftops/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RooftopUpdate(UpdateView):
  model = Rooftop
  # Let's disallow the renaming of a Rooftop by excluding the name field!
  fields = ['name', 'description', 'price']

class RooftopDelete(DeleteView):
  model = Rooftop
  success_url = '/rooftops/'

def add_photo(request, rooftop_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, rooftop_id=rooftop_id)
      rooftop_photo = Photo.objects.filter(rooftop_id=rooftop_id)
      if rooftop_photo.first():
        rooftop_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('rooftops_detail', rooftop_id=rooftop_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('rooftops_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)