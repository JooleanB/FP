from domain.entities import Person, Event, Participare
from domain.validators import Validator
import random
import string


class Console:
    def __init__(self, srv, Validator):
        """
        Initializeaza consola
        :type srv: ShowService
        """
        self.__srv = srv
        self.__Validator = Validator

    def __print_all_eveniment(self):
        """
         Afiseaza toate evenimentele disponibile

         """
        evenimente_list = self.__srv.get_all_evenimente()
        if len(evenimente_list) == 0:
            print('Nu exista evenimente in lista.')
        else:
            print('Lista de evenimente este:')
            for eveniment in evenimente_list:
                print('ID:', eveniment.get_id(), 'Data: ', eveniment.get_date(), ' - Timp: ', eveniment.get_time(),
                      '  Descriere: ', eveniment.get_description())

    # DICTIONAR #for person in persoane_list:
    # print(persoane_list[person])
    def __print_all_persoane(self):
        """
        Afiseaza toate persoanele disponibile

        """
        persoane_list = self.__srv.get_all_persoane()
        if len(persoane_list) == 0:
            print('Nu exista persoane in lista.')
        else:
            print('Lista de persoane este:')
            for person in persoane_list:
                print(person)
            # for person in persoane_list:
            #     print(persoane_list[person])

    def __add_Persoana(self):
        """
        Adauga o persoana cu datele citite de la tastatura
        """
        try:
            id = int(input("ID: "))
        except (ValueError, TypeError) as ve:
            print(str(ve))
        Nume = input("Numele: ")
        adresa = input("Adresa: ")
        try:
            persoana = self.__srv.add_persoana(id, Nume, adresa)
            #self.__Validator.validate_person(self, persoana)
            print('Persoana a fost adaugata cu succes')
        except ValueError as ve:
            print(str(ve))

    def __add_Eveniment(self):
        """
        Adauga un eveniment cu datele citite de la tastatura
        """
        try:
            ID = int(input("ID: "))
        except (ValueError, TypeError) as ve:
            print(str(ve))
        data = input("data: ")
        timp = input("timp: ")
        descriere = input("descriere: ")
        try:
            eveniment = self.__srv.add_eveniment(ID, data, timp, descriere)
            self.__Validator.validate_eveniment(self, eveniment)
            print('Evenimentul a fost adaugat cu succes')
        except ValueError as ve:
            print(str(ve))

    def __delete_Persoana(self):
        """
        Sterge o persoana din lista dupa un id introdus de la tastatura
        """

        try:
            id = int(input('Identificatorul persoanei de sters:'))
            deleted_person = self.__srv.delete_person(id)
            print('Persoana ' + deleted_person.get_name() + ' a fost stearsa cu succes')
        except ValueError as ve:
            print(str(ve))

    def __delete_Eveniment(self):
        """
        Sterge un eveniment din lista dupa un id introdus de la tastatura
        """
        try:
            id = int(input('Identificatorul evenimentului de sters:'))
            self.__srv.delete_eveniment(id)
            print('Evenimentul a fost sters cu succes')
        except ValueError as ve:
            print(str(ve))

    def __modifica_Eveniment(self):
        print("Introduceti id-ul evenimentului pe care doriti sa il modificati")
        id = input('ID: ')
        print("Introduceti noile date ale evenimentului")
        data = input("data: ")
        timp = input("timp: ")
        descriere = input("descriere: ")
        try:
            self.__srv.modifica_event(id, data, timp, descriere)
            print('Evenimentul a fost modificat cu succes')
        except ValueError as ve:
            print(str(ve))

    def __modifica_Persoana(self):
        print("Introduceti id-ul persoanei pe care doriti sa o modificati")
        id = input('ID: ')
        print("Introduceti noile date ale persoanei")
        nume = input("nume: ")
        adresa = input("adresa: ")
        try:
            self.__srv.modifica_persoana(id, nume, adresa)
            print('Persoana a fost modificata cu succes')
        except ValueError as ve:
            print(str(ve))

    def __random_Persoane(self):
        try:
            cate_persoane = int(input('Introduceti numarul de persoane '))
            self.__srv.random_Persoane(cate_persoane)
        except TypeError as ve:
            print(str(ve))

    def __random_Evenimente(self):
        try:
            numar_evenimente = int(input('Introduceti numarul de evenimente de generat '))
            self.__srv.random_Evenimente(numar_evenimente)
        except(TypeError,ValueError) as ve:
            print(str(ve))

    def __adauga_participare(self):
        try:
            id_person = int(input('Introduceti id-ul persoanei: '))
            id_eveniment = int(input('Introduceti id-ul evenimentului: '))
            self.__srv.modifica_participare(id_person, id_eveniment, 'DA')
        except (TypeError, ValueError) as ve:
            print(str(ve))

    def __afisare_participari(self):
        participari = self.__srv.get_all_participari()
        if len(participari) == 0:
            print("Nu exista participari. ")
        else:
            for participare in participari:
                try:
                    if self.__srv.find_person(participare.get_person()) is not None and self.__srv.find_event(
                            participare.get_event()) is not None:
                        print(participare)
                except ValueError as ve:
                    pass

    def __sortare_evenimente_pentru_persoana(self):
        try:
            id_person = int(input('Introduceti id-ul persoanei: '))
            person = self.__srv.find_person(id_person)
            mod = input('Alegeti dintre bubble sort si shell sort: ')
            if mod == 'bubble sort':
                lista_evenimente = self.__srv.bubble_sort_pentru_evenimente_pentru_persoana(person)
            elif mod == 'shell sort':
                lista_evenimente = self.__srv.shell_sort_pentru_evenimente_pentru_persoana(person)
            else:
                print('ati introdus un mod gresit de sortare.')
            for eveniment in lista_evenimente:
                print(eveniment)
        except ValueError as ve:
            print(str(ve))

    def __persoane_participante_la_cele_mai_multe_eveniment(self):
        self.__srv.print_persoane_participante_la_cele_mai_multe_eveniment()

    def __primele_20_la_suta_evenimente(self):
        self.__srv.print_Primele_20_la_suta_evenimente()

    def __find_person(self):
        try:
            id = int(input('Introduceti id-ul persoanei cautate '))
            print(self.__srv.find_person(id))
        except (ValueError, TypeError) as ve:
            print(str(ve))

    def __find_eveniment(self):
        try:
            id = int(input('Introduceti id-ul evenimentului cautat '))
            print(self.__srv.find_event(id))
        except (ValueError, TypeError) as ve:
            print(str(ve))

    def __cel_mai_hype_eveniment(self):
        self.__srv.print_cel_mai_hype_eveniment()

    def __nr_participari(self):
        try:
            id = int(input('Introduceti id : '))
        except ValueError as ve:
            print(ve)
        print(self.__srv.lista_participari(id))


    def ui(self):
            print('Comenzi disponibile:\n 1.adauga persoana \n 2.afisare persoane\n 3.adauga eveniment\n'
                  ' 4.afisare evenimente\n 5.sterge persoana\n 6.sterge eveniment\n 7.modifica persoana\n'
                  ' 8.modifica eveiment\n 9.lista random de persoane\n 10.adauga participare\n 11.afisare participari\n'
                  ' 12.lista de evenimente la care participa o persoana sortata dupa descriere si data\n'
                  ' 13.Persoane participante la cele mai multe evenimente\n 14.lista random de evenimente \n'
                  ' 15.Sortare eveniment \n 16.gaseste persoana dupa id\n 17.gaseste eveniment dupa id\n'
                  ' 18.cel mai hype eveniment')
            cmd = input('Comanda este:')
            if cmd == '1':
                self.__add_Persoana()
            elif cmd == '2':
                self.__print_all_persoane()
            elif cmd == '3':
                self.__add_Eveniment()
            elif cmd == '4':
                self.__print_all_eveniment()
            elif cmd == '5':
                self.__delete_Persoana()
            elif cmd == '6':
                self.__delete_Eveniment()
            elif cmd == '7':
                self.__modifica_Persoana()
            elif cmd == '8':
                self.__modifica_Eveniment()
            elif cmd == '9':
                self.__random_Persoane()
            elif cmd == '10':
                self.__adauga_participare()
            elif cmd == '11':
                self.__afisare_participari()
            elif cmd == '12':
                self.__sortare_evenimente_pentru_persoana()
            elif cmd == '13':
                self.__persoane_participante_la_cele_mai_multe_eveniment()
            elif cmd == '14':
                self.__random_Evenimente()
            elif cmd == '15':
                self.__primele_20_la_suta_evenimente()
            elif cmd == '16':
                self.__find_person()
            elif cmd == '17':
                self.__find_eveniment()
            elif cmd == '18':
                self.__cel_mai_hype_eveniment()
            elif cmd == '19':
                self.__nr_participari()
            elif cmd =='x':
                return
            else:
                print('Comanda invalida.')
            self.ui()
