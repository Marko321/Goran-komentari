from . import TvojaKancelarija
from . import Cinkaros


class Generalni(TvojaKancelarija):
    def opis(self):

        if self._kol_besa > 5:
            self.ispis('Generalni: Verujem Vam kolega, ali dodjite JUCE na razgovor.')
        else:
            clan = raw_input('Generalni: Kolega Vi ste bese clan nase BIBLIOTEKE?')
            if clan == 'da' or clan == 'jesam':
                print('Generalni: Vec neko vreme razmisljam kako da iskoristim Vase potencijale')

                dalje = Cinkaros(self._kol_besa)
                dalje.opis()
            else:
                self.ispis('Generalni: Zao mi je, ali ne mogu Vam pomoci dok ne nabavite clansku kartu')