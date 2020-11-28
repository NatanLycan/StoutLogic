import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from collections import namedtuple as nt
import numpy as np
from scipy import stats

#VAriables de Ejecucion
file = csv.reader(open("data/raw/data/ubicaciones.csv", "r",encoding='utf-8-sig'), delimiter=',')
f = csv.reader(open("data/raw/data/ubicaciones.csv", "r",encoding='utf-8-sig'), delimiter=',')
line_count = 0
l=[]
frecs=[]
todas_frecs=[]
minlat=0#y
maxlat=0#y
minlon=0#x
maxlon=0#x
vol_total=0


##VAriables de respuesta final
cliente = nt('cliente','CLIENTE, D1, D2, D3, D4, D5, D6')
respuesta=[]

#Obtengo las distintas frecuencias
for r in f:
    todas_frecs.append(r[2])
    if not frecs.__contains__(r[2]):
        frecs.append(r[2])
frecs.pop(0)
todas_frecs.pop(0)
frecs.sort()

#Inicializo variable por frecuencia
for n in frecs:
    exec("x"+n+"=[]\ny" + n + "=[]")



for row in file:
    if line_count == 0:
        Personas = nt('Personas', ", ".join(row))
        line_count += 1
    else:
        p1= Personas(row[0],row[1],int(row[2]),float(row[3]),float(row[4]),float(row[5]))
        #print(p1)
        l.append(p1)
        line_count += 1
        vol_total += float(row[3])
        if maxlat<p1.lat:
            maxlat=p1.lat
        elif minlat>p1.lat:
            minlat=p1.lat
        if maxlon<p1.lon:
            maxlon=p1.lon
        elif minlon>p1.lon:
            minlon = p1.lon
        #Aqui abajo se guardan datos para grafico de distribucion de entregas
        for n in frecs:
            txt="if p1.Frecuencia=="+n+":\n\tx"+n+".append(p1.lon)\n\ty"+n+".append(p1.lat)"
            exec(txt)
print("Volumen disponible: "+str(vol_total)+"\nVolumen por Grupo: "+str(vol_total/6))

#################Grafico Distribucion de entregas**********************s
#for n in frecs:
#    txt="xe"+n+"=np.array(x"+n+")\nye"+n+"=np.array(y"+n+")\nplt.scatter(xe"+n+", ye"+n+",label='Frecuencia "+n+"')"
#    exec(txt)
#plt.legend()
#plt.grid(True)
#plt.show()



##########Probability Distribution Frequency PDF***************
#bins = np.linspace(min(map(int,frecs))-1, max(map(int,frecs))+1, 10)
#histogram, bins = np.histogram(tuple(map(int,todas_frecs)), bins=bins, density=True)
#bin_centers = 0.5*(bins[1:] + bins[:-1])
#print(bins,histogram,bin_centers)

#pdf = stats.norm.pdf(bin_centers)

#plt.plot(bin_centers, histogram, label="Histogram of samples")
#plt.plot(bin_centers, pdf, label="PDF")
#plt.legend()
#plt.show()

##############################Anderson-DArling Test
#from scipy.stats import anderson
#a=anderson(tuple(map(int,todas_frecs)))
#print(a)