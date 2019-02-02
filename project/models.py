from django.db import models


# Create your models here.
class Counter(models.Model):
    count = models.IntegerField()
    name = models.CharField(max_length=128, default="")
    def __str__(self):
        return self.name + " " + str(self.count)
