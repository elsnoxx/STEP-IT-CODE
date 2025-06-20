# todo_app/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    # vazba na uzivatele, ktery ukol vytvoril
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # text => charField, maximalní délka 200 znaků, nazev "Úkol"
    text = models.CharField(max_length=200, verbose_name="Úkol")
    # poznamka => textField, volitelné (blank), nazev "Poznámka"
    poznamka = models.TextField(blank=True, verbose_name="Poznámka")
    # ocekavane => dateField, volitelné, nazev "Očekávaný" (null)
    ocekavane = models.DateField(null=True, blank=True, verbose_name="Očekávaný termín")
    # predmet => charField, maximalní délka 100 znaků, volitelné, nazev "Předmět"
    predmet = models.CharField(max_length=100, blank=True, verbose_name="Předmět")
    # done => booleanField, výchozí hodnota False (default), nazev "Splněno"
    done = models.BooleanField(default=False, verbose_name="Splněno")
    # created => dateTimeField, výchozí hodnota aktuální čas, nazev "Vytvořeno"
    created = models.DateTimeField(default=timezone.now, verbose_name="Vytvořeno")
    # completed => dateTimeField, volitelné, nazev "Dokončeno"
    completed = models.DateTimeField(null=True, blank=True, verbose_name="Dokončeno")
    # deleted => booleanField, výchozí hodnota False, nazev "Smazáno"
    deleted = models.BooleanField(default=False, verbose_name="Smazáno")
    # deleted_at => dat'eTimeField, volitelné, nazev "Smazáno v"
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Smazáno v")
    
    # Přidání metody pro zobrazení úkolu __str__
    def __str__(self):
        return self.text
    

# po aktualizaci
# 1. python manage.py makemigrations
# vybrat z menu 1
# 2. k >>> napsat 1 jako defaultni hodnotu prozatim
# 3. python manage.py migrate
# pokud se vam ztratil superuser tak porom spustit -> python manage.py createsuperuser