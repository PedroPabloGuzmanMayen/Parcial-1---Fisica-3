import sympy as smp
import numpy as np
import scipy as sp
from scipy.integrate import quad
class ElectricField:
    
    def __init__(self):
        self.charge = 1e-06
        self.constant = 9e09

    def calcRing(self, ratio, cordinate):
        variable = smp.symbols("S", real=True) #Indicar la variable con respecto a la cuál vamos a integrar
        return smp.integrate((((self.constant)*(self.charge/(2*smp.pi*ratio))*cordinate)/((cordinate**2+ratio**2)**1.5)), (variable, 0, ((2*smp.pi)*ratio))) #Retornamos el valor de la integral respecto a S. Multiplicamos la constante 

    def calcDisc(self, ratio, coordinate):
        variable = smp.symbols('r', real=True) #Definir la variable respecto a la que integraremos
        sigma = self.charge / (smp.pi * ratio**2) #Definir sigma
        dQ = 2 * smp.pi * variable * sigma #Definir el diferencial de carga
        integrand = ((self.constant * dQ * coordinate) / (coordinate**2 + variable**2)**(3/2)) #Armar la expresión a integrar
        #Se usa scipy, pues con simpy existía un error de tipo de dato
        integrand_func = smp.lambdify(variable, integrand, 'numpy') #COnvertir la expresión de simpy a una función que puede usarse en scipy
        result, _ = quad(integrand_func, 0, float(ratio))  # Integrar utlizando scipy, almacenar en la variable result. Utilizar la coma para especificar el formato en que queremos el resultado
    
        return result #Retornar el resultado
    
    def calcLine()

    


hola = ElectricField()
print(hola.calcRing(65.83923,43.6578))
x = smp.symbols('r', real = True)
print(((x)**2+(4)**2)**1.5)
print(hola.calcDisc(133.8586,20.4555))