class Testari:
    def __init__(self, srv):
        # self.__repo = repo
        self.__srv = srv

    def test_media(self):
        media = self.__srv.media_pret()
        assert (media == 750.0)

    def test_tranzactie(self):
        id = 1
        pret = 1000
        assert ()

    def test_all(self):
        self.test_media()
