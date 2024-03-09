from domain.entities import Participare, Event, Person


class InMemoryRepository_Event:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de persoane (i.e. sa ofere un depozit persistent pentru obiecte
        de tip persoana)
    """
    def __init__(self, citire_din_fisier=True):
        self.__evenimente = []
        if citire_din_fisier:
            self.citire_fisier()

    def find_eveniment(self, ID:int):
        """
        Cauta evenimentul cu id dat
        :param ID: id dat
        :type ID: str
        :return: evenimentul cu id dat, None daca nu exista
        :rtype: eveniment
        """
        for eveniment in self.__evenimente:
            if eveniment.get_id() == ID:
                return eveniment
        return None


    def store_evenimente(self, eveniment):
        """
        Adauga un eveniment in lista
        :param eveniment: eveniment care se adauga
        :type eveniment: eveniment
        :return: -; lista de evenimente se modifica prin adaugarea evenimentului dat
        """
        if self.find_eveniment(eveniment.get_id()) is not None:
            raise ValueError('Exista deja eveniment cu acest id.')
        self.__evenimente.append(eveniment)
        self.save_file()


    def delete_eveniment(self, id):
        """
        Sterge eveniment dupa id
        :param id: id-ul dat
        :type id: str
        :return:evenimentul sters sters
        :rtype: Serial
        :raises: ValueError daca id-ul nu exista
        """

        eveniment = self.find_eveniment(id)
        if eveniment is None:
            raise ValueError('Nu exista eveniment cu acest id.')
        self.__evenimente.remove(eveniment)
        self.save_file()
        return eveniment


    def get_all_evenimente(self):
        """
        Returneaza o lista cu toate persoanele existente
        :rtype: list of objects de tip person
        """
        return self.__evenimente

    def modifica_eveniment(self, id, eveniment_nou):
        eveniment = self.find_eveniment(id)
        if eveniment is None:
            raise ValueError('Nu exista eveniment cu acest id.')
        eveniment.set_date(eveniment_nou.get_date())
        eveniment.set_time(eveniment_nou.get_time())
        eveniment.set_description(eveniment_nou.get_description())
        self.save_file()
        return eveniment

    def citire_fisier(self):
        try:
            with open("Date_Eveniment", 'r') as f_event:
                linie = f_event.readline().strip()
                while linie != "":
                    linie = linie.split(',')
                    event_id = int(linie[0])
                    event_data = linie[1]
                    event_timp = linie[2]
                    event_descriere = linie[3]
                    event = Event(event_id,event_data,event_timp,event_descriere)
                    self.__evenimente.append(event)
                    linie = f_event.readline().strip()
        except (ValueError, IndexError) as ve:
            print(str(ve))
        except FileNotFoundError:
            with open("Date_Eveniment", 'x'):
                self.citire_fisier()

    def save_file(self):
        try:
            with open("Date_Eveniment", 'w') as f_evenimente:
                for eveniment in self.__evenimente:
                    f_evenimente.write(f"{eveniment.get_id()},{eveniment.get_date()},{eveniment.get_time()},{eveniment.get_description()}\n")
        except ValueError:
            print("Eroare: Valoare invalida")
        except IndexError:
            print("Eroare: Tip de data invalid")
        except FileNotFoundError:
            print("Eroare: Fisierul nu a fost gasit")

