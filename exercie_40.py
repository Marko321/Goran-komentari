class Pesma(object):
    def __init__(self,tekst):
        self.tekst=tekst
        
    def stampa(self):
        for line in self.tekst:
            print line
            
pesma=Pesma(['Bum bum bum bum',
            'tra la la la',
            'bum bum bum bum',
            'tra la la la'])

pesma.stampa()