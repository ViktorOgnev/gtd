from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, CreateView

from .models import Item

class CreateItem(CreateView):
    
    model = Item
    template = "core/add_item_form.html"
    

    
