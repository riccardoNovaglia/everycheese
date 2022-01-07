from django.views.generic import ListView, DetailView

from .models import Cheese


class CheeseDetails(DetailView):
    model = Cheese


class CheeseList(ListView):
    model = Cheese
