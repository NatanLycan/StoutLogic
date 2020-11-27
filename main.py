import csv
from collections import namedtuple 

Personas = namedtuple('Personas', 'name, age')


for p in map(Personas._make, csv.reader(open("test.csv", "r"))):
    print(p.name, p.age)