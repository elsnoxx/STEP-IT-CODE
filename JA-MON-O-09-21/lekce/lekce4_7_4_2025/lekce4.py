# Úkol 1: Třída Pes
# Vytvoř třídu Pes, která má atributy jméno a barva. Přidej metodu info, která vypíše informace o psovi.
class Pes:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.age = 0

    def info(self):
        print(f"Pes se jmenuje {self.name}, ma barvu {self.color} a ma {self.age} let")

    def birthday(self):
        self.age += 1
        print(f"Pes {self.name} ma dneska {self.age} let")

# pesRex = Pes("Rex", "Brown")
# print(pesRex.name)
# pesMax = Pes("Max", "Black")
# print(pesMax.name)

pesRex = Pes("Rex", "Brown")
pesMax = Pes("Max", "Black")
pesRex.info()
pesMax.info()

pesMax.birthday()
pesRex.info()
pesMax.info()

# seznam = [Pes("Rex", "Brown"), Pes("Max", "Black")]
seznam = []
seznam.append(Pes("Rex", "Brown"))
seznam.append(Pes("Max", "Black"))
print(seznam)
for dog in seznam:
    dog.birthday()
    dog.info()

# Úkol 2: Třída Osoba se zapouzdřením
# Vytvoř třídu Osoba, která má atributy jméno a věk. Věk nastav jako soukromý atribut.
# Přidej metody pro změnu věku (zmen_vek) a získání věku (get_vek).

class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.__vek = vek
    
    def zmen_vek(self, novy_vek):
        self.__vek = novy_vek
    
    def info(self):
        print(f"Osoba se jmenem {self.jmeno} ma {self.__vek} let")
    
person = Osoba("Adam", 18)
person.info()
person.zmen_vek(26)
person.info()


# Úkol 3: Třída Auto
# Vytvoř třídu Auto, která má atributy značka a barva. Přidej metodu info, která vypíše informace o autě.
class Auto:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print(f"Auto znacky {self.name}, Barvy {self.color}")


auto1 = Auto("Škoda", "modrá")
auto2 = Auto("Tesla", "červená")
auto1.info()
auto2.info()


# Úkol 4: Dědičnost - Třída ElektrickeAuto
# Vytvoř třídu ElektrickeAuto, která dědí od třídy Auto. Přidej atribut kapacita_baterie a metodu nabij,
# která vypíše, že auto je nabíjeno, a zobrazí kapacitu baterie.
class ElektrickeAuto(Auto):
    def __init__(self, name, color, kapacita_baterie):
        super().__init__(name, color)
        self.kapacita_baterie = kapacita_baterie 
    
    def nabito(self):
        print(f"Auto je nyni nabito na {self.kapacita_baterie} Kwh")
    
    def nabij(self):
        self.kapacita_baterie += 5

elAuto = ElektrickeAuto("Tesla", "bila", 5)
elAuto.info()
elAuto.nabito()
elAuto.nabij()
elAuto.nabito()

# Úkol 5: Polymorfismus - Třída Zvire
# Vytvoř abstraktní třídu Zvire s metodou zvuk. Poté vytvoř dvě třídy Pes a Kocka,
# které dědí od třídy Zvire a implementují metodu zvuk.
class Zvire:
    def __init__(self, name):
        self.name = name
    
    def zvuk(self):
        return f"Zvire se jmenem {self.name}"

class Pes(Zvire):
    def __init__(self, name):
        super().__init__(name)

    def zvuk(self):
        return "Haf Haf"

class Kocka(Zvire):
    def __init__(self, name):
        super().__init__(name)

    def zvuk(self):
        return "Mnau Mnau"

pes = Pes("Rex")
kocka = Kocka("Mica")
print(f"Zvuk psa: {pes.zvuk()}")
print(f"Zvuk kočky: {kocka.zvuk()}")


# Úkol 6: Hra - Evidence zvířat v zoo
# Vytvoř třídu Zvire, která má atributy jméno a druh. Přidej metodu info, která vypíše informace o zvířeti.
# Poté vytvoř třídu Zoo, která bude evidovat zvířata. Přidej metody pro přidání zvířete, zobrazení všech zvířat
# a hledání zvířete podle jména.

class Zvire:
    def __init__(self, name, druh):
        self.name = name
        self.druh = druh
    
    def info(self):
        return f"Zvire: {self.name}, Druh {self.druh}"
    
class Zoo:
    def __init__(self):
        self.zvirata = []

    def pridej_zvire(self, zvire):
        self.zvirata.append(zvire)
        print(f"Zvire {zvire.name} bylo pridano do zoo")

    def zobraz_zvirata(self):
        if not self.zvirata:
            print("Zoo je prazdne")
        else:
            print("Seznam zvirat: ")
            for zvire in self.zvirata:
                print(f"Zvire: {zvire.info()}")

    def najdi_zvire(self, name):
        for zvire in self.zvirata:
            if zvire.name == name:
                print(f"Nalezeno: {zvire.info()}")
                return
        print(f"Zvire se jmenem {name} se nenachazi v Zoo.")

zoo = Zoo()

zoo.pridej_zvire(Zvire("Lev", "Selma"))
zoo.pridej_zvire(Zvire("Slon", "Bylozravec"))
zoo.pridej_zvire(Zvire("Papousek", "Ptak"))


zoo.zobraz_zvirata()

zoo.najdi_zvire("Lev")
zoo.najdi_zvire("Zebra")