class Melodii:
    def __init__(self, titlu, artist, gen, data):
        """
        Functia de initializare a obiectului melodie
        :param titlu: titlu-string
        :param artist: artist-string
        :param gen: gen-string
        :param data: data-string
        """
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__data = data


    def __str__(self):
        """
        functie pentru afizarea obiectului de tip melodie
        :return:
        """
        return f'{self.__titlu},{self.__artist},{self.__gen},{self.__data}'

    def __lt__(self, other):
        """
        functie creata pentru compararea obiectelor de tip melodie dupa data
        :param other: data cu care compar
        :return:
        """
        data1 = self.__data.split('.')
        data2 = other.get_data().split('.')
        if data1[2]<data2[2]:
            return True
        elif data1[2]==data2[2]:
            if data1[1] < data2[1]:
                return True
            elif data1[1]==data2[1]:
                if data1[0]<data2[0]:
                    return True
        return False

    def set_gen(self,gen_nou):
        """
        functie care seteaza genul unei melodii
        :param gen_nou: stringul cu care va fi inlocuit genul
        :return:
        """
        self.__gen = gen_nou

    def set_data(self,data_noua):
        """
        functie care seteaza data unei melodii
        :param data_noua: stringul cu care va fi inlocuita data
        :return:
        """
        self.__data = data_noua

    def get_titlu(self):
        """
        functie care returneaza titlul
        :return:
        """
        return self.__titlu

    def get_artist(self):
        """
        functie care returneaza artistul
        :return:
        """
        return self.__artist

    def get_gen(self):
        """
        functie care returneaza genul

        :return:
        """
        return self.__gen

    def get_data(self):
        """
        functie care returneaza data
        :return:
        """
        return self.__data

