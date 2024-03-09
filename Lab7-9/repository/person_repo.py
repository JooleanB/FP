from domain.entities import Participare, Event, Person


class InMemoryRepository_person:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de persoane (i.e. sa ofere un depozit persistent pentru obiecte
        de tip persoana)
    """

    def __init__(self, citeste_din_fisier=True):
        self.__persoane = []
        if citeste_din_fisier:
            self.citire_fisier()

    def find_person(self, id):
        """
        Cauta persoana cu id dat
        :param id: id dat
        :type id: str
        :return: persoana cu id dat, None daca nu exista
        :rtype: Person
        """
        for person in self.__persoane:
            if person.get_id() == id:
                return person
        return None
    #

    # def binaryS(self, el, l, left, right):
    #     """
    #     Search an element in a list
    #     el - element to be searched; l - a list of ordered elements
    #     left,right the sublist in which we search
    #     return the position of first occurrence or the insert position
    #     """
    #     if left >= right - 1:
    #         return right
    #     m = (left + right) // 2
    #     if int(el) <= int(l[m].get_id_carte()):
    #         return self.binaryS(el, l, left, m)
    #     else:
    #         return self.binaryS(el, l, m, right)
    #
    #
    # def searchBinaryRec(self,el, l):
    #     """
    #     Search an element in a list
    #     el - element to be searched
    #     l - a list of ordered elements
    #     return the position of first occurrence or the insert position
    #     """
    #     if len(l) == 0:
    #         return 0
    #     if int(el) < int(l[0].get_id_carte()):
    #         return 0
    #     if int(el) >int (l[len(l) - 1].get_id_carte()):
    #         return len(l)
    #     return self.binaryS(el, l, 0, len(l))


    def __find_index(self, id):
        """
        Gaseste index-ul (pozitia) pe care este serialul cu id dat
        :param id: id dat
        :type id: str
        :return: pozitia in lista a serialului cu id dat, -1 daca serialul nu exista
        :rtype: int (>=0, <repo.size())
        """
        index = -1
        for i in range(self.size()):
            if self.__persoane[i].getId() == id:
                index = i
        return index

    def store_persoane(self, person):
        """
        Adauga o persoana in lista
        :param person: persoana care se adauga
        :type person: persoana
        :return: -; lista de persoane se modifica prin adaugarea persoanei date
        """
        if self.find_person(person.get_id()) is not None:
            raise ValueError('Exista deja o persoana cu acest id.')
        self.__persoane.append(person)
        self.save_file()
        # for i in self.__evenimente:
        #     self.__participari.append(Participare(person, i, 'NU'))

    def delete_person(self, id):
        """
        Sterge persoana dupa id
        :param id: id-ul dat
        :type id: str
        :return: persoana sters
        :rtype: Serial
        :raises: ValueError daca id-ul nu exista
        """

        person = self.find_person(id)
        if person is None:
            raise ValueError('Nu exista persoana cu acest id.')
        self.__persoane.remove(person)
        self.save_file()
        return person

    def get_all_persoane(self):
        """
        Returneaza o lista cu toate persoanele existente
        :rtype: list of objects de tip person
        """
        return self.__persoane

    def modifica_persoana(self, id, persoana_noua):
        persoana = self.find_person(id)
        if persoana is None:
            raise ValueError('Nu exista persoana cu acest id.')
        persoana.set_name(persoana_noua.get_name())
        persoana.set_address(persoana_noua.get_address())
        self.save_file()

    def citire_fisier(self):
        try:
            with open("Date_Persoane", 'r') as f_persoane:
                linie = f_persoane.readline().strip()
                while linie != "":
                    person_id = int(linie)
                    linie = f_persoane.readline().strip()
                    person_nume = linie
                    linie = f_persoane.readline().strip()
                    person_adresa = linie
                    persoana = Person(person_id, person_nume, person_adresa)
                    self.__persoane.append(persoana)
                    linie = f_persoane.readline().strip()
        except (ValueError, IndexError) as ve:
            print(str(ve))
        except FileNotFoundError:
            with open("Date_Persoane", 'x'):
                self.citire_fisier()

    def save_file(self):
        try:
            with open("Date_Persoane", 'w') as f_persoane:
                for persoana in self.__persoane:
                    f_persoane.write(f"{persoana.get_id()}\n{persoana.get_name()}\n{persoana.get_address()}\n")
        except ValueError:
            print("Eroare: Valoare invalida")
        except IndexError:
            print("Eroare: Tip de data invalid")
        except FileNotFoundError:
            print("Eroare: Fisierul nu a fost gasit")


