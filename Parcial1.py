import sympy as smp
import scipy as sp
import numpy as np




#Esta función se encargará de calcular el campo eléctrico del anillo

charge = 0
constant = smp.symbols("Eo", real = True)

expression = 1/(4*smp.pi*constant)

def getDensity():
    pass

def ring(ratio):
    ratio = smp.symbols(ratio, real = True)
    surface = smp.symbols('s', real=True)
    x_variable = smp.symbols('x', real=True)
    density = smp.symbols('Q', real=True)/(2*smp.pi * ratio)
    f = 1/(x_variable**2+ratio**2)
    x_component = x_variable/smp.sqrt(x_variable**2 + ratio**2)
    equation = density*x_component*expression*f

    return smp.integrate(equation, (surface, 0, 2*smp.pi*ratio))

#Está función se encarga de calcular el campo eléctrico de la línea
def line(a):
    # Variables simbólicas
    x = smp.symbols('x', real=True)
    a = smp.symbols('a', real=True)
    epsilon = smp.symbols('E_0', real=True)
    r_ = (x**2 + a**2)**(3/2)
    expression = a / r_
    electric_field = smp.integrate(expression, (x, -smp.oo, smp.oo))
    return epsilon * electric_field


#Esta función calcula el campo de un disco
def disc(ratio):
    #Variables simbólicos
    sigma = smp.symbols('sigma', real=True)
    Q = smp.symbols('Q', real = True)
    #Se reutiliza la función ring() para la integral de disc(), subss() funciona para sustituir
    #el primer elemento, por el segundo, en este caso Q por sigma
    return ring(ratio).subs(Q, sigma).simplify()


print(line('A'))

