class imenik(object):
    imen={}

    def dodaj(self,ime,broj):
        self.imen[ime]=broj

    def pretraga(self,ime):
        print('Broj telefona od osobe po imenu %s je %d' %(ime, self.imen[ime]))

    def brisanje(self,ime):
        del self.imen[ime]

    def ispis(self):
        print(self.imen)

marko=imenik()
nevena=imenik()

marko.dodaj('mare', 3333)
nevena.dodaj('nena', 222)
marko.pretraga('mare')
marko.ispis()
nevena.brisanje('nena')
marko.ispis()

novi={'dejan':1111,'petar':2222,'stojan':33533}

'''''Nije mi jasno kako da ubacim podatke iz dict-a novi u class-u imenik, petlja ispod ne radi
for ime in novi:
    ime=imenik()
    ime.dodaj('ime',novi[ime])

dejan.dodaj('deki',99999999)
dejan.ispis()