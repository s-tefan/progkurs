def read_data(f, sep = ','):
    '''Läs in en fil av rader och returnera en lista av 
    dataposter (records) av typ dict.
    Första raden består av nycklarna till dataposternas fält.
    Efterföljande rader, en per post, består av
    värden av typ 'str' för respektive fält. 
    Funktionen returnerar en lista av dict.
    '''
    h = f.readline()
    headers = plocka(h, sep)
    n = len(headers)
    data_list = []
    for line in f:
        values = plocka(line, sep)
        data_record = {}
        for k in range(n):
            data_record[headers[k]] = values[k]
        data_list.append(data_record)
    print(data_list)

def plocka(line_string, sep=','):
    '''Delar upp teckensträng line_string som en lista av delar åtskilda av "," 
    eller alternativ symbol angiven i sep. Eventuell "whitespace" som blanksteg 
    eller tab runt delarna tas bort
    '''
    return [s.strip() for s in line_string.strip().split(sep)]

with open('min_csv.csv', 'r') as f:
    read_data(f)

          
