from django.db import models

# Create your models here.
class Rooftop(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  price = models.IntegerField()

  def __str__(self):
    return self.name