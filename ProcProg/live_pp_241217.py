import CoreData_241217

data = CoreData_241217.data


def value_of(product):
    a = product['value']/product['weight']
    return a

def score_all(product_list):
    for product in product_list:
        # Ändra product['score'] till value_of(product)
        product['score'] = value_of(product)

print("Före")
for p in data:
    print(p)

score_all(data)

print("Efter")
for p in data:
    print(p)





