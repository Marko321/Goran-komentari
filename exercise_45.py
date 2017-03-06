class TvojaKancelarija(object):
    
    def __init__(self,kol_besa):
        #Super da znas
        #Python nema prava pristupa atributima u klasi ali po pep8 standardu se podrazumeva da
        #ako promenljiva pocinje sa _ (underscore) to je privatna promenljiva
        self._kol_besa=kol_besa
    
    def ispis(self,recenica):
        self.recenica=recenica
        print self.recenica + ' Takav je zivot.'
        #Opet ista prica za exit, inace u web applikacijama exit() nesmes da imas :), oborices server
        #exit(0)
        
    def opis(self):
        print'Imali ste problem na poslu, osteceni ste novom preraspodelom posla.'
        odgovor=raw_input('Da li biste se obratili tehnickom ili generalnom direktoru?')
        if 'teh' in odgovor:
            dalje=Tehnicki(self._kol_besa)
            dalje.opis()
        else:
            dalje=Generalni(self._kol_besa)
            dalje.opis()


class Cinkaros(TvojaKancelarija):
    
    def opis(self):
        
        print'Generalni: Ovo ti je kolega koji ti je radio iza ledja.'
        print'Generalni: Mozes ga kazniti cvrgama.'
        while True:
            try:
                broj = int(raw_input('Generalni: Koliko ces mu cvrga lupiti?'))
                break
            except ValueError:
                print('Generalni: To nije broj')
        dalje=Cinkaros(self.kol_besa)
        dalje.cvrge(broj)
        
    def cvrge(self,broj):
        self.broj=broj

        if self.broj == 0:
            self.ispis('Generalni: Dokazao si da smo bili u zabludi, ti si dobar covek')
        elif self.broj>0 and self.broj<10:
            if self.broj<5:
                self.ispis('Generalni: Zasluzio je da ga zaboli glava.')
            else:
                self.ispis('Generalni: Mislim da preterujes.')
        else:
            self.ispis('Generalni: Dobra fora, bas si ga uplasio.')
            
    
class Generalni(TvojaKancelarija):
    
    def opis(self):
        
        if self.kol_besa>5:
            self.ispis('Generalni: Verujem Vam kolega, ali dodjite JUCE na razgovor.')
        else:
            clan = raw_input('Generalni: Kolega Vi ste bese clan nase BIBLIOTEKE?')
            if clan == 'da' or clan== 'jesam':
                print('Generalni: Vec neko vreme razmisljam kako da iskoristim Vase potencijale')
                dalje=Cinkaros(self.kol_besa)
                dalje.opis()
            else:
                self.ispis('Generalni: Zao mi je, ali ne mogu Vam pomoci dok ne nabavite clansku kartu')
             
class Tehnicki(TvojaKancelarija):
    
    def opis(self):
        print'Tehnicki: Kolega cujem da ste nezadovoljni novom preraspodelom radnih mesta?'
        print'Tehnicki: Kazite sta Vas muci?'
    
        if self.kol_besa>5:
            self.ispis('Tehnicki: Smirite se i sledeci put povedite racuna o svom ponasanju.')
        else:
            print'Tehnicki: Mozete popricati sa generalnim, sve ovo je njegova zamisao.'
            dalje=Generalni(self.kol_besa)
            dalje.opis()
            
ja=TvojaKancelarija(4)
ja.opis()

#Generalno savet, jednu klasu u jedan fajl stavljaj, i probaj da import-ujes klase kao module
#Ja cu sad napraviti Direktor modul.