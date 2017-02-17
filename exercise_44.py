class Ljudi(object):
    def __init__(self,ime,pol,godine,visina):
        self.ime=ime
        self.pol=pol
        self.godine=godine
        self.visina=visina
    def opis(self):
        print ('Kandidat se zove:%s, pol:%s i ima %d godina.' %(self.ime,self.pol,self.godine))



class osobine(Ljudi):
    
    def opis(self):
        super(osobine,self).opis()
                
    def opis(self):
        print ('Covek se zove:%s, pol:%s i ima %d godina.' %(self.ime,self.pol,self.godine))
    

    def sport(self):
        if self.visina<150:
            print('%s ima gradju fudbalera zbog visine od %d cm.' %(self.ime,self.visina))
        elif self.visina<180:
            print('%s ima gradju rukometasa zbog visine od %d cm.' %(self.ime,self.visina))
        else:
            print('%s ima gradju kosarkasa zbog visine od %d cm.' %(self.ime,self.visina))

ja=osobine('Pera','muski',44,166)                  
ja.opis()
ja.sport()