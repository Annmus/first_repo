class Audi:
    def __init__(self, kolor, kondycja, vin):
        self.kolor = kolor
        self.kondycja = kondycja
        self.przebieg = 20
        self.__vin = vin

    def aktualizuj_przebieg(self, o_ile):
        self.przebieg += o_ile

    def pokaz_vin(self):
        print(self.__vin)

moje_auto = Audi('czerwony', 'dobra', 123654)

print(moje_auto.kolor)
moje_auto.kolor = 'niebieski'
print(moje_auto.kolor)

moje_auto.aktualizuj_przebieg(40)
print(moje_auto.przebieg)

moje_auto.pokaz_vin()
