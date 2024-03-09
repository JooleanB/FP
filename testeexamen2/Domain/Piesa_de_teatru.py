class Piesa_de_teatru:
    def __init__(self,titlu,regizor,gen,durata):
        self.__titlu = titlu
        self.__regizor = regizor
        self.__gen = gen
        self.__durata = durata

    def __str__(self):
        return f"{self.__titlu},{self.__regizor},{self.__gen},{self.__durata}"

    def get_titlu(self):
        return self.__titlu
    def get_regizor(self):
        return self.__regizor
    def get_gen(self):
        return self.__gen
    def get_durata(self):
        return self.__durata

    def set_durata(self,durata_noua):
        self.__durata = durata_noua

    def set_gen(self,gen_nou):
        self.__gen = gen_nou