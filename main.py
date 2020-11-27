import csv
from collections import namedtuple 

Personas = namedtuple('Personas', 'name, age')
path="test.csv"

for p in map(Personas._make, csv.reader(open(path, "r"))):
    print(p.name, p.age)