class Ljudi(object):
    def __init__(self,ime,pol,godine,visina):
        self.ime=ime
        self.pol=pol
        self.godine=godine
        self.visina=visina
    def opis(self):
        print ('Kandidat se zove:%s, pol:%s i ima %d godina.' %(self.ime,self.pol,self.godine))


#Po PEP8 standardu ime klase pocinje velikim slovom
class Osobine(Ljudi):

    #Menjanjem redosleda funkcija opis menja se ispis Covek/Kandidat zbog nasledjivanja

    #Ovo se zove redeklaracija promenljivih i nije cest primer u praksi
    #Prva funkcija ovde je skroz overload-ovana drugom funkcijom tako da je nemoguce
    #da se ona ikad izvrsi
    #Python funkcije gleda po imenu i u jednoj klasi, nikad nebi trebalo da imas 2 funkcije koje se isto zovu
    #Sto se tice nasledjivanja to je ok, skroz, cak i preporucljivo, naslediti i predefinisati funkciju ako
    #ima potrebe za tim
    def opis(self):
        super(Osobine,self).opis()
                
    def opis(self):
        print ('Covek se zove:%s, pol:%s i ima %d godina.' %(self.ime,self.pol,self.godine))
    

    def sport(self):
        if self.visina<150:
            print('%s ima gradju fudbalera zbog visine od %d cm.' %(self.ime,self.visina))
        elif self.visina<180:
            print('%s ima gradju rukometasa zbog visine od %d cm.' %(self.ime,self.visina))
        else:
            print('%s ima gradju kosarkasa zbog visine od %d cm.' %(self.ime,self.visina))

ja=Osobine('Pera','muski',44,166)
ja.opis()
ja.sport()