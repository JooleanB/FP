from Repo.Repo_melodii import Repo_Melodii
from Service.Service_melodii import Service_Melodii
from UI.console import Console
from Validator.validator import Validator


nume_fisier = "C:\\Users\\musat\\PycharmProjects\\EXAMENFP\\Domain\\Text_Melodii"
validator = Validator()
repo = Repo_Melodii(nume_fisier)
srv = Service_Melodii(repo,validator)
ui = Console(srv)

ui.run()