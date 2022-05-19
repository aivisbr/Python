
def find_words_by_pos(wrds:list = None, letters:list = None) -> list:
    """
    Funkcija find_words_by_pos atgriež sarakstu ar vārdiem no saraksta wrds, kuros ir visi
    letters nodefinētie burti, ņemot vērā letters burtu secību.\n
    Ja no wrds saraksta  ir nepieciešams atlasīt vārdu, kur pirmais burts vai otrais burts u.tml.
    nav zināms tad letters sarakstā burta vietā ieliek tukšu elementu '' (der jebkurš simbols, kurš nav burts)\n
    wrds - saraksts ar vārdiem\n
    letters - saraksts ar burtiem, kuri jāatrod vārdiem no saraksta wrds
    """
    finlist = []

    if len(wrds)==0:
        return finlist
    
    if len(letters)==0:
        return wrds
    
    for word in wrds:
        lcounter = 0
        match = 0
        for indx, l in enumerate(letters):
            if l.isalpha():
                lcounter += 1
                if l.upper()==word[indx].upper():
                    match += 1
        
        if lcounter>0 and lcounter==match:
            finlist.append(word)
    
    finlist.sort()

    if lcounter==0:
        return wrds

    return finlist


def find_words(wrds:list = None, letters:list = None, include:bool = True) -> list:
    """
    Funkcija find_words atgriež sarakstu ar vārdiem no saraksta wrds, kuros ir visi
    letters nodefinētie burti.\n
    wrds - saraksts ar vārdiem\n
    letters - saraksts ar burtiem, kuri jāatrod vārdiem no saraksta wrds
    """
    if len(letters)==0:
        return wrds

    mod_let = list(map(lambda x: x.lower(), letters))
    mod_wrds = list(set(wrds)) # Remove dublicates
    finlist = []
    
    for word in mod_wrds:
        counter = 0
        for letter in mod_let:
            if letter in word.lower():
                counter += 1
            if include and counter == len(mod_let):
                finlist.append(word)
        if not include and counter == 0:
            finlist.append(word)
    return finlist


def get_uniq_val(lst:list = None, ignore_case:bool = True) -> list:
    """
    Funkcija get_uniq_val atgriež sarakstu ar unikālām vērtībām.\n
    Ja ignore_case = True, tad teksta gadījumā lielie un mazie burti tiks uzskatīti kā vienādi. 
    """
    finres = []
    for l in lst:
        if type(l) == int or type(l) == float:
            if l not in finres:
                finres.append(l)
        else:
            if ignore_case:
                l = l.upper()
            if l not in finres and l.isalpha():
                finres.append(l)
    return finres
