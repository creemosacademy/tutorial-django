from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class Formulario(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    message = models.TextField()


class FomularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = (
            'name',
            'email',
            'phone',
            'message'
        )
