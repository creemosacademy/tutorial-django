from django.shortcuts import render

from django.views.generic import CreateView
from sitio.models import FomularioForm
# Create your views here.

class Index(CreateView):
    template_name = "index.html"
    form_class = FomularioForm

    def get_success_url(self):
        return "/"
