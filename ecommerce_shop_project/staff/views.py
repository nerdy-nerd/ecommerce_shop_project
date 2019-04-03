from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView


class PanelView(TemplateView):
    template_name = "TEMPLATE_NAME"

    pass


class AddProductView(TemplateView):
    template_name = "TEMPLATE_NAME"

    pass
