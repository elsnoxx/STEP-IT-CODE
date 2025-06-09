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
        text = request.POST.get('ukol')
        poznamka = request.POST.get('poznamka', '')
        ocekavane = request.POST.get('ocekavane') or None
        predmet = request.POST.get('predmet', '')
        
        if text:
            Todo.objects.create(
                text=text,
                poznamka=poznamka,
                ocekavane=ocekavane,
                predmet=predmet
            )
        return redirect('index')
    # Načti všechny úkoly kde deleted=False, seřaď podle data vytvoření
    # Vrať render s template 'index.html' a seznamem úkolů
    todos = Todo.objects.filter(deleted=False).order_by('-created')
    return render(request, 'index.html', {'todos': todos})

def done(request, pk):
    """Označení úkolu jako splněného/nesplněného"""
    if request.method == 'POST':
        # Najdi úkol podle pk pomocí get_object_or_404
        # Přepni hodnotu done (True/False)
        # Pokud je done=True, nastav completed=aktuální čas
        # Pokud je done=False, nastav completed=None
        # Ulož změny pomocí save()
        todo = get_object_or_404(Todo, pk=pk)
        todo.done = not todo.done
        if todo.done:
            todo.completed = timezone.now()
        else:
            todo.completed = None
        todo.save()
    # Přesměruj na hlavní stránku
    return redirect('index')

def delete(request, pk):
    """Soft delete úkolu"""
    # Najdi úkol podle pk
    # Nastav deleted=True a deleted_at=aktuální čas
    # Ulož změny
    # Přesměruj na hlavní stránku
    todo = get_object_or_404(Todo, pk=pk)
    todo.deleted = not todo.deleted
    todo.deleted_at = timezone.now()
    todo.save()
    return redirect('index')

def edit(request, pk):
    """Editace existujícího úkolu"""
    # Najdi úkol podle pk
    todo = get_object_or_404(Todo, pk=pk)
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

def history(request):
    """Zobrazení historie splněných a smazaných úkolů"""
    # Načti splněné úkoly: done=True, deleted=False
    # Načti smazané úkoly: deleted=True
    # Vrať template 'history.html' s oběma seznamy
    splnene = Todo.objects.filter(done=True, deleted=False).order_by('-completed')
    smazane = Todo.objects.filter(deleted=True).order_by('-deleted_at')
    return render(request, 'history.html', {'splnene': splnene, 'smazane': smazane})