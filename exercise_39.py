gradovi={'Nemacka':'Berlin','Francuska':'Pariz','Norveska':'Oslo','Danska':'Kopenhagen','Ceska':'Prag'}
drzave={'Nemacka':'DE','Francuska':'FRA','Norveska':'NOR'}
drzave['Ceska']='CEZ'
drzave['Danska']='DEN'

for drz,skr in drzave.items():
    print ('Drzava %s ima skraceni naziv: %s i njen glavni grad je:%s' %(drz,skr,gradovi[drz]))
    
grad=gradovi.get('Nemacka','nema')

print (grad)

drzava=drzave.get('Norveska', None)
if drzava:
    print('Skracenica je %s' %drzava)
else:
    print('Skracenica nije dostupna')