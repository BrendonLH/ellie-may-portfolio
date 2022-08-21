from django.views.generic import TemplateView, DetailView, ListView

from .models import Fact


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/ellie_home.html'


class FactListView(ListView):
    template_name = 'pages/ellie_fact_list.html'
    model = Fact
    context_object_name = 'facts_objects'


class FactDetailView(DetailView):
    model = Fact
    template_name = 'pages/ellie_fact_detail.html'
