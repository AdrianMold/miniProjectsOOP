class mini_calculator:

    def __init__(self, valoare_initiala=0):
        self.valoare_curenta = valoare_initiala

    def adunare(self, numar):
        self.valoare_curenta += numar

    def scadere(self, numar):
        self.valoare_curenta -= numar

    def inmultire(self, numar):
        self.valoare_curenta *= numar

    def impartire(self, numar):
        if numar != 0:
            self.valoare_curenta /= numar
        else:
            print('Nu se poate imparti la zero!')

    def setare(self, numar):
        self.valoare_curenta = numar


calculator = mini_calculator()  # cream un obiect de tip Calculator

# facem o bucla pentru a astepta comenzile userului
while True:
    print(f'Valoarea curenta este {calculator.valoare_curenta} ')
    comanda = input('> ').strip()  # citim comanda si o despartim in operator si numar

    if '+' in comanda:
        numar = float(comanda[1:])  # convertim numarul introdus intr-un float
        calculator.adunare(numar)
    elif '-' in comanda:
        numar = float(comanda[1:])
        calculator.scadere(numar)  # apelam fiecare metoda
    elif '*' in comanda:
        numar = float(comanda[1:])
        calculator.inmultire(numar)
    elif '/' in comanda:
        numar = float(comanda[1:])
        calculator.impartire(numar)
    elif '=' in comanda:
        numar = float(comanda[1:])
        calculator.setare(numar)
    elif comanda.lower() == 'x':
        print('Iesire din calculator!')
        break
    else:
        print('Comanda invalida!')

    comanda = input('> ')


