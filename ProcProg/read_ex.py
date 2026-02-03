with open("min_csv.csv") as f:
    data = f.read()
print(data)
for c in data:
    print(c, end = '')

with open("min_csv.csv") as f:
    line_data = [line for line in f]
print(line_data)