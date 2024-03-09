from Entities.Imobile import Imobile
class Servicii:
    def __init__(self, repo):
        self.__repo = repo

    def afisare_imobile(self):
        """
        functie ce afiseaza obiect cu obiect fiecare imobil din lista de imobile din repo
        :return:
        """
        lista_imobile = self.__repo.get_all_imobile()
        for un_imobil in lista_imobile:
            print(un_imobil)

    def media_pret(self):
        """
        functie ce calculeaza media de pret pentru vanzare
        :return:
        """
        lista_imobile = self.__repo.get_all_imobile()
        nr = 0
        suma = 0
        for un_imobil in lista_imobile:
            if un_imobil.get_tipoferta() == 'vanzare':
                suma =suma + int(un_imobil.get_pret())
                nr = nr+1
        if nr == 0:
            return False
        else:
            media_artimetica = suma / nr
            return media_artimetica

    def tranzactie(self,id,pret):
        """
        functie ce creaza o tranzactie si afiseaza adresa imobilului cu id-ul dat cat si comisionul calculat
        in functie de pretul dat
        :param id: id-ul imobilului pentru tranzactie
        :param pret:  pretul negociat
        :return:
        """
        imobil = self.__repo.find_imobile(id)
        if imobil:
            tipoferta = imobil.get_tipoferta()
            print('Adresa este: '+ imobil.get_adresa())
            if tipoferta == 'vanzare':
                comision = (2*pret)/100
            else:
                comision = (5*pret)/10
            print('Comisionul este: '+ str(comision))
        else:
            print('Nu exista un imobil cu acest id.')

