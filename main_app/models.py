from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
EXPENSIVE = (
  (1, 'Very Affordable'),
  (2, 'Affordable'),
  (3, 'Average'),
  (4, 'Expensive'),
  (5, 'Very Expensive')
)

class Rooftop(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  price = models.IntegerField(
    choices=EXPENSIVE,
    default=EXPENSIVE[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('rooftops_detail', kwargs={'rooftop_id': self.id})
  
class Photo(models.Model):
  url = models.CharField(max_length=250)
  rooftop = models.OneToOneField(Rooftop, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for rooftop_id: {self.rooftop_id} @{self.url}"