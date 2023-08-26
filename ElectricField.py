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
    #Realizar el procedimiento anterior, slamente que con los valores correspondientes a una línea de carga
    def calcLine(self, lenght, cordinate):
        variable = smp.symbols("y", real = True)
        linear_density = self.charge/lenght
        expression = cordinate/(cordinate**2+variable**2)**(3/2)
        integrand = self.constant*linear_density*expression
        integrand_func = smp.lambdify(variable, integrand, 'numpy' )
        result, _ = quad(integrand_func, float(-lenght/2), float(lenght/2))
        return result

