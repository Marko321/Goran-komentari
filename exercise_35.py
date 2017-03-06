def cinkaros():
    print'Ovo ti je kolega koji ti je radio iza ledja.\n'
    print'Mozes ga kazniti cvrgama.\n'
    try:
        broj=int(raw_input('Koliko ces mu cvrga lupiti?\n'))
    except ValueError as e:
        #Program ce baciti value error ako unesemo slovo ili neki znak
        #validacija je bitna mnogo i kasnije u web development-u
        # , jer se mora tacno specificirati sta se zeli od servisa
        ispis("Moras uneti broj!\n")
        broj = -1
    if broj == 0:
        ispis('Dokazao si da smo bili u zabludi, ti si dobar covek\n')
    elif broj>0 and broj<10:
        if broj<5:
            ispis('Zasluzio je da ga zaboli glava.\n')
        else:
            ispis('Mislim da preterujes.\n')
    elif broj >10:
        ispis('Dobra fora, bas si ga uplasio.\n')
    else:
        ispis('Nisi lepo uneo broj.\n')
        cinkaros()
    
def generalni():

    odgovor=raw_input('/Da li bi galamio ili mirno izneo cinjenice?/\n')
    if 'gal' in odgovor:
        ispis('Verujem Vam kolega, ali dodjite juce na razgovor\n')
    elif 'mir' in odgovor:
        clan = raw_input('Kolega Vi ste bese clan nase biblioteke?\n')
        if clan == 'da':
            print('Vec neko vreme razmisljam kako da iskoristim Vase potencijale\n')
            cinkaros()
        else:
             ispis('Zao mi je, ali ne mogu Vam pomoci dok ne nabavite clansku kartu\n')
    else:
        #Mora postojati i handle-ovanje else grane!
        ispis("Moras uneti reci galamio ili mirno!\n")
             
def tehnicki():
    #Ovde sve ok
    print'Kolega cujem da ste nezadovoljni novom preraspodelom radnih mesta?\n'
    print'Kazite sta Vas muci?'
    odgovor=raw_input('/Da li bi galamio ili mirno izneo cinjenice?/\n')
    if 'gal' in odgovor:
        ispis('Sledeci put povedite racuna o svom ponasanju.\n')
    else:
        print'Mozete popricati sa generalnim, sve ovo je njegova zamisao.\n'
        generalni()
        
def ispis(recenica):
    print recenica + ' Takav je zivot.\n'
    #Hocemo da testiramo sva 3 pa necemo da izlazimo iz procesa ovde
    #exit(0)
    
def izbor():
    print'Imali ste problem na poslu, oseceni ste novom preraspodelom posla.\n'
    odgovor=raw_input('Da li biste se obratili tehnickom ili generalnom direktoru?\n')
    if 'teh' in odgovor:
        tehnicki()
    else:
        generalni()


cinkaros()
tehnicki()
generalni()
izbor()