from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from .forms import UserRegisterForm, TeamForm, LoginForm
from .models import CustomUser
from django.contrib import messages, auth

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
            auth.login(request, user)
            messages.success(request, f"Bienvenu(e) {user.nom}, Vous êtes maintenant connectés !!!")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect !!!")
            return redirect('accounts:signin')

    context = {'form': form, 'submit_text': 'Se connecter'}
    return render(request, 'accounts/login.html',context)

def logoutView(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO,"Vous venez de vous déconnecter de l'application !!!")
    return redirect('accounts:signin')

def registerUser(request):
    # Si le user ouvre une autre fenetre pour s'enregistrer alors qu'il est déja connecté, on le redirife vers le dashboard
    if request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, "Vous êtes déjà connectés !!!")
        return redirect("home")

    elif request.method == "POST":
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
            context = {'form': form, 'submit_text': 'Enregistrer'}
            return render(request, "accounts/signup.html", context)
    else:
        form = UserRegisterForm()
        context = {'form':form, 'submit_text':'Enregistrer'}
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

class UserListView(ListView):
    paginate_by = 10
    # Modèle sur lequel on travaille
    model = CustomUser
    # le template qui sera rendu au navigateur
    template_name = "accounts/liste_user.html"
    context_object_name = "users"

class TeamCreationView(CreateView):
    template_name = "team/add.html"
    form_class = TeamForm
    # redirection en cas de création d'un user avec succès
    success_url = reverse_lazy('accounts:add_team')
    success_message = "Equipe créée avec succès !!!"

    # Pour envoyer des variables à notre template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Enregistrer"
        return context

    """Validation du formulaire"""
    def form_valid(self, form):
        return super().form_valid(form)