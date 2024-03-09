from domain.entities import Participare, Event, Person
class InMemoryRepository_participare:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de persoane (i.e. sa ofere un depozit persistent pentru obiecte
        de tip persoana)
    """

    def __init__(self):
        self.__participari = []

    def adauga_participare(self,person_id,eveniment_id,participare):
        PART = Participare(person_id, eveniment_id, participare)
        self.__participari.append(PART)


    def get_all_participari(self):
        return self.__participari


