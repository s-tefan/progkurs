

def hälsa_välkommen():
    print("Välkommen!")

def ta_reda_på_namn():
    svar = input("Vad heter du? ")
    return {'namn': svar} # Skapar en person (typ dict) med angivet namn

def tacka(person):
    print("Tack " + person['namn'] +"!", "Ha det bra!")

def ta_emot_person():
    hälsa_välkommen()
    person = ta_reda_på_namn() # Tar reda på namnet och kopplar personen till variabeln 'person'
    tacka(person)
    return person

#ta_emot_person()


def ta_emot(antal_platser):
    fullt = False
    deltagarlista = [] # En tom lista
    while not fullt:
        person = ta_emot_person()
        deltagarlista.append(person) # Lägger till person till deltagarlista
        if len(deltagarlista) >= antal_platser:
            fullt = True
    print("Nu är det tyvärr fullt! Välkomna åter i morgon!")
    return(deltagarlista)

print(ta_emot(3))
