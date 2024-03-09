class Imobile:
    def __init__(self,id,adresa,pret,tipoferta):
        self.__id = id
        self.__adresa = adresa
        self.__pret = pret
        self.__tipoferta = tipoferta

    def __str__(self):
        """
        functie pentru afisarea de imobile
        :return:
        """
        return "{}, {}, {}, {}, {}".format(self.__id,type(self.__id),self.__adresa,self.__pret,self.__tipoferta)

    def get_id(self):
        """
        functie ce returneaza id-ul unui imobil
        :return:
        """
        return self.__id
    def get_adresa(self):
        """
        functie ce returneaza adresa unui imobil
        :return:
        """
        return self.__adresa
    def get_pret(self):
        """
        functie ce returneaza pretul unui imobil
        :return:
        """
        return self.__pret
    def get_tipoferta(self):
        """
        functie ce returneaza tipul de oferta al unui imobil
        :return:
        """
        return self.__tipoferta