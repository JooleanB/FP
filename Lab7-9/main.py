from domain.entities import Person, Event
from domain.validators import Validator
from repository.person_repo import InMemoryRepository_person
from repository.event_repo import InMemoryRepository_Event
from repository.participare_repo import InMemoryRepository_participare
from Service.Servicii import Service
from UI.Console import Console

repo_participare = InMemoryRepository_participare()
repo_event = InMemoryRepository_Event()
repo_person = InMemoryRepository_person()
val = Validator()
srv = Service(repo_person,repo_event,repo_participare, val)
ui = Console(srv, Validator)
ui.ui()

