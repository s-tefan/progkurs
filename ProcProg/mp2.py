import csv
import pathlib

#cl = list(csv.reader(open(pathlib.Path(__file__).parent / "greenhouse-gase-emissions-industry-and-household-cleaned.csv"), delimiter=";"))
cl = list(csv.reader(open("greenhouse-gase-emissions-industry-and-household-cleaned.csv"), delimiter=";"))
print(cl[0])

cdl = list(csv.DictReader(open("greenhouse-gase-emissions-industry-and-household-cleaned.csv"), delimiter=";"))


print(cdl[0])
import matplotlib.pyplot as P


xs,ys = [],[]
for post in cdl:
    print(f"={post['variable']=}")
    if post['variable'] == 'Carbon dioxide' :
        xs.append(post['year'])
        ys.append(float(post['data_value']))

print(len(xs))
P.scatter(xs,ys)
P.show()
