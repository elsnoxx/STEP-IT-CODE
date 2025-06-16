# todo_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Count, Q

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error' : 'Chybne prihlasovaci udaje'})
    return render(request, 'login.html' )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form' : form})

def user_logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('login')

@login_required
def index(request):
    """Hlavní stránka s přidáváním úkolů"""
    if request.method == 'POST':
        # Získej data z formuláře (ukol, poznamka, ocekavane, predmet)
        # Vytvoř nový Todo objekt pomocí Todo.objects.create()
        # Přesměruj na stejnou stránku
        text = request.POST.get('ukol')
        poznamka = request.POST.get('poznamka', '')
        ocekavane = request.POST.get('ocekavane') or None
        predmet = request.POST.get('predmet', '')
        
        if text:
            Todo.objects.create(
                user = request.user, # pridani uzivatele do objektu
                text=text,
                poznamka=poznamka,
                ocekavane=ocekavane,
                predmet=predmet
            )
        return redirect('index')
    # Načti všechny úkoly kde deleted=False, seřaď podle data vytvoření
    # Vrať render s template 'index.html' a seznamem úkolů
    todos = Todo.objects.filter(user=request.user, deleted=False).order_by('-created')
    return render(request, 'index.html', {'todos': todos})

@login_required
def done(request, pk):
    """Označení úkolu jako splněného/nesplněného"""
    if request.method == 'POST':
        # Najdi úkol podle pk pomocí get_object_or_404
        # Přepni hodnotu done (True/False)
        # Pokud je done=True, nastav completed=aktuální čas
        # Pokud je done=False, nastav completed=None
        # Ulož změny pomocí save()
        todo = get_object_or_404(Todo, pk=pk, user=request.user) # pridani filtrovani, tak aby sli videt pouze ukoly pro daneho uzivatele
        todo.done = not todo.done
        if todo.done:
            todo.completed = timezone.now()
        else:
            todo.completed = None
        todo.save()
    # Přesměruj na hlavní stránku
    return redirect('index')

@login_required
def delete(request, pk):
    """Soft delete úkolu"""
    # Najdi úkol podle pk
    # Nastav deleted=True a deleted_at=aktuální čas
    # Ulož změny
    # Přesměruj na hlavní stránku
    todo = get_object_or_404(Todo, pk=pk, user=request.user) # pridani filtrovani, tak aby sli videt pouze ukoly pro daneho uzivatele
    todo.deleted = not todo.deleted
    todo.deleted_at = timezone.now()
    todo.save()
    return redirect('index')

@login_required
def edit(request, pk):
    """Editace existujícího úkolu"""
    # Najdi úkol podle pk
    todo = get_object_or_404(Todo, pk=pk, user=request.user) # pridani filtrovani, tak aby sli videt pouze ukoly pro daneho uzivatele
    if request.method == 'POST':
        # Aktualizuj všechna pole úkolu z formuláře
        # Ulož změny
        # Přesměruj na hlavní stránku
        todo.text = request.POST.get('ukol', todo.text)
        todo.poznamka = request.POST.get('poznmka', todo.poznamka)
        ocekavane = request.POST.get('ocekavane')
        if ocekavane:
            todo.ocekavane = ocekavane
        else:
            todo.ocekavane = None
        
        todo.predmet = request.POST.get('predmet', todo.predmet)
        todo.save()
        return redirect('index')
    # Pro GET požadavek vrať template 'edit.html' s úkolem
    return render(request, 'edit.html', {'todo': todo})

@login_required
def history(request):
    """Zobrazení historie splněných a smazaných úkolů"""
    # Načti splněné úkoly: done=True, deleted=False
    # Načti smazané úkoly: deleted=True
    # Vrať template 'history.html' s oběma seznamy
    splnene = Todo.objects.filter(user=request.user, done=True, deleted=False).order_by('-completed')
    smazane = Todo.objects.filter(user=request.user, deleted=True).order_by('-deleted_at')
    return render(request, 'history.html', {'splnene': splnene, 'smazane': smazane})

@login_required
def admin_stats(request):
    users_stats = []
    for user in User.objects.all():
        stats = {
            'user' : user,
            'aktivni' : Todo.objects.filter(user=user, done=False, deleted=False).count(),
            'splnene' : Todo.objects.filter(user=user, done=True, deleted=False).count(),
            'smazane' : Todo.objects.filter(user=user, done=False, deleted=True).count(),
            'celkem' : Todo.objects.filter(user=user).count(),
        }
        users_stats.append(stats)

    total_stats = {
        'celkem_uzivatelu': User.objects.count(),
        'celkem_ukolu': Todo.objects.count(),
        'aktivni_ukoly': Todo.objects.filter(done=False, deleted=False).count(),
        'splnene_ukoly': Todo.objects.filter(done=True, deleted=False).count(),
        'smazane_ukoly': Todo.objects.filter(deleted=True).count(),
    }

    return render(request, 'admin-stats.html', {'users_stats' : users_stats , 'total_stats' : total_stats})