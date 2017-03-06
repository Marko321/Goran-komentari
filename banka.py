class OtvoriRacun(object):
    
    def __init__(self,iznos):
        self.iznos=iznos

    def uplata(self,uplata):
        ukupno=uplata+self.iznos
        print(ukupno)
        
    def isplata(self,isplata):
        self.isplata=isplata
        
    def provera(self):
        print(self.iznos)

racun=OtvoriRacun(200)
racun.uplata(100)