import pathlib
'''Givet en fil (som ligger i samma mapp som programkoden) med en tabell 
där varje rad har semikolonåtskilda 'celler', läs in filen filnamn och skapa 
en lista med ett element för varje rad som i sin tur är en lista av innehållet i respektive cell'''

''' Inläsning av csv-fil med pythons standardfunktioner'''
filename = "greenhouse-gase-emissions-industry-and-household-cleaned.csv"
with open(pathlib.Path(__file__).parent / filename) as csv_file:
    row_list = [row.strip().split(';') for row in csv_file]
    # Går igenom alla rader i tur och ordning och skapar en motsvarande lista
    # med hjälp av 'list comprehension', en kompakt form av for-loop 
    # .strip() tar bort blanksteg och radslut i textradens ändar
    # .split(';') delar upp textraden i en lista av delar, åtskilda av ';'
    # Resultatet blir en lista av raddata, som i sin tur är en lista av data (typ str) på den raden för respektive kolumn

''' Variant som använder modulen csv:
import csv
filename = "greenhouse-gase-emissions-industry-and-household-cleaned.csv"
with open(pathlib.Path(__file__).parent / filename) as csv_file:
    row_list = list(csv.reader(csv_file, delimiter=";"))
'''


rubriker = row_list[0] # plockar ut rubrikerna från första raden
post_dict_list = [] # initierar en tom lista att fylla på med dataposter
for row in row_list[1:]: # går igenom alla rader utom första
    post_dict = {} # skapa en tom datapost som dict för att sedan fylla på
    for k, rubrik in enumerate(rubriker): # k: index, rubrik: rubriker[k]
        post_dict[rubrik] = row[k]
    post_dict_list.append(post_dict) # Lägg till posten i listan


def timeline(dl, ad, variable, units):
    '''En funktion som ur datapostlistan dl filtrerar ut de poster där
    ad är värdet till nyckeln 'anzsic_descriptor',
    variable är värdet till nyckeln 'variable' och
    units är värdet av nyckeln 'units'
    Returnerar en lista med poster som dicts med nycklarna 'year', 'data_value' och 'units'
    [ {'year': ..., 'data_value': ..., 'units': ...}, ...]
    '''
    out_list = []
    for post in dl:
        if post['anzsic_descriptor'] == ad and post['variable'] == variable and post['units'] == units:
            out_list.append({'year': post['year'], 'data_value': post['data_value'], 'units': post['units']})
    return out_list

'''Exempel på att presentera data'''

anzic_descriptor = 'Agriculture'
variable = 'Carbon dioxide'
units = 'Kilotonnes'
choice = timeline(post_dict_list, anzic_descriptor, variable, units)

import matplotlib.pyplot as plt
fig, ax = plt.subplots() # Initierar ett diagram
x = [int(post['year']) for post in choice]  # Plockar ut årtalen som en lista av heltal
y = [float(post['data_value']) for post in choice] # Plockar ut utsläppsvärden som en lista av flyttal
ax.stem(x,y) # Gör ett diagram över värdena i y mot värdena i x. Testa gärna olika diagramtyper enligt
# dokumentationen för matplotlib https://matplotlib.org/stable/plot_types/index.html
ax.set_title(choice[0]['units'], loc='left', fontsize='medium') # sätt ut enhet vid y-axeln
fig.suptitle('Emission of ' + variable + ' from ' + anzic_descriptor) # Sätt en titel för figuren
plt.show() # Visa diagrammet i ett fönster






