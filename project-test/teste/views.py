from django.views.generic import ListView

from .models import Teste

class TesteListView(ListView):
    model = Teste
