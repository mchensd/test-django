from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Counter(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.all()[0].pk)
    count = models.IntegerField()
    name = models.CharField(max_length=128, default="")
    def __str__(self):
         self.name + " " + str(self.count)


