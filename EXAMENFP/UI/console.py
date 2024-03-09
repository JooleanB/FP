class Console:
    def __init__(self,srv):
        """
        initializarea consolei care va apela functii din service
        :param srv: obiect de tip service
        """
        self.__srv = srv

    def afisare_melodii(self):
        """
        functie pt afisarea melodiiilor
        :return:
        """
        lista = self.__srv.lista_melodii()
        for melodie in lista:
            print(melodie)

    def modifica(self):
        """
        functie care apeleaza srv pentru a modifica o anumita melodie cu ajutorul datelor de input
        :return:
        """
        try:
            titlu = input("Introduceti titlu ")
            artist = input("Introduceti artist ")
            gen = input("Introduceti gen ")
            data = input("Introduceti data ")
            self.__srv.modificare_melodie(titlu,artist,gen,data)
        except (ValueError,TypeError) as ve:
            print(ve)

    def random_melodii(self):
        """
        functie care apeleaza srv cu scopul de a genera un anumit numar de melodii random, cu artistii si titlul dati ca
        input in aceasta functie
        :return:
        """
        try:
            numar = int(input("Introduceti numarul: "))
            lista_titlu = input("Introduceti Titluri separate prin virgula: ")
            lista_artist = input("Introduceti artisti separati prin virgula: ")
            self.__srv.random(numar,lista_titlu,lista_artist)
            print("S-au adaugat ",numar," melodii")
        except (ValueError,TypeError,IndexError) as ve:
            print(ve)

    def export(self):
            nume_fisier = input("Nume fisier este: ")
            lista = self.__srv.lista_melodii()
            lista2 = self.__srv.merge_sort(lista)
            self.__srv.save_file(nume_fisier,lista2)


    def run(self):
        """
        functia care incepe programul
        :return:
        """
        while True:
            print("1. Afisare melodii \n2.Modifica melodie\n3.Melodii randon\n4.Export\n5.Iesire din program")
            comanda=input("Introduceti comanda dorita: ")
            if comanda == '1':
                self.afisare_melodii()
            elif comanda == '2':
                self.modifica()
            elif comanda =='3':
                self.random_melodii()
            elif comanda == '4':
                self.export()
            elif comanda =='5':
                break
            else:
                print("Ati Introdus o comanda gresita")