class mini_calculator:

    def __init__(self, valoare_initiala=0.0):
        self.valoare_curenta = valoare_initiala

    def adunare(self):
        self.valoare_curenta += numar  # adunam nr la valoarea curenta

    def scadere(self):
        self.valoare_curenta -= numar   # scadem nr la valoarea curenta

    def inmultire(self):
        self.valoare_curenta *= numar   # inmultim nr la valoarea curenta

    def impartire(self):
        if numar != 0:
            self.valoare_curenta /= numar  # impartim valoarea curenta la numarul dat
        else:
            print('Nu se poate imparti la zero!')

    def setare(self, numar):
        self.valoare_curenta = numar  # setam valoarea curenta cu numarul dat

# Cream un obiect de tip Calculator
calculator = mini_calculator()

# facem o bucla pentru a astepta comenzile utilizatorului
while True:
    print(f'Valoarea curenta este {calculator.valoare_curenta} ')
    comanda = input('> ').strip()  # citim comanda si o despartim in operator si numar
    #comanda2 = comanda.split()
    if '+' in comanda:
        numar = float(comanda[1:])
        calculator.adunare(numar)     # apelam fiecare metoda
    elif '-' in comanda:
        numar = float(comanda[1:])
        calculator.scadere(numar)
    elif '*' in comanda:
        numar = float(comanda[1:])
        calculator.inmultire(numar)
    elif '/' in comanda:
        numar = float(comanda[1:])
        calculator.impartire(numar)
    elif '=' in comanda:
        numar = float(comanda[1:])
        calculator.setare(numar)
    elif comanda.lower() == 'x': # transforma intregul text in litere mici si verifica daca comanda de utilizator introdusa este litera x
        print('Iesire din calculator!')
        break
    else:
        print('Comanda invalida!')

