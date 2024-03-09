from Entities.Imobile import Imobile
class InMemoryRepo_Imobile:
    def __init__(self):
        self.__imobile = []
        self.citire_fisier()

    def adauga_imobil(self, imobil):
        """
        adauga imobile la lista de imobile din repo
        :param imobil: imobilul care se adauga la lista de imobile
        :return:
        """
        self.__imobile.append(imobil)

    def citire_fisier(self):
        """
        Functia de citire din fisier, care adauga fiecare imobil citit in lista de imobile din repo
        :return:
        """
        try:
            with open("Repo/Date_Imobile", 'r') as f_imobile:
                line = f_imobile.readline().strip()
                while line!="":
                    linie = line.split(',')
                    id = linie[0]
                    adresa = linie[1]
                    pret = linie[2]
                    tipoferta = linie[3]
                    imobil = Imobile(id, adresa, pret, tipoferta)
                    self.adauga_imobil(imobil)
                    line = f_imobile.readline().strip()
        except(ValueError,TypeError,AttributeError) as ve:
            print(str(ve))
        except FileNotFoundError:
            with open("Repo/Date_Imobile", 'x') as f_imobile:
                self.citire_fisier()

    def find_imobile(self,id):
        """
        functie care gaseste un imobil dupa id
        :param id: id-ul imobilului cautat
        :return:
        """
        for imobil in self.__imobile:
            if imobil.get_id() == id:
                return imobil
        return False

    def get_all_imobile(self):
        """
        functie ce returneaza intreaga lista de imobile
        :return:
        """
        return self.__imobile