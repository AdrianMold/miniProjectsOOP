from GradiniteMiniProiect.ClaseGradinite.GradinitaPublica import GradinitaPublica
from GradiniteMiniProiect.ClaseGradinite.PrintColorString import PrintColorString

class GradinitaPublica25(GradinitaPublica):

    def activitate_practica(self):
        print('Copiii se joaca in curte pe balansoar')

        '''In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de la tastatura numarul de buline rosii pe care 
        le-a primit fiecare elev in parte, procesati-le si calculati media aritmetica a numarului de buline rosii. 
        Daca aceasta este mai mare decat cinci, printati pe ecran: “Elevii acestei gradinite sunt foarte neastamparati”.'''

    def calcul_buline(self):
        suma_buline = 0
        nr_copii = int(input('Introduceti numarul de copii'))
        for copil in range(1, nr_copii + 1):  # for each; pentru fiecare copil executa comanda de mai jos
            nr_buline = int(input(f'Introduceti numarul de buline rosii pentru copilul {copil}'))
            suma_buline += nr_buline
        media_aritmetica_buline = suma_buline / nr_copii
        print(f'Media bulinelor este: {media_aritmetica_buline}')
        if media_aritmetica_buline > 5:
            print(f'{PrintColorString.YELLOW} Elevii acestei gradinite sunt foarte neastamparati {PrintColorString.RESET}')
                #Am apelat clasa de colorat, la inceput punem rosu , si la final dam reset , altfel va ramane mereu rosu

        '''In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de la tastatura un dictionar care sa contina o serie
         de perechi cheie:valoare si dictionare imbricate (embedded, nested) care sa contina urmatoarele informatii: numele elevului, 
         numele parintilor, varsta elevului, activitatea preferata. Printati pentru fiecare elev toate informatiile de mai sus.'''

    '''{ 1: { 'nume' : 'Matei', 'nume_parinti' : 'Ion si Maria', 'varsta_elev' : 9, 'activitate_preferata' : 'colorat' }}
    
              
              
              
    ,
    2: { nume : Roxana,
              nume_parinti : Ionel si Maria,
              varsta_elev : 10,
              activitate_preferata : pictat
    }
    }'''

    def introduceti_informatii_elevi(self):
        info = eval(input('Introduceti datele despre elev: \n'))  # eval - preia input-uri si interpreteaza codul, ca si cum ar fi un cod real
        for elev_cheie, detalii_value in info.items():
            print(f'Elevul numarul {elev_cheie}')
            for date_cheie, date_value in detalii_value.items():
                print(f'{date_cheie} : {date_value}')























