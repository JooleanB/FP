from Domain.Piesa_de_teatru import Piesa_de_teatru

class Validare:
    def validate_piesa(self,piesa:Piesa_de_teatru):
        lista_erori = []
        if piesa.get_titlu() == "":
            lista_erori.append("Titlul trebuie sa fie nevid")
        if piesa.get_regizor() == "":
            lista_erori.append("Regizorul trebuie sa fie nevid")
        lista_genuri = ["Drama","Comedie","Satira","Altele"]
        eroare_gen = True
        for gen in lista_genuri:
            if piesa.get_gen() == gen:
                eroare_gen = False
        if eroare_gen is True:
            lista_erori.append("Genul trebuie sa fie din lista de genuri specificata")
        if type(piesa.get_durata())!= int or piesa.get_durata()<0:
            lista_erori.append("Durata trebuie sa fie de tip int si un numar pozitiv")
        if len(lista_erori) > 0:
            lista_erori_string = '\n'.join(lista_erori)
            raise ValueError(lista_erori_string)

