from domain.entities import Person, Event
import unittest


class Testari(unittest.TestCase):

    def test_persona(self):
        persoana = Person(1,'Musatoiu Iulian', 'Principala 481')
        self.assertEqual(type(persoana),Person)

    def test_get_id_persoana(self):
        persoana = Person(1, 'Musatoiu Iulian', 'Principala 481')
        self.assertEqual(persoana.get_id(),1)

    def test_get_nume(self):
        persoana = Person(1, 'Musatoiu Iulian', 'Principala 481')
        self.assertEqual(persoana.get_name(),'Musatoiu Iulian')

    def test_set_nume(self):
        persoana = Person(1, 'Musatoiu Iulian', 'Principala 481')
        persoana.set_name('Mandoiu Vlad')
        self.assertEqual(persoana.get_name(),'Mandoiu Vlad')

    def test_get_adresa(self):
        persoana = Person(1, 'Musatoiu Iulian', 'Principala 481')
        self.assertEqual(persoana.get_address(),'Principala 481')

    def test_set_adresa(self):
        persoana = Person(1, 'Musatoiu Iulian', 'Principala 481')
        persoana.set_address('Cocorului 12')
        self.assertEqual(persoana.get_address(),'Cocorului 12')

    def test_eveniment(self):
        eveniment = Event(1,'12.10.2000','20:00','xyz')
        self.assertEqual(type(eveniment),Event)

    def test_get_id_eveniment(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        self.assertEqual(eveniment.get_id(),1)

    def test_get_data(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        self.assertEqual(eveniment.get_date(),'12.10.2000')

    def test_set_date(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        eveniment.set_date('10.09.2000')
        self.assertEqual(eveniment.get_date(),'10.09.2000')

    def test_get_time(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        self.assertEqual(eveniment.get_time(),'20:00')

    def test_set_time(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        eveniment.set_time('10:00')
        self.assertEqual(eveniment.get_time(),'10:00')

    def test_get_description(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        self.assertEqual(eveniment.get_description(),'xyz')

    def test_set_description(self):
        eveniment = Event(1, '12.10.2000', '20:00', 'xyz')
        eveniment.set_description('abc')
        self.assertEqual(eveniment.get_description(),'abc')