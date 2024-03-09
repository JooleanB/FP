from Domain.Piesa_de_teatru import Piesa_de_teatru


class Repo:
    def __init__(self,nume_fisier):
        self.__lista_piese_de_teatru = []
        self.__nume_fisier = nume_fisier
        self.citire_fisier()

    def adaugare_piesa(self,piesa):
        for piesa_din_lista in self.__lista_piese_de_teatru:
            if piesa_din_lista.get_regizor() == piesa.get_regizor() and piesa_din_lista.get_titlu() == piesa.get_titlu():
                raise ValueError
        self.__lista_piese_de_teatru.append(piesa)
        self.save()
    def get_all_piese(self):
        return self.__lista_piese_de_teatru

    def find_piesa(self,titlu,regizor):
        for piesa in self.__lista_piese_de_teatru:
            if piesa.get_regizor() == regizor and piesa.get_titlu() == titlu:
                return piesa
        raise ValueError("Nu exista piesa")

    def modifica_piesa(self,piesa):
        titlu = piesa.get_titlu()
        regizor = piesa.get_regizor()
        piesa_de_modificat = self.find_piesa(titlu,regizor)
        for o_piesa in self.__lista_piese_de_teatru:
            if o_piesa.get_titlu() == piesa_de_modificat.get_titlu() and o_piesa.get_regizor() == piesa_de_modificat.get_regizor():
                o_piesa.set_durata(piesa.get_durata())
                o_piesa.set_gen(piesa.get_gen())



    def citire_fisier(self):
        try:
            with open(self.__nume_fisier,'r') as f_piese_de_teatru:
                linie = f_piese_de_teatru.readline().strip()
                while linie != "":
                    lista_elementa = linie.split(',')
                    titlu = lista_elementa[0]
                    regizor = lista_elementa[1]
                    gen = lista_elementa[2]
                    durata = lista_elementa[3]
                    piesa_de_teatru = Piesa_de_teatru(titlu,regizor,gen,durata)
                    print(piesa_de_teatru)
                    self.adaugare_piesa(piesa_de_teatru)
                    linie = f_piese_de_teatru.readline().strip()
        except (ValueError,TypeError) as ve:
            print(ve)
        except FileNotFoundError:
            with open(self.__nume_fisier,'x'):
                self.citire_fisier()

    def save(self):
        try:
            with open(self.__nume_fisier,'w') as f_piese:
                for piesa in self.__lista_piese_de_teatru:
                    f_piese.write(f'{piesa.get_titlu()},{piesa.get_regizor()},{piesa.get_gen()},{piesa.get_durata()}\n')
        except (IndexError,ValueError,TypeError) as ve:
            print(ve)



