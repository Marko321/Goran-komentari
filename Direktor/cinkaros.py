from . import TvojaKancelarija


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
        dalje = Cinkaros(self._kol_besa)
        dalje.cvrge(broj)

    def cvrge(self, broj):
        self.broj = broj

        if self.broj == 0:
            self.ispis('Generalni: Dokazao si da smo bili u zabludi, ti si dobar covek')
        elif self.broj > 0 and self.broj < 10:
            if self.broj < 5:
                self.ispis('Generalni: Zasluzio je da ga zaboli glava.')
            else:
                self.ispis('Generalni: Mislim da preterujes.')
        else:
            self.ispis('Generalni: Dobra fora, bas si ga uplasio.')