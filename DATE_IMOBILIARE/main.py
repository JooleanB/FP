from Repo.Repo_Imobile import InMemoryRepo_Imobile
from Servicii.Servicii import Servicii
from UI.Console import Console
from Testari.Teste import Testari


repo = InMemoryRepo_Imobile()
srv = Servicii(repo)
test =  Testari(srv)
ui = Console(srv, test)
ui.consola()
