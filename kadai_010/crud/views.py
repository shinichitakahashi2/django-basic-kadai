from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import product
from django.urls import reverse_lazy

# Create your views here.
class TopView(TemplateView):
  template_name="top.html"

class ProductListView(ListView):
  model = product
  paginate_by =3
  template_name="list.html"

class ProductCreateView(CreateView):
  model = product
  fields ='__all__'

class ProductUpdateView(UpdateView):
  model = product
  fields ='__all__'
  template_name_suffix ='_update_form'

class ProductDeleteView(DeleteView):
  model = product
  success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
  model = product
  fields ='__all__'

  