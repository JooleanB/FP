class Console:
    def __init__(self, srv):
        self.__srv = srv

    def adaugare_piesa(self):
        try:
            titlu = input("Introduceti titlu: ")
            regizor = input("Introduceti regizor: ")
            gen = input("Introduceti gen: ")
            durata = int(input("Introduceti durata: "))
            self.__srv.adauga_piesa(titlu,regizor,gen,durata)
        except (ValueError,TypeError) as ve:
            print(ve)

    def afisare(self):
        lista_piese = self.__srv.toate_piesele()
        for piesa in lista_piese:
            print(piesa)
    def modificarre(self):
        try:
            titlu = input("Introduceti titlu: ")
            regizor = input("Introduceti regizor: ")
            gen = input("Introduceti gen: ")
            durata = int(input("Introduceti durata: "))
            self.__srv.modifica_piesa(titlu,regizor,gen,durata)
        except (ValueError,TypeError) as ve:
            print(ve)

    def generare_random_piese(self):
        try:
            numar = int(input("Introduceti numar: "))
            self.__srv.generare_random(numar)
        except (ValueError,TypeError) as ve:
            print(ve)

    def run(self):
        while True:
            print("1.Adaugare piesa")
            print("2.Afisare piese")
            print("3.Modificare piesa")
            print("4.Generare random piese")
            cmd = input("Introduceti comanda dorita: ")
            if cmd == '1':
                self.adaugare_piesa()
            if cmd =='2':
                self.afisare()
            if cmd == '3':
                self.modificarre()
            if cmd == '4':
                self.generare_random_piese()