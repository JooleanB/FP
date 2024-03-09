from Service.Servicii import Service
from domain.entities import Person, Event, Participare
from domain.validators import Validator
from repository.participare_repo import InMemoryRepository_participare
from repository.event_repo import InMemoryRepository_Event
from repository.person_repo import InMemoryRepository_person
import unittest


class Testari(unittest.TestCase):

    def test_add_persoana(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        added_person = test_srv.add_persoana(5, 'Musatoiu Iulian', 'Principala 481')
        self.assertEqual(added_person.get_name(), 'Musatoiu Iulian')
        self.assertEqual(added_person.get_id(), 5)
        self.assertEqual(added_person.get_address(), 'Principala 481')
        self.assertEqual(len(repo_p.get_all_persoane()), 1)
        self.assertRaises(ValueError, test_srv.add_persoana, 5, 'Musatoiu', 'Strada Principala Nr 481')

    def test_delete_persoana(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        test_srv.delete_person(4)
        self.assertEqual(len(repo_p.get_all_persoane()), 3)
        #self.assertRaises(ValueError, test_srv.delete_person, 8) DECI E BLACK BOX !

    def test_add_eveniment(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        added_eveniment = test_srv.add_eveniment(5, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        self.assertEqual(added_eveniment.get_date(), '12.07.2000')
        self.assertEqual(added_eveniment.get_id(), 5)
        self.assertEqual(added_eveniment.get_time(), '20:00')
        self.assertEqual(added_eveniment.get_description(), 'Cel mai tare concert din bacau ma jur')
        self.assertEqual(len(repo_e.get_all_evenimente()), 1)
        self.assertRaises(ValueError, test_srv.add_eveniment, 5, '31.-2.2007', '20:00', 'Cel')

    def test_delete_eveniment(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(1, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(2, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(3, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.delete_eveniment(3)
        self.assertEqual(len(repo_e.get_all_evenimente()), 2)
        self.assertRaises(ValueError, test_srv.delete_eveniment, 6)

    def test_modifica_persoana(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        test_srv.modifica_persoana(1, 'Crihan Viviana', 'Principala 69')
        lista_persoane = test_srv.get_all_persoane()
        persoana = Person(1, 'Crihan Viviana', 'Principala 69')
        self.assertEqual(lista_persoane[0], persoana)

    def test_modifica_eveniment(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(1, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(2, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(3, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.modifica_event(1, '15.12.2003', '20:00', 'Cel mai panarama baiat')
        eveniment = Event(1, '15.12.2003', '20:00', 'Cel mai panarama baiat')
        lista_evenimente = test_srv.get_all_evenimente()
        self.assertEqual(lista_evenimente[0], eveniment)

    def test_generare_random_persoane(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.random_Persoane(10)
        self.assertEqual(len(repo_p.get_all_persoane()), 10)

    def test_generare_random_evenimente(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.random_Evenimente(10)
        self.assertEqual(len(repo_e.get_all_evenimente()), 10)

    def test_find_person(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        persoana = Person(1, 'Musatoiu Iulian', 'Principala 481')
        self.assertEqual(test_srv.find_person(1), persoana)
        self.assertRaises(ValueError, test_srv.find_person, 6)

    def test_find_eveniment(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(1, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(2, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(3, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.modifica_event(1, '15.12.2003', '20:00', 'Cel mai panarama baiat')
        eveniment = Event(3, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        self.assertEqual(test_srv.find_event(3), eveniment)
        self.assertRaises(ValueError, test_srv.find_event, 4)

    def test_adauga_participare(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare()
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(1, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(2, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(3, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        test_srv.modifica_participare(1, 2, 'DA')
        participare = Participare(1, 2, 'DA')
        self.assertEqual(len(repo_part.get_all_participari()), 1)
        self.assertEqual(repo_part.get_all_participari()[0], participare)
        self.assertRaises(ValueError, test_srv.modifica_participare, 4, 5, 'da')

    def test_lista_sortata(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare()
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(3, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(1, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(2, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        persoana = test_srv.find_person(1)
        eveniment1 = test_srv.find_event(1)
        eveniment2 = test_srv.find_event(2)
        eveniment3 = test_srv.find_event(3)
        test_srv.modifica_participare(1, 1, 'DA')
        test_srv.modifica_participare(1, 2, 'DA')
        test_srv.modifica_participare(1, 3, 'DA')
        lista_evenimente = test_srv.sortare_evenimente_pentru_persoana(persoana)
        self.assertEqual(lista_evenimente[0].get_id(), eveniment1.get_id())
        self.assertEqual(lista_evenimente[1].get_id(), eveniment3.get_id())
        self.assertEqual(lista_evenimente[2].get_id(), eveniment2.get_id())

    def test_persoane_participante(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare()
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(3, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(1, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(2, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        test_srv.modifica_participare(4, 1, 'DA')
        test_srv.modifica_participare(2, 2, 'DA')
        test_srv.modifica_participare(4, 3, 'DA')
        test_srv.modifica_participare(4, 2, 'DA')
        test_srv.modifica_participare(3, 3, 'DA')
        test_srv.modifica_participare(3, 2, 'DA')
        test_srv.modifica_participare(2, 3, 'DA')
        test_srv.modifica_participare(1, 2, 'DA')
        lista = test_srv.persoane_participante_la_cele_mai_multe_eveniment()
        self.assertEqual(lista[0], (4, 3))
        self.assertEqual(lista[1], (3, 2))
        self.assertEqual(lista[2], (2, 2))
        self.assertEqual(lista[3], (1, 1))

    def test_20_la_suta(self):
        repo_p = InMemoryRepository_person(False)
        repo_e = InMemoryRepository_Event(False)
        repo_part = InMemoryRepository_participare()
        validator = Validator()
        test_srv = Service(repo_p, repo_e, repo_part, validator)
        test_srv.add_eveniment(3, '12.07.2000', '20:00', 'Cel mai tare concert din bacau ma jur')
        test_srv.add_eveniment(1, '27.07.2003', '10:00', 'Cei 4 corifei tandreturi pentru femei')
        test_srv.add_eveniment(2, '31.08.2003', '14:00', 'RHCP ONG NIGHTWISH FR TE OMOR')
        test_srv.add_persoana(1, 'Musatoiu Iulian', 'Principala 481')
        test_srv.add_persoana(2, 'Olariu Florin', 'Cocorului 16')
        test_srv.add_persoana(3, 'Buda Robert', 'Decembrie 13')
        test_srv.add_persoana(4, 'Flinta Ovidiu', 'Dealul-Melcilor 69')
        test_srv.modifica_participare(4, 1, 'DA')
        test_srv.modifica_participare(2, 2, 'DA')
        test_srv.modifica_participare(4, 3, 'DA')
        test_srv.modifica_participare(4, 2, 'DA')
        test_srv.modifica_participare(3, 3, 'DA')
        test_srv.modifica_participare(3, 2, 'DA')
        test_srv.modifica_participare(2, 3, 'DA')
        test_srv.modifica_participare(1, 2, 'DA')
        lista = test_srv.Primele_20_la_suta_evenimente()
        self.assertEqual(lista[0],('RHCP ONG NIGHTWISH FR TE OMOR', 4))

