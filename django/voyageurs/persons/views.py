from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import PersonForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Count

from persons.models import Person
from accounts.utils import get_user_daily_counter, get_user_total_counter


# Create your views here.
# LoginRequiredMixin qui est use pour les CBV est l'équivalent de @login_required pour les FBV
class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Person
    template_name = 'person/add.html'
    form_class = PersonForm
    success_message = 'Agent voyageur enregistré avec succès !!!'
    success_url = reverse_lazy('persons:add')
    total = Person.objects.all().count()

    """Validation du formulaire"""
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.collector = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.user.is_authenticated:
            form.instance.collector = self.request.user
        print(form.cleaned_data)
        return JsonResponse(form.errors, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        context["submit_text"] = "Enregistrer"
        return context

class PersonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Person
    template_name = 'person/edit.html'
    form_class = PersonForm
    success_message = 'Agent voyageur modifié avec succès !!!'
    success_url = reverse_lazy('persons:list')
    total = Person.objects.all().count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        return context

    """Validation du formulaire"""
    def form_valid(self, form):
        return super().form_valid(form)


class PersonListView(LoginRequiredMixin, ListView):
    # Le modele pour lequel nous voulons lister le contenu
    model = Person
    # template qui sera rendu dans le navigateur
    template_name = "person/list.html"
    context_object_name = "persons"
    total = Person.objects.all().count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        return context

class StatistiquesView(TemplateView):
    template_name = "person/statistiques.html"
    total = Person.objects.all().count()
    users_count = Person.objects.values("collector__nom").annotate(nb_saisies=Count("nom")).order_by("-nb_saisies")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["users_count"] = self.users_count
        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        return context