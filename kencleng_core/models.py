from django.db import models

# Create your models here.


class Transksi(models.Model):
        a = models.TextField()
        b = models.DecimalField(max_digits=20,decimal_places=2)
        c = models.DateField(auto_now_add=True)
        d = models.DateField(auto_now_add=True)
        e = models.ForeignKey('auth.User', null=False , on_delete=models.CASCADE,)
