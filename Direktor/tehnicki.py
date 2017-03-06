from . import TvojaKancelarija
from . import Generalni


class Tehnicki(TvojaKancelarija):

    def opis(self):
        print'Tehnicki: Kolega cujem da ste nezadovoljni novom preraspodelom radnih mesta?'
        print'Tehnicki: Kazite sta Vas muci?'

        if self._kol_besa > 5:
            self.ispis('Tehnicki: Smirite se i sledeci put povedite racuna o svom ponasanju.')
        else:
            print'Tehnicki: Mozete popricati sa generalnim, sve ovo je njegova zamisao.'
            #Import-ujemo ovde kada imamo situaciju da mozemo da izazovemo cirkularni import.
            # kada klasa A import-uje klasu B a klasa B import-uje klasu A
            dalje = Generalni(self._kol_besa)
            dalje.opis()