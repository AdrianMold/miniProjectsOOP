from GradiniteMiniProiect.ClaseGradinite.GradinitaPrivata import GradinitaPrivata
from GradiniteMiniProiect.ClaseGradinite.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinite.GradinitaPublica25 import GradinitaPublica25

if __name__ == '__main__':
    gradinita_privata1 = GradinitaPrivata()
    gradinita_privata1.activitate_practica()
    gradinita_privata1.ora_de_somn()

    gradinita_publica1 = GradinitaPublica()
    gradinita_publica1.activitate_practica()
    gradinita_publica1.ora_de_somn()

    gradinita_publica_25 = GradinitaPublica25()
    gradinita_publica_25.activitate_practica()

    # object pt a testa culoarea bulinelor
    gradinita_publica_25.calcul_buline()

    # apelare metpda introduceti informatii elevi pe objectul gradinitapublica25
    gradinita_publica_25.introduceti_informatii_elevi()




















































