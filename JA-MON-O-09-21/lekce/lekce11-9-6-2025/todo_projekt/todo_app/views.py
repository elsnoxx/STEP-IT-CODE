# todo_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.utils import timezone

def index(request):
    """Hlavní stránka s přidáváním úkolů"""
    if request.method == 'POST':
        # Získej data z formuláře (ukol, poznamka, ocekavane, predmet)
        # Vytvoř nový Todo objekt pomocí Todo.objects.create()
        # Přesměruj na stejnou stránku
        pass
    
    # Načti všechny úkoly kde deleted=False, seřaď podle data vytvoření
    # Vrať render s template 'index.html' a seznamem úkolů
    return render(request, 'index.html')

def done(request, pk):
    """Označení úkolu jako splněného/nesplněného"""
    if request.method == 'POST':
        # Najdi úkol podle pk pomocí get_object_or_404
        # Přepni hodnotu done (True/False)
        # Pokud je done=True, nastav completed=aktuální čas
        # Pokud je done=False, nastav completed=None
        # Ulož změny pomocí save()
        pass
    # Přesměruj na hlavní stránku
    pass

def delete(request, pk):
    """Soft delete úkolu"""
    # Najdi úkol podle pk
    # Nastav deleted=True a deleted_at=aktuální čas
    # Ulož změny
    # Přesměruj na hlavní stránku
    pass

def edit(request, pk):
    """Editace existujícího úkolu"""
    # Najdi úkol podle pk
    if request.method == 'POST':
        # Aktualizuj všechna pole úkolu z formuláře
        # Ulož změny
        # Přesměruj na hlavní stránku
        pass
    # Pro GET požadavek vrať template 'edit.html' s úkolem
    pass

def history(request):
    """Zobrazení historie splněných a smazaných úkolů"""
    # Načti splněné úkoly: done=True, deleted=False
    # Načti smazané úkoly: deleted=True
    # Vrať template 'history.html' s oběma seznamy
    pass