import CoreData

def all_messages_about_product(data, product_id):
    ret=[] 
    for i in data:
        if i["product"]==product_id: 
            ret.append(i) 
    ret.sort(key=lambda i:i["time"]) 
    return ret

# Fellistningen kan implementeras på flera sätt, här är ett par varianter
# En variant med felkoder som dict-värden
def test_sensors(data, product_id):
    sensor_list = tuple(sorted(mess["sensor"] for mess in all_messages_about_product(data, product_id)))
    error_codes = {
        (1,2,3,4): -1,
        (1,2,5,6): -1,
        (2,3,4): 1,
        (1,3,4): 2,
        (2,5,6): 1,
        (1,5,6): 2,
        (1,2,4): 3,
        (1,2,3): 4,
        (1,2,6): 5,
        (1,2,5): 6
    }
    if sensor_list in error_codes:
        return error_codes[sensor_list]
    else:
        return 0 # Annat fel

# Variant som använder mängder (set)
def test_sensors(data, product_id):
    sensor_set = set(mess["sensor"] for mess in all_messages_about_product(data, product_id))
    for s in [{1,2,3,4},{1,2,5,6}]:
        if sensor_set == s:
            return -1
        elif sensor_set < s: # A<B betyder för mängder att A är en äkta delmängd till B, dva att varje element i A också finns i B, men att finns minst ett element i B som inte finns i A.
            return (s - sensor_set).pop() # ger en sensor som felat, även om det var fler


def list_error_codes(data):
    product_set = set(m["product"] for m in data)
    for product in product_set:
        print(product, test_sensors(data, product))


list_error_codes(CoreData.sensor_data)

def vg(data):
    for product in set(m["product"] for m in data):
        mess_list = all_messages_about_product(data, product)
        # obs: mess_list är i tidsordning
        for k in range(1,len(mess_list)):
            if mess_list[k]["sensor"] < mess_list[k-1]["sensor"]:
                print(mess_list[k-1], mess_list[k], "i fel ordning")

vg(CoreData.sensor_data)
