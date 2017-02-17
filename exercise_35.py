def cinkaros():
    print'Ovo ti je kolega koji ti je radio iza ledja.'
    print'Mozes ga kazniti cvrgama.'
    broj=int(raw_input('Koliko ces mu cvrga lupiti?'))
    if broj == 0:
        ispis('Dokazao si da smo bili u zabludi, ti si dobar covek')
    elif broj>0 and broj<10:
        if broj<5:
            ispis('Zasluzio je da ga zaboli glava.')
        else:
            ispis('Mislim da preterujes.')
    elif broj >10:
        ispis('Dobra fora, bas si ga uplasio.')
    else:
        ispis('Nisi lepo uneo broj.')
        cinkaros()
    
def generalni():
    odgovor=raw_input('/Da li bi galamio ili mirno izneo cinjenice?/')
    if 'gal' in odgovor:
        ispis('Verujem Vam kolega, ali dodjite juce na razgovor')
    elif 'mir' in odgovor:
        clan = raw_input('Kolega Vi ste bese clan nase biblioteke?')
        if clan == 'da':
            print('Vec neko vreme razmisljam kako da iskoristim Vase potencijale')
            cinkaros()
        else:
             ispis('Zao mi je, ali ne mogu Vam pomoci dok ne nabavite clansku kartu')
             
def tehnicki():
    print'Kolega cujem da ste nezadovoljni novom preraspodelom radnih mesta?'
    print'Kazite sta Vas muci?'
    odgovor=raw_input('/Da li bi galamio ili mirno izneo cinjenice?/')
    if 'gal' in odgovor:
        ispis('Sledeci put povedite racuna o svom ponasanju.')
    else:
        print'Mozete popricati sa generalnim, sve ovo je njegova zamisao.'
        generalni()
        
def ispis(recenica):
    print recenica + ' Takav je zivot.'
    exit(0)
    
def izbor():
    print'Imali ste problem na poslu, oseceni ste novom preraspodelom posla.'
    odgovor=raw_input('Da li biste se obratili tehnickom ili generalnom direktoru?')
    if 'teh' in odgovor:
        tehnicki()
    else:
        generalni()