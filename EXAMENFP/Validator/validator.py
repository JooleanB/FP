class Validator:
    def validare_melodie(self, melodie,lista_melodii):
        """
        functie care valideaza datele unei melodii pe care vreau sa o adaug listei din repo
        :param melodie: melodia pe care o verific
        :param lista_melodii: lista din repo pentru a putea sa verific daca exista vreo melodie cu titlul si artistul
         parametrului melodie
        :return:
        """
        lista_gen = ['Rock', 'Pop', 'Jazz']
        lista_erori = []
        nr=0
        for melodie_lista in lista_melodii:
            if melodie.get_artist() == melodie_lista.get_artist() and melodie.get_titlu() == melodie_lista.get_titlu():
                nr = nr -1
            nr = nr+1
        if nr == len(lista_melodii):
            lista_erori.append("Nu exisra nicio melodie cu titlul si artistul dat")
        if melodie.get_gen() != lista_gen[0]:
            if melodie.get_gen() != lista_gen[1]:
                if melodie.get_gen() != lista_gen[2]:
                    lista_erori.append('Genul nu este bun')
        data = melodie.get_data().split('.')
        if 0>int(data[2])>2023:
            lista_erori.append("Data gresita")
        elif 1>int(data[1])>12:
            lista_erori.append("Data gresita")
        elif int(data[1]==2):
            if 1>int(data[0])>28:
                lista_erori.append("Data gresita")
        elif int(data[1])==1 or int(data[1])==3 or int(data[1])==5 or int(data[1])==7 or int(data[1])==8 or int(data[1])==10 or int(data[1])==12:
            if 1>int(data[0])>31:
                lista_erori.append("Data gresita")
        else:
            if 1 > int(data[0]) > 30:
                lista_erori.append("Data gresita")

        if len(lista_erori) > 0:
            lista_erori_string = '\n'.join(lista_erori)
            raise ValueError(lista_erori_string)