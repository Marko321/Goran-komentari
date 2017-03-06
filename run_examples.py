#From package import class

from Direktor import Tehnicki
from Direktor import Generalni
from Direktor import Cinkaros

tehn = Tehnicki(kol_besa=3)
tehn.opis()
gen = Generalni(kol_besa=4)
gen.opis()
cin = Cinkaros(kol_besa=5)
cin.opis()


#Evo ga solidno organizovan python modul. Obrati paznju na:

#__init__.py fajl, kako su import-ovane klase
#Na fajlove i klase unutar modula Direktor, kako se importuju klase
#Na fajlove iznvan modula, konkretno ovaj fajl, kako se pozivaju klase.