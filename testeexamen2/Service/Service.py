import random
import string

from Domain.Piesa_de_teatru import Piesa_de_teatru


class Service:
    def __init__(self,repo,validator):
        self.__repo = repo
        self.__validator = validator

    def toate_piesele(self):
        print(len(self.__repo.get_all_piese()))
        return self.__repo.get_all_piese()

    def modifica_piesa(self,titlu,regizor,gen,durata):
        piesa = Piesa_de_teatru(titlu,regizor,gen,durata)
        self.__validator.validate_piesa(piesa)
        self.__repo.modifica_piesa(piesa)

    def adauga_piesa(self,titlu,regizor,gen,durata):
            piesa = Piesa_de_teatru(titlu,regizor,gen,durata)
            self.__validator.validate_piesa(piesa)
            self.__repo.adaugare_piesa(piesa)

    def generare_random(self,numar_de_generari):
        for i in range(0,numar_de_generari):
            lungime = random.randint(8,11)
            lungime_cuv = lungime//2
            lista_vocale =['a','e','i','o','u']
            lista_consoane = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
            cuv = ''
            for j in range (0,lungime_cuv):
                if j%2==0:
                    c = random.choice(lista_vocale)
                    cuv = cuv + c
                else:
                    c = random.choice(lista_consoane)
                    cuv = cuv + c
            titlu = cuv + ' '
            cuv2 = ''
            for k in range (0,lungime_cuv):
                if k%2==0:
                    c = random.choice(lista_vocale)
                    cuv2 = cuv2 + c
                else:
                    c = random.choice(lista_consoane)
                    cuv2 = cuv2 + c
            titlu = titlu +cuv2
            regizor1 = ''
            for a in range (0,lungime_cuv):
                if a%2==0:
                    c = random.choice(lista_vocale)
                    regizor1 = regizor1 + c
                else:
                    c = random.choice(lista_consoane)
                    regizor1 = regizor1 + c
            regizor = regizor1 + ' '
            regizor2 = ''
            for b in range (0,lungime_cuv):
                if b%2==0:
                    c = random.choice(lista_vocale)
                    regizor2 = regizor2 + c
                else:
                    c = random.choice(lista_consoane)
                    regizor2 = regizor2 + c
            regizor = regizor + regizor2

            lista_gen = ["Drama","Satira","Comedie","Altele"]
            gen = random.choice(lista_gen)

            durata = random.randint(0,1000)

            piesa = Piesa_de_teatru(titlu,regizor,gen,durata)
            self.__repo.adaugare_piesa(piesa)

