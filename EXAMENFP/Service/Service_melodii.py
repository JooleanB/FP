import random

from Domain.Melodii import Melodii


class Service_Melodii:
    """
    clasa ce aplica functionalitatile cu datele obtinute din ui pe lista de melodii din service
    """
    def __init__(self, repo, validator):
        """
        initializarea
        :param repo: parametrul prin care se face legatura dintre repo si service
        :param validator: parametrul prin care se face legatura dintre repo si validator
        """
        self.__repo = repo
        self.__validator = validator

    def lista_melodii(self):
        """
        functie ce apeleaza functia din repo si da return la lista de melodii
        :return:
        """
        return self.__repo.get_lista()

    def modificare_melodie(self, titlu, artist, gen, data):
        """
        functie ce creeaza o melodie cu datele primite din ui
        si apoi modifica melodia care are acelasi titlu si artist din lista de melodii
        cu noile date
        :param titlu: titlul melodiei
        :param artist: artistul melodiei
        :param gen: genul melodiei
        :param data: data melodiei
        :return:
        """
        melodie_noua = Melodii(titlu, artist, gen, data)
        self.__validator.validare_melodie(melodie_noua, self.lista_melodii())
        self.__repo.modifica_melodie(melodie_noua)

    def random(self, numar, titluri, artisti):
        """
        functie ce genereaza random melodii
        :param numar: numarul de melodii generate
        :param titluri: stringul de titluri caruia ii dau split si creez astfel o lista de titluri
        :param artisti: stringul de artisti caruia ii dau split si creez astfel o lista de artisti
        :return:
        """
        lista_titluri = titluri.split(',')
        lista_artisti = artisti.split(',')
        lista_gen = ['Rock', 'Pop', 'Jazz']
        lista_data = ['20.10.2000', '13.02.2003', '31.08.2003']
        for i in range(0, numar):
            titlu = random.choice(lista_titluri)
            artist = random.choice(lista_artisti)
            gen = random.choice(lista_gen)
            data = random.choice(lista_data)
            melodie = Melodii(titlu, artist, gen, data)
            self.__repo.adauga_melodie(melodie)

    def merge1(self,st,dr):
        """
        interclasare a 2 liste stanga si dreapta
        :param st:
        :param dr:
        :return:
        """
        i,j=0,0
        rez = []
        while i<len(st) and j<len(dr):
            if st[i]<dr[i]:
                rez.append(st[i])
                i+=1
            else:
                rez.append(dr[i])
                j+=1
        while i<len(st):
            rez.append(st[i])
            i += 1
        while j<len(dr):
            rez.append(dr[j])
            j += 1
        return rez

    def merge_sort(self,l):
        """
        algoritmul de merge_Sort
        :param l:
        :return:
        """
        if len(l)<=1:
            return l
        mid = len(l)//2
        st = self.merge_sort(l[:mid])
        dr = self.merge_sort(l[mid:])
        return self.merge1(st,dr)

    def save_file(self,nume_fisier,lista):
        """
        functia care scrie in fisierul cu numele dat lista data
        :param nume_fisier: numele fisierului primit din input-ul din consola
        :param lista: lista sortata cu merge_sort
        :return:
        """
        try:
            with open(nume_fisier, 'w') as f_melodii:
                for melodie in lista:
                    f_melodii.write(f'{melodie.get_titlu()},{melodie.get_artist()},{melodie.get_gen()},{melodie.get_data()}\n')
        except ValueError:
            print('Eroare Valoare invalida')
        except IndexError:
                print('Eroare Tip de data invalid')
        except FileNotFoundError:
                print('Eroare Fisierul nu a fost gasit')
