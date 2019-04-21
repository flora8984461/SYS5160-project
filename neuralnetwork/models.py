from django.db import models
import neuralnetwork
# Create your models here.

class weights(models.Model):

    weight = models.CharField(max_length=2000)
    file = models.FileField(upload_to='aftertrained/')

    def __str__(self):
        return self.weight
    