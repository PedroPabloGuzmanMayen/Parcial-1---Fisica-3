import sympy as smp
import scipy as sp
import numpy as np




#Esta función se encargará de calcular el campo eléctrico del anillo

constant = smp.symbols("Eo", real = True)

expression = 1/(4*smp.pi*constant)

def ring(ratio):
    surface = smp.symbols('s', real=True)
    x_variable = smp.symbols('x', real=True)
    linear_density = smp.symbols('l', real=True, positive=True)*smp.symbols("ds", real=True)
    ratio = ratio
    x_component = x_variable/smp.sqrt(x_variable**2 + ratio**2)
    print(linear_density*x_component*expression)



#Está función se encarga de calcular el campo eléctrico de la línea
def line():
    pass

#Esta función calcula el campo de un disco
def disc():
    pass




x_variable = smp.symbols('1', real=True)
surface = smp.symbols('s', real=True)

print(smp.integrate(x_variable, surface))
print("Pinche chems")
