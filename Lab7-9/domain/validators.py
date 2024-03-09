from domain.entities import Person,Event,Participare


class Validator:
    def validate_person(self, person:Person):
        errors = []
        nume = person.get_name().split(" ")
        adresa = person.get_address().split(" ")
        if len(nume) < 2:
            errors.append('Numele persoanei trebuie sa aiba atat nume cat si prenume.')
        for i in range(len(nume)):
            if len(nume[i]) < 3:
                errors.append('Numele si prenumele trebuie sa aiba cel putin 3 litere.')
                break
            if nume[i][0].islower():
                errors.append('Initialele trebuie sa fie majuscule')
                break
        if len(adresa) < 2:
            errors.append('Adresa trebuie sa contina cel putin strada si numarul.')
        elif len(adresa) > 2:
            errors.append('Numele strazii trebuie scris folosind "-" daca este format din mai mult de un cuvant.')
        else:
            if adresa[0][0].islower():
                errors.append('Numele strazii trebuie sa inceapa cu majuscula.')
            if not adresa[1].isnumeric():
                errors.append('Nu ati introdus numarul strazii.')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def validate_eveniment(self, eveniment:Event):
        errors = []
        data=eveniment.get_date().split('.')
        if 1>int(data[0])>31:
            errors.append('Ziua trebuie sa fie in intervalul [1,31]')
        if 1>int(data[1])<12:
            errors.append('Luna trebuie sa fie in intervalul [1,12]')
        if 1900>int(data[2])<2022:
            errors.append('Anul trebuie sa fie in intervalul [1900,2022]')
        timp=eveniment.get_time().split(':')
        if 0>int(timp[0])>23:
            errors.append('Ora trebuie sa fie in intervalul [0,23]')
        if 0>int(timp[1])>59:
            errors.append('Minutele trebuie sa fie in intervalul [0,59]')
        if len(eveniment.get_description().split())<1:
            errors.append('Descrierea trebuie sa aiba mai mult de 0 cuvinte')
        if len(errors) != 0:
            errors_str = '\n'.join(errors)
            raise ValueError(errors_str)

    def validate_participare(self, participare:Participare):
        errors = []
        if participare.get_participare() != 'NU' and participare.get_participare() != 'DA':
            errors.append('Nu ati introdus o participare valida')
        if len(errors)!=0:
            errors_str = '\n'.join(errors)
            raise ValueError(errors_str)