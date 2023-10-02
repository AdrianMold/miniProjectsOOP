class mini_calculator():

    def __init__(self, valoare_initiala = 0):  # initializam valoarea curenta cu 0
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

# cream un obiect de tip Calculator
calculator = Calculator()

