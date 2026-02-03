import CoreData_241217

def value_of(product):
    """Denna funktion tar en produkt från listan som
    indata och returnerar kvoten mellan produktens värde('value) och vikt('weight'). 
    Det returnerade värdet ska vara högre när kvoten mellan värde och vikt är "bra". 
    Detta returnerade värde blir produktens poäng ('score')."""
    return product['value']/product['weight']

def score_all(product_list):
    """Denna funktion uppdaterar en lista av produkter gonam att sätta fältet
    'score' till kvoten av värdena av 'value' och 'weight'"""
    for product in product_list:
        product['score'] = value_of(product)
    return None

def find_best_product(product_list):
    best = None
    for product in product_list:
        if best:        
            if product['score'] > best['score']:
                best = product
        else:
            best = product

    return best

def alt_find_best_product(product_list):
    return max(product_list, key = lambda x: x['score'])

def display_products(product_list):
    for product in product_list:
        print(product)

def main(product_list):
    score_all(product_list)
    best = find_best_product(product_list)
    best['taken'] = True
    print('Best product:')
    print(best)
    print('All products:')
    display_products(product_list)

def fill_pallet(product_list, max_load):
    pallet_load = 0
    pallet_list = []
    score_all(product_list)
    while True:
        candidate_list = [p for p in product_list if not p['taken']]
        if candidate_list == []:
            return pallet_list
        best = find_best_product(candidate_list)
        if pallet_load + best['weight'] <= max_load:
            pallet_load += best['weight']
            pallet_list.append(best)
        best['taken'] = True



main(CoreData_241217.data)

print('++++')
for p in CoreData_241217.data:
    p['taken'] = False

display_products(fill_pallet(CoreData_241217.data, 150))
print('====')
display_products(CoreData_241217.data)
