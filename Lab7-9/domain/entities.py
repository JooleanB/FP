import datetime


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__date = datetime.date(year, month, day)

    def __str__(self) -> str:
        return "{}.{}.{}".format(self.__date.day, self.__date.month, self.__date.year)

    def get_date(self) -> datetime.date:
        return self.__date

    def __lt__(self, other):
        return self.__date < other.get_date()


class Time:
    def __init__(self, hour: int, minutes: int):
        self.__hour = hour
        self.__min = minutes

    def __str__(self) -> str:
        return "{}:{}".format(self.__hour, self.__min)

    def get_hour(self) -> int:
        return self.__hour

    def get_min(self) -> int:
        return self.__min

    def __lt__(self,timp_nou):
        if self.__hour < timp_nou.get_hour():
            return True


class Event:
    def __init__(self, eveniment_id: int, date: Date, time: Time, description: str):
        self.__ID = eveniment_id
        self.__date = date
        self.__time = time
        self.__description = description

    def __str__(self):
        return "{}, {}, {}, {}".format(self.__ID, self.__date, self.__time, self.__description)

    def __lt__(self, other):
        if self.__description < other.get_description():
            return True
        elif self.__description > other.get_description():
            return False
        if self.__date < other.get_date():
            return True
        else:
            return False

    def get_id(self):
        return self.__ID

    def set_date(self, date: Date):
        self.__date = date

    def get_date(self) -> Date:
        return self.__date

    def set_time(self, time: Time):
        self.__time = time

    def get_time(self) -> Time:
        return self.__time

    def set_description(self, description: str):
        self.__description = description

    def get_description(self) -> str:
        return self.__description

    def __eq__(self, eveniment_nou):
        if self.__ID == eveniment_nou.get_id():
            return True
        return False


class PersonName:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    def __str__(self) -> str:
        return "{} {}".format(self.__first_name, self.__last_name)

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name


class PersonAddress:
    def __init__(self, street: str, number: int):
        self.__street = street.title()
        self.__number = number

    def __str__(self) -> str:
        return "Str. {} Nr. {}".format(self.__street, self.__number)

    def get_street(self) -> str:
        return self.__street

    def get_number(self) -> int:
        return self.__number


class Person:
    def __init__(self, person_id: int, name: PersonName, address: PersonAddress):
        self.__id = person_id
        self.__name = name
        self.__address = address

    def __str__(self):
        return "{}, {}, {}".format(self.__id, self.__name, self.__address)

    def get_id(self):
        return self.__id

    def set_name(self, name: PersonName):
        self.__name = name

    def get_name(self) -> PersonName:
        return self.__name

    def set_address(self, address: PersonAddress):
        self.__address = address

    def get_address(self) -> PersonAddress:
        return self.__address

    def __eq__(self, persoana_noua):
        if self.__id == persoana_noua.get_id():
            return True
        return False


class Participare:
    def __init__(self, person_id, event_id, participare: str):
        self.__person = person_id
        self.__event = event_id
        self.__participare = participare

    def __eq__(self, other):
        if self.get_event() == other.get_event():
            return True
        return False

    def get_person(self):
        return self.__person

    def get_event(self):
        return self.__event

    def get_participare(self):
        return self.__participare

    def set_person(self, persoana_noua):
        self.__person = persoana_noua

    def set_event(self, eveniment_nou):
        self.__event = eveniment_nou

    def set_participare(self, participare_noua):
        self.__participare = participare_noua

    def __str__(self):
        return "person_id: {},event_id: {}: participare: {}".format(self.__person, self.__event,
                                                                    self.__participare)