#  Dictionar
#
# class InMemoryRepository:
#     """
#         Clasa creata cu responsabilitatea de a gestiona
#         multimea de persoane (i.e. sa ofere un depozit persistent pentru obiecte
#         de tip persoana)
#     """
#     def __init__(self):
#         self.__persoane = {}
#         self.__evenimente = {}
#
#     def find_person(self, id):
#         """
#         Cauta persoana cu id dat
#         :param id: id dat
#         :type id: str
#         :return: persoana cu id dat, None daca nu exista
#         :rtype: Person
#         """
#         for person in self.__persoane:
#             if person.get_id() == id:
#                 return person
#         return None
#
#     def find_eveniment(self, id):
#         """
#         Cauta evenimentul cu id dat
#         :param id: id dat
#         :type id: str
#         :return: evenimentul cu id dat, None daca nu exista
#         :rtype: eveniment
#         """
#         for eveniment in self.__evenimente:
#             if eveniment.get_id() == id:
#                 return eveniment
#         return None
#
#     def __find_index(self, id):
#         """
#         Gaseste index-ul (pozitia) pe care este serialul cu id dat
#         :param id: id dat
#         :type id: str
#         :return: pozitia in lista a serialului cu id dat, -1 daca serialul nu exista
#         :rtype: int (>=0, <repo.size())
#         """
#         index = -1
#         for i in range(self.size()):
#             if self.__persoane[i].getId() == id:
#                 index = i
#         return index
#
#     def store_persoane(self, person):
#         """
#         Adauga o persoana in lista
#         :param person: persoana care se adauga
#         :type person: persoana
#         :return: -; lista de persoane se modifica prin adaugarea persoanei date
#         """
#         if self.find_person(person.get_id()) is not None:
#             raise ValueError('Exista deja o persoana cu acest id.')
#         self.__persoane[person.get_id()] = person
#
#     def store_evenimente(self, eveniment):
#         """
#         Adauga un eveniment in lista
#         :param eveniment: eveniment care se adauga
#         :type eveniment: eveniment
#         :return: -; lista de evenimente se modifica prin adaugarea evenimentului dat
#         """
#         if self.find_eveniment(eveniment.get_id()) is not None:
#             raise ValueError('Exista deja eveniment cu acest id.')
#         self.__evenimente[eveniment.get_id()] = eveniment
#
#
#     def delete_person(self, id):
#         """
#         Sterge persoana dupa id
#         :param id: id-ul dat
#         :type id: str
#         :return: persoana sters
#         :rtype: Serial
#         :raises: ValueError daca id-ul nu exista
#         """
#
#         person = self.find_person(id)
#         if person is None:
#             raise ValueError('Nu exista persoana cu acest id.')
#
#         self.__persoane.remove(person)
#         return person
#
#
#     def delete_eveniment(self, id):
#         """
#         Sterge eveniment dupa id
#         :param id: id-ul dat
#         :type id: str
#         :return:evenimentul sters sters
#         :rtype: Serial
#         :raises: ValueError daca id-ul nu exista
#         """
#
#         eveniment = self.find_eveniment(id)
#         if eveniment is None:
#             raise ValueError('Nu exista eveniment cu acest id.')
#
#         self.__evenimente.remove(eveniment)
#         return eveniment
#
#     def get_all_persoane(self):
#         """
#         Returneaza o lista cu toate persoanele existente
#         :rtype: list of objects de tip person
#         """
#         return self.__persoane
#
#     def get_all_evenimente(self):
#         """
#         Returneaza o lista cu toate persoanele existente
#         :rtype: list of objects de tip person
#         """
# return self.__evenimente
