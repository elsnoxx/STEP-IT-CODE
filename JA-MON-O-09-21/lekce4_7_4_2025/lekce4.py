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






# Úkol 4: Dědičnost - Třída ElektrickeAuto
# Vytvoř třídu ElektrickeAuto, která dědí od třídy Auto. Přidej atribut kapacita_baterie a metodu nabij,
# která vypíše, že auto je nabíjeno, a zobrazí kapacitu baterie.





# Úkol 5: Polymorfismus - Třída Zvire
# Vytvoř abstraktní třídu Zvire s metodou zvuk. Poté vytvoř dvě třídy Pes a Kocka,
# které dědí od třídy Zvire a implementují metodu zvuk.





# Úkol 6: Hra - Evidence zvířat v zoo
# Vytvoř třídu Zvire, která má atributy jméno a druh. Přidej metodu info, která vypíše informace o zvířeti.
# Poté vytvoř třídu Zoo, která bude evidovat zvířata. Přidej metody pro přidání zvířete, zobrazení všech zvířat
# a hledání zvířete podle jména.

