from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *



class HomeView(TemplateView):
    template_name= 'root/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['Business'] = Business_Card_Portfolios.objects.filter(status=True)
        context['Portfolios_children'] = Portfolios_children.objects.filter(status=True)
        context['special'] = SpecialService.objects.filter(status=True)

        return context
        
class Service(TemplateView):
    template_name = 'root/service.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['special'] = SpecialService.objects.filter(status=True)

        return context


