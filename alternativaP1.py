import sympy as smp
#Declaración de variables
pi = 3.1415
k = 9e9
Q = 1e-06
epsilon_0  = 8.85e-12


def ring(ratio, coordinate):
    variable = smp.symbols('S', real=True)
    integral_expr = (((k * Q) / (2 * pi * ratio)) * coordinate) / ((coordinate**2 + ratio**2)**(3/2))
    return smp.integrate(integral_expr, (variable, 0, (2 * pi * ratio)))

def disc(ratio, coordinate):
    variable = smp.symbols('r', real=True)
    sigma = Q/(pi*ratio**2)
    dQ = 2*pi*variable*sigma
    integral_expr = ((k*dQ*coordinate)/(coordinate**2+variable**2)**(3/2))
    return smp.integrate(integral_expr, (variable, 0, ratio))


print(ring(15, 37.5))
print(disc(1, 1))
