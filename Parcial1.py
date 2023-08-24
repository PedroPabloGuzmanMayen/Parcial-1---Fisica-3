import sympy as smp
import scipy as sp
import numpy as np




#Esta función se encargará de calcular el campo eléctrico del anillo

constant = smp.symbols("Eo", real = True)

expression = 1/(4*smp.pi*constant)


def ring(ratio):
    ratio = smp.symbols(ratio, real = True)
    surface = smp.symbols('s', real=True)
    x_variable = smp.symbols('x', real=True)
    linear_density = smp.symbols('Q', real=True)/(2*smp.pi * ratio)
    f = 1/(x_variable**2+ratio**2)
    x_component = x_variable/smp.sqrt(x_variable**2 + ratio**2)
    equation = linear_density*x_component*expression*f

    return smp.integrate(equation, (surface, 0, 2*smp.pi*ratio))

#Está función se encarga de calcular el campo eléctrico de la línea
def line():
    surface = smp.symbols('y', real=True)
    x_variable = smp.symbols('x', real=True)
    linear_density = smp.symbols 
#Esta función calcula el campo de un disco
def disc():
    pass




print(ring('R'))

