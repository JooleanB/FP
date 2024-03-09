from Testari.Teste import Testari
class Console:
    def __init__(self, srv, test):
        self.__srv = srv
        self.__test =test

    def afisare_imobile(self):
        """
        functie ce apeleaza functie de afisare_imobile din servicii
        :return:
        """
        self.__srv.afisare_imobile()

    def media_aritmetica(self):
        """
        functie ce apeleaza functia de media_pret din servicii
        :return:
        """
        media_pret = self.__srv.media_pret()
        if not media_pret:
            print("Nu exista niciun imobil de vanzare")
        else:
            print("Media de pret pentru imobilele la vanzare este: " +str(media_pret))

    def tranzactie(self):
        """
        functie ce apeleaza functia de tranzactie din servicii
        :return:
        """
        try:
            id = input("Introduceti id-ul: ")
            pret_negociat = int(input("Introduceti pretul negociat: "))
            self.__srv.tranzactie(id, pret_negociat)
        except(ValueError,TypeError,AttributeError) as ve:
            print(ve)

    def returnare(self):
        x,y = self.__srv.returnare()
        print(x)
        print(y)

    def consola(self):
        self.__test.test_all()
        while True:
            print("Alegerile sunt: 1.afisare_imobile, 2.media_per_pret_vanzare, 3.efectuare_tranzactie")
            cmd = input("Introduceti comanda dorita: ")
            if cmd == '1':
                self.afisare_imobile()
            elif cmd == '2':
                self.media_aritmetica()
            elif cmd == '3':
                self.tranzactie()
            else:
                print("Ati introdus o comanda gresita!")
