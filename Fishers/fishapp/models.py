from django.db import models

# Create your models here.
class River(models.Model):
    rivername = models.CharField(max_length=300)
    fishname = models.CharField(max_length=200)

    def __str__(self):
        return self.rivername

class details(models.Model):
    water = models.ForeignKey(River, on_delete=models.CASCADE)
    rn = models.CharField(max_length=500)
    fn = models.CharField(max_length=500)

    def __str__(self):
        return self.rn
