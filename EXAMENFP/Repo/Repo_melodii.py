from Domain.Melodii import Melodii


class Repo_Melodii:
    """
    clasa care se ocupa cu listele de melodii
    """
    def __init__(self,nume_fisier):
        """
        functia de initializare a obiectului de tip repo
        :param nume_fisier:
        """
        self.__nume_fisier = nume_fisier
        self.__lista_melodii = []
        self.citire_fisier()

    def get_lista(self):
        """
        functie ce returneaza lista de melodii
        :return:
        """
        return self.__lista_melodii

    def modifica_melodie(self,melodie_noua):
        """
        functie ce inlocuieste in lista o melodie cu acelasi titlu si artist cu parametrul melodie_noua
        :param melodie_noua: parametru de tip Melodii
        :return:
        """
        for melodie in self.__lista_melodii:
            if melodie.get_titlu() == melodie_noua.get_titlu() and melodie.get_artist() == melodie_noua.get_artist():
                melodie.set_gen(melodie_noua.get_gen())
                melodie.set_data(melodie_noua.get_data())
                break
        self.save_file()

    def adauga_melodie(self,melodie_noua):
        """
        functie ce adauga o melodie la lista de melodii
        :param melodie_noua: melodia pe care o adaug
        :return:
        """
        self.__lista_melodii.append(melodie_noua)
        self.save_file()



    def citire_fisier(self):
        """
        functie care citeste din fisier
        :return:
        """
        try:
            with open(self.__nume_fisier, 'r') as f_melodii:
                linie = f_melodii.readline().strip()
                while linie != "":
                    lista_elemente = linie.split(',')
                    titlu = lista_elemente[0]
                    artist = lista_elemente[1]
                    gen = lista_elemente[2]
                    data = lista_elemente[3]
                    tractor = Melodii(titlu,artist,gen, data)
                    self.__lista_melodii.append(tractor)
                    linie = f_melodii.readline().strip()
        except (ValueError, IndexError) as ve:
            print(str(ve))
        except FileNotFoundError:
            with open(self.__nume_fisier, 'x'):
                self.citire_fisier()

    def save_file(self):
        """
        functie care scrie in fisier
        :return:
        """
        try:
            with open(self.__nume_fisier, 'w') as f_melodii:
                for melodie in self.__lista_melodii:
                    f_melodii.write(f'{melodie.get_titlu()},{melodie.get_artist()},{melodie.get_gen()},{melodie.get_data()}\n')
        except ValueError:
            print('Eroare Valoare invalida')
        except IndexError:
                print('Eroare Tip de data invalid')
        except FileNotFoundError:
                print('Eroare Fisieruln u a fost gasit')
