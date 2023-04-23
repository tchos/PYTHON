from django.shortcuts import render
from datetime import datetime
from django.views import  View
from django.views.generic import TemplateView

class HomView(TemplateView):
    template_name = "home/index.html"
    title = "Default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context