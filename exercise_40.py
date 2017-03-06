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


str = "Bum bum bum bum\ntra la la la\nbum bum bum bum\n"

class NaprednaPesma(object):

    def __init__(self, tekst):
        self.textString = tekst

    def stampa(self):
        #ovakav string se moze dobiti i ucitavanjem iz fajla
        # , ovo je nacin da se stampaju i razdvoje linije generatorom
        for line in str.splitlines():
            print line


pesma = NaprednaPesma(tekst=str)
pesma.stampa()