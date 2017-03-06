

class TvojaKancelarija(object):

    def __init__(self, kol_besa):
        # Super da znas
        # Python nema prava pristupa atributima u klasi ali po pep8 standardu se podrazumeva da
        # ako promenljiva pocinje sa _ (underscore) to je privatna promenljiva
        self._kol_besa = kol_besa

    def ispis(self, recenica):
        self.recenica = recenica
        print self.recenica + ' Takav je zivot.'
        # Opet ista prica za exit, inace u web applikacijama exit() nesmes da imas :), oborices server
        # exit(0)

    def opis(self):
        print'Imali ste problem na poslu, osteceni ste novom preraspodelom posla.'
        odgovor = raw_input('Da li biste se obratili tehnickom ili generalnom direktoru?')
        if 'teh' in odgovor:
            from . import Tehnicki
            dalje = Tehnicki(self._kol_besa)
            dalje.opis()
        else:
            from . import Generalni
            dalje = Generalni(self._kol_besa)
            dalje.opis()