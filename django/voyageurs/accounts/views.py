from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from .forms import UserRegisterForm, TeamForm, LoginForm, UserChangeForm
from .models import CustomUser, Team
from persons.models import Person
from django.contrib import messages, auth
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import get_user_daily_counter, get_user_total_counter

# Create your views here.
def loginView(request):
    form = LoginForm()

    # Si le user ouvre une autre fenetre pour se logger alors qu'il est déja connecté, on le redirife vers le dashboard
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, "You are already logged in !")
        return redirect("home")

    # Authentification des users: on recupère l'email et le password saisis dans le formulaire de login
    elif request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        # on teste s'il existe un usr avec ces paramètres de connexion
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, f"Bienvenu(e) {user.nom}, Vous êtes maintenant connectés !!!")
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, "Compte désactivé, veuillez contacter l'administateur du système")
                return redirect('accounts:login')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect !!!")
            return redirect('accounts:signin')

    context = {'form': form, 'submit_text': 'Se connecter'}
    return render(request, 'accounts/login.html',context)

def logoutView(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO,"Vous venez de vous déconnecter de l'application !!!")
    return redirect('accounts:signin')

def chech_user_admin(current_user):
    return current_user.is_admin

@login_required
@user_passes_test(chech_user_admin)
def registerUser(request):
    saisies_total = get_user_total_counter(request.user)
    saisies_jour = get_user_daily_counter(request.user)
    total = Person.objects.all().count()

    if request.method == "POST":
        print(request.POST)
        # on recupère les données saisies dans le formulaire
        form = UserRegisterForm(request.POST)

        # si les données saisies dans le formulaire sont valides
        if form.is_valid():
            # Create an user using create_user method defined in the UserManager class in models.py
            nom = form.cleaned_data['nom']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            equipe = form.cleaned_data['equipe']

            user = CustomUser.objects.create_user(
                nom = nom,
                telephone = telephone,
                email = email,
                password = password,
                equipe = equipe
            )
            user.save()

            # Message flash à afficher si creation ducompte avec succes. Par defaut les messages sont accessibles dans toutes les pages web
            messages.add_message(request, messages.SUCCESS,"Votre compte a été créé avec succès !!!")
            return redirect('accounts:signup')
        else:
            context = {'form': form, 'submit_text': 'Enregistrer', 'total': total, 'saisies_total': saisies_jour, 'saisies_jour': saisies_jour}
            return render(request, "accounts/signup.html", context)
    else:
        form = UserRegisterForm()
        context = {'form':form, 'submit_text':'Enregistrer', 'total': total, 'saisies_total': saisies_jour, 'saisies_jour': saisies_jour}
        return render(request, "accounts/signup.html", context)

"""
class UserRegistrationView(CreateView):
    template_name = "accounts/signup.html"
    form_class = UserRegisterForm
    # redirection en cas de création d'un user avec succès
    success_url = reverse_lazy('home')

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Enregistrer"
        context["messages"] = "Utilisateur créé avec succès !!!"
        return context

    # Validation du formulaire
    def form_valid(self, form):
        return super().form_valid(form)
"""

# LoginRequiredMixin qui est use pour les CBV est l'équivalent de @login_required pour les FBV
class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    # Modèle sur lequel on travaille
    model = CustomUser
    # le template qui sera rendu au navigateur
    template_name = "accounts/liste_user.html"
    context_object_name = "users"
    total = Person.objects.all().count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        return context

    def test_func(self):
        return self.request.user.is_admin


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = UserChangeForm
    template_name = "accounts/modifier_user.html"
    success_url = reverse_lazy('accounts:signout')
    success_message = "Utilisateur modifié avec succès !!!"
    total = Person.objects.all().count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        context["submit_text"] = "Modifier"
        return context

    def test_func(self):
        return self.request.user.is_admin

class TeamCreationView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "team/add.html"
    form_class = TeamForm
    # redirection en cas de création d'un user avec succès
    success_url = reverse_lazy('accounts:add_team')
    success_message = "Equipe créée avec succès !!!"
    total = Person.objects.all().count()

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        context["submit_text"] = "Enregistrer"
        return context

    """Validation du formulaire"""
    def form_valid(self, form):
        # print(form.cleaned_data)
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_admin

class TeamListView(LoginRequiredMixin, ListView):
    # Le modele pour lequel nous voulons lister le contenu
    model = Team
    # template qui sera rendu dans le navigateur
    template_name = "team/list.html"
    context_object_name = "teams"
    total = Person.objects.all().count()

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        return context

class TeamEditView(LoginRequiredMixin, UpdateView):
    # Le modele pour lequel nous voulons modifier les informations
    model = Team
    template_name = "team/edit.html"
    form_class = TeamForm
    # redirection en cas de création d'un user avec succès
    success_url = reverse_lazy('accounts:list_teams')
    success_message = "Equipe modifiée avec succès !!!"
    total = Person.objects.all().count()

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        saisies_total = get_user_total_counter(self.request.user)
        saisies_jour = get_user_daily_counter(self.request.user)

        context["total"] = self.total
        context["saisies_total"] = saisies_total
        context["saisies_jour"] = saisies_jour
        context["submit_text"] = "Modifier"
        return context

    """Validation du formulaire"""
    def form_valid(self, form):
        # print(form.cleaned_data)
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_admin