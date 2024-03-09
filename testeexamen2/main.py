from UI.Console import Console
from Repo.Repo import Repo
from Service.Service import Service
from Validator.Validari import Validare
nume_fisier ="C:\\Users\\musat\\PycharmProjects\\testeexamen2\Domain\\Piese_de_teatru"
repo = Repo(nume_fisier)
validator = Validare()
srv = Service(repo,validator)
ui = Console(srv)
ui.run()

