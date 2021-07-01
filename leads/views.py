from django.shortcuts import reverse
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView, 
    DetailView, 
    UpdateView, 
    DeleteView
    )

from .models import Lead
from leads.forms import LeadModelForm


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadCreateView(CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:list_list")


class LeadDetailView(DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadUpdateView(UpdateView):
    template_name = "lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list.html')


class LeadDeleteView(DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list.html')


class LeadListView(ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"