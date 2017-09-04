import numpy as np
import pylab as pl 
#Vector (arreglo) con los valores del eje x
x=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
#Vector (arreglo) con los valores del eje y
y=[0,0,0,0,0,1,1,1,1,2,2,3,3,4,4,4,5,6,6,7,7]
#Grafica el vector x contra el vector y
pl.plot(x,y)
pl.ylabel('Numero de novios y mascotas')
pl.xlabel('Anios')
pl.title('Numero de novios y mascotas por anio de vida')
#Guarda la grafica
pl.savefig('temp1.png') 
