from types import NoneType
import random, string
from domain.entities import Person, Event, Participare
from domain.validators import Validator
from repository.person_repo import InMemoryRepository_person


class Service:
    """
        GRASP Controller (Curs 6)
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
        (i.e. declansare actiune: utilizator -> ui-> obiect tip service in ui -> service -> service coordoneaza operatiile
        folosind alte obiecte (e.g. repo, validator) pentru a realiza efectiv operatia)
        """

    def __init__(self, repo_person, repo_event, repo_participare, validator: Validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de evenimente sau persoane
        :type repo: InMemoryRepository
        :param validator: validator pentru verificarea persoanelor sau evenimentele
        :type validator: ShowValidator
        """
        self.__repo_person = repo_person
        self.__repo_event = repo_event
        self.__repo_participare = repo_participare
        self.__validators = validator

    def add_persoana(self, personID, nume, adresa):
        """
        Adauga o persoana la lista
        :param nume: numele persoanei pe care o adaugam
        :param adresa: adresa persoanei pe care o adaugam
        :return:
        """
        s = Person(personID, nume, adresa)
        self.__validators.validate_person(s)
        self.__repo_person.store_persoane(s)
        return s

    def add_eveniment(self, id, data, timp, descriere):
        """
        Adauga un eveniment la lista
        :param data: data evenimentului pe care il adaugam
        :param timp: ccand incepe evenimentul pe care il adaugam
        :param descriere: descrierea evenimentului pe care il adaugam
        :return:
        """
        s = Event(id, data, timp, descriere)
        self.__validators.validate_eveniment(s)
        self.__repo_event.store_evenimente(s)
        return s

    def get_all_persoane(self):
        """
        Returneaza o lista cu toate persoanele disponibile
        :return: lista de persoane disponibile
        :rtype: list of objects de tip Person
        """
        return self.__repo_person.get_all_persoane()

    def get_all_evenimente(self):
        """
        Returneaza o lista cu toate persoanele disponibile
        :return: lista de persoane disponibile
        :rtype: list of objects de tip Person
        """
        return self.__repo_event.get_all_evenimente()

    def delete_person(self, id):
        """
        Sterge persoana cu id dat din lista
        :param id: id-ul dat
        :type id: str
        :return: persoana stearsa
        :rtype: Person
        :raises: ValueError daca nu exista persoana cu id-ul dat
        """
        return self.__repo_person.delete_person(id)

    def delete_eveniment(self, id):
        """
        Sterge evenimentul cu id dat din lista
        :param id: id-ul dat
        :type id: str
        :return: evenimentul sters
        :rtype: Event
        :raises: ValueError daca nu exista eveniment cu id-ul dat
        """
        return self.__repo_event.delete_eveniment(id)

    def modifica_event(self, id, data, timp, descriere):
        eveniment = Event(id, data, timp, descriere)
        self.__validators.validate_eveniment(eveniment)
        return self.__repo_event.modifica_eveniment(id, eveniment)

    def modifica_persoana(self, id, nume, adresa):
        persoana = Person(id, nume, adresa)
        self.__validators.validate_person(persoana)
        return self.__repo_person.modifica_persoana(id, persoana)

    def modifica_participare(self, person_id, eveniment_id, participare):
        if self.__repo_person.find_person(person_id) is None:
            raise ValueError('Nu exista persoana cu acest id')
        elif self.__repo_event.find_eveniment(eveniment_id) is None:
            raise ValueError('Nu exista eveniment cu acest id')
        else:
            part = Participare(person_id, eveniment_id, participare)
            self.__validators.validate_participare(part)
            self.__repo_participare.adauga_participare(person_id, eveniment_id, participare)

    def find_person(self, persoana_id: int):
        pers = self.__repo_person.find_person(persoana_id)
        if type(pers) != NoneType:
            return self.__repo_person.find_person(persoana_id)
        else:
            raise ValueError('Nu exista persoana cu id-ul : {}'.format(persoana_id))

    def find_event(self, eveniment_id: int):
        event = self.__repo_event.find_eveniment(eveniment_id)
        if type(event) != NoneType:
            return self.__repo_event.find_eveniment(eveniment_id)
        else:
            raise ValueError('Nu exista eveniment cu id-ul : {}'.format(eveniment_id))

    def get_all_participari(self):
        return self.__repo_participare.get_all_participari()

    def bubble_sort_pentru_evenimente_pentru_persoana(self, person):
        lista_evenimente = []
        for participare in self.get_all_participari():
            if participare.get_person() == person.get_id() and participare.get_participare() == 'DA':
                lista_evenimente.append(self.find_event(participare.get_event()))
        #self.bubbleSort(lista_evenimente, lambda x: x.get_description(), lambda x: x.get_date(), True)
        self.bubbleSort(lista_evenimente, True)
        #self.shellSort(lista_evenimente, lambda x: x.get_description(), True)
        #self.shellSort(lista_evenimente, lambda x: x.get_date(), True)
        # self.bubbleSort(lista_evenimente, lambda x: x.get_date(), True)
        # lista_evenimente.sort()
        return lista_evenimente

    def shell_sort_pentru_evenimente_pentru_persoana(self, person):
        lista_evenimente = []
        for participare in self.get_all_participari():
            if participare.get_person() == person.get_id() and participare.get_participare() == 'DA':
                lista_evenimente.append(self.find_event(participare.get_event()))
        self.shellSort(lista_evenimente, False)
        return lista_evenimente

    def nr_participari_persoana(self, id_persoana, lista_participari):
        nr_participari = 0
        for participare in lista_participari:
            if participare.get_participare() == 'DA' and participare.get_person() == id_persoana:
                nr_participari += 1
        return nr_participari

    def lista_participari(self, id_persoana):
        lista_participari = self.__repo_participare.get_all_participari()
        return self.nr_participari(id_persoana, lista_participari, 0)

    def nr_participari(self, id_persoana, lista_participari, nr_participari):
        if lista_participari == []:
            return 0
        if lista_participari[len(lista_participari) - 1].get_participare() == 'DA' and lista_participari[
            len(lista_participari) - 1].get_person() == id_persoana:
            nr_participari += 1
        lista_participari.pop()
        if len(lista_participari) > 1:
            self.nr_participari(id_persoana, lista_participari, nr_participari)
        return nr_participari

    def persoane_participante_la_cele_mai_multe_eveniment(self):
        dictionar_persoane = {}
        for participare in self.get_all_participari():
            dictionar_persoane[participare.get_person()] = self.nr_participari_persoana(
                participare.get_person())
        dictionar_sortat = sorted(dictionar_persoane.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return dictionar_sortat

    def print_persoane_participante_la_cele_mai_multe_eveniment(self):
        dictionar_persoane = self.persoane_participante_la_cele_mai_multe_eveniment()
        for persoana in dictionar_persoane:
            print(f'persoana_id: {persoana[0]}, nr_participari: {persoana[1]}')

    def __nr_participari_eveniment(self, id_eveniment):
        nr_participari = 0
        lista_participari = self.get_all_participari()
        for participare in lista_participari:
            if participare.get_participare() == 'DA' and participare.get_event() == id_eveniment:
                nr_participari += 1
        return nr_participari

    def Primele_20_la_suta_evenimente(self):
        dictionar_evenimente = {}
        for participare in self.get_all_participari():
            dictionar_evenimente[
                self.find_event(participare.get_event()).get_description()] = self.__nr_participari_eveniment(
                participare.get_event())
        dictionar_sortat = sorted(dictionar_evenimente.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return dictionar_sortat

    def print_Primele_20_la_suta_evenimente(self):
        dictionar_evenimente = self.Primele_20_la_suta_evenimente()
        lungime_20_la_suta = int((len(dictionar_evenimente) * 2) / 10)
        for i in range(0, lungime_20_la_suta):
            print(f'descriere: {dictionar_evenimente[i][0]}, nr_participari: {dictionar_evenimente[i][1]}')

    def print_cel_mai_hype_eveniment(self):
        dictionar_evenimente = self.Primele_20_la_suta_evenimente()
        print(f'descriere: {dictionar_evenimente[0][0]}, nr_participari: {dictionar_evenimente[0][1]}')

    def random_Evenimente(self, nr_evenimente):
        lista_data = ['20.10.2000', '27.07.2003', '31.08.2003', '16.05.2018', '03.12.2022', '15.04.2008', '16.09.2015']
        lista_timp = ['20:00', '12:30', '15:30', '07:20', '18:00', '10:00', '13:30']
        litere = string.ascii_lowercase
        lungime_lista = len(self.get_all_evenimente())
        lungime_noua = lungime_lista + nr_evenimente
        while len(self.get_all_evenimente()) != lungime_noua:
            OK = 1
            id = random.choice(range(1, 1000))
            data = random.choice(lista_data)
            timp = random.choice(lista_timp)
            descriere = ''.join(random.choice(litere) for _ in range(10))
            evenimente = self.get_all_evenimente()
            for eveniment in evenimente:
                if eveniment.get_id() == id:
                    OK = 0
                    break
            if OK == 1:
                self.add_eveniment(id, data, timp, descriere)

    def random_Persoane(self, nr_persoane):
        lista_nume = ['Musatoiu Iulian', 'Buda Robert', 'Flinta Ovidiu', 'Olariu Florin', 'Apreutesei Rares',
                      'Mandoiu Vlad', 'Crihan Viviana', 'Caraveteanu William', 'Jigarea Andra', 'Ovreiu David']
        lista_adrese = ['Principala 481', '13-Decembrie 41', 'Cocorului 16', 'Vlahuta 21', 'Caragiale 52']

        lungime_lista = len(self.get_all_persoane())
        lungime_noua = lungime_lista + nr_persoane
        while len(self.get_all_persoane()) != lungime_noua:
            OK = 1
            id = random.choice(range(1, 1000))
            nume = random.choice(lista_nume)
            adresa = random.choice(lista_adrese)
            persoane = self.get_all_persoane()
            for person in persoane:
                if person.get_id() == id:
                    OK = 0
                    break
            if OK == 1:
                self.add_persoana(id, nume, adresa)

    def cmp (self,a,b):
        if a.get_description() < b.get_description():
            return True
        elif a.get_description() == b.get_description() and a.get_time() < b.get_time():
            return True
        elif a.get_description() == b.get_description() and a.get_time() == b.get_time() and a.get_time() < b.get_time():
            return True
        return False

    def bubbleSort(self, l, reverse=False):
        # , key=lambda x: x'
        sorted = False
        while not sorted:
            sorted = True  # assume the list is already sorted
        for i in range(len(l) - 1):
            if self.cmp(l[i + 1], l[i]):
                l[i], l[i + 1] = l[i + 1], l[i]
        sorted = False  # the list is not sorted yet
        if reverse == True:
            return l[::-1]
        return l

    # def bubbleSort_2_key(self, l, key1=lambda x: x, key2=lambda x: x, reverse=False):
    #     sorted = False
    #     while not sorted:
    #         sorted = True  # assume the list is already sorted
    #     for i in range(len(l) - 1):
    #         if key1(l[i + 1]) < key1(l[i]):
    #             l[i], l[i + 1] = l[i + 1], l[i]
    #         elif key1(l[i + 1]) == key1(l[i]) and key2(l[i+1])< key2(l[i]):
    #             l[i], l[i + 1] = l[i + 1], l[i]
    #     sorted = False  # the list is not sorted yet
    #     if reverse == True:
    #         return l[::-1]
    #     return l

    def shellSort(self, lista, key=lambda x: x, reverse=False):
        """
        Complexity in the Worst-Case Scenario: Less Than or Equal to O (n2)
        Complexity in the Best Case: O(n*Log n)
        Complexity in the Average Case: O(n*log n)
        :param lista:
        :param key:
        :param reverse:
        :return:
        """

        # Start with a big gap, then reduce the gap
        n = len(lista)
        gap = n // 2

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        while gap > 0:

            for i in range(gap, n):

                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = lista[i]

                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                #self.cmp(lista[j - gap], temp)
                while j >= gap and self.cmp(lista[j - gap], temp) is True:
                    lista[j] = lista[j - gap]
                    j -= gap

                # put temp (the original a[i]) in its correct location
                lista[j] = temp
            gap /= 2
            if reverse == True:
                return lista[::-1]
            return lista
