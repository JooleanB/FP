import unittest
from Repo.Repo_melodii import Repo_Melodii
from Service.Service_melodii import Service_Melodii
from UI.console import Console
from Validator.validator import Validator

nume_fisier_test = "C:\\Users\\musat\\PycharmProjects\\EXAMENFP\\Teste\\Text_Test"
repo_teste = Repo_Melodii(nume_fisier_test)
validator_teste = Validator()
srv_teste = Service_Melodii(repo_teste,validator_teste)
class Test_melodie(unittest.TestCase):
    """
    clasa care testeaza functiile din service
    """
    def test_random(self):
        """
        functie care testeaza daca se genereaza random numarul de melodii
        :return:
        """
        srv_teste.random(2,"Adrian cox,kendama","Adrian cox,kendama")
        self.assertEqual(len(repo_teste.get_lista()),3)
        self.assertRaises(TypeError,srv_teste.random,'f',"Adrian cox,kendama","Adrian cox,kendama")

    def test_modifica(self):
        """
        functie care teseteaza functia de modificare din service
        :return:
        """
        srv_teste.modificare_melodie('Time','Pink Floyd','Jazz','20.10.2003')
        self.assertEqual(repo_teste.get_lista()[0].get_titlu(),'Time')
        self.assertEqual(repo_teste.get_lista()[0].get_artist(), 'Pink Floyd')
        self.assertRaises(ValueError, srv_teste.modificare_melodie,'b','a','jaz','31.02.2003')


