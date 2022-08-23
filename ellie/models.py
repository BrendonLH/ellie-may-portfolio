from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class Fact(models.Model):
    name = models.CharField(max_length=50)
    reason = models.TextField(default=' ')
    image = models.ImageField(upload_to='images', default='')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fact_detail', args=[str(self.id)])
