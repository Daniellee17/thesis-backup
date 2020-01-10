from django.db import models

# Create your models here.
#ONE CLASS ONE TABLE

class sensors(models.Model):
    temperature = models.FloatField(max_length=250, default=0.0);
    moisture = models.FloatField(max_length=250, default=0.0);
    humidity = models.FloatField(max_length=250, default=0.0);
    summary = models.TextField(max_length=250, default="None");
    date = models.DateTimeField(auto_now=True);


class devicestatus(models.Model):
    fansStatus = models.TextField(max_length=250, default="off");
    lightsStatus = models.TextField(max_length=250, default="off");
    waterStatus = models.TextField(max_length=250, default="off");
    seedStatus = models.TextField(max_length=250, default="off");
    date = models.DateTimeField(auto_now=True);

class cameraSnaps(models.Model):
    camera = models.ImageField(default='default.png', blank=True);
    date = models.DateTimeField(auto_now=True);
