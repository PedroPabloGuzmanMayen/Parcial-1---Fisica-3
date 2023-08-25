import sympy as smp 
#Declaración de variables
pi = 3.1415
pi_smp = smp.symbols('\u03C0')
E0_smp = smp.symbols('\u03B50')
k = 9e9
k_smp = smp.symbols(f'1/(4{pi_smp}{E0_smp})')
radius = 2
Q = 1
radius_smp = smp.symbols('R')
lambda_smp = smp.symbols('\u03BB')
lambda_ = Q/radius
dQ_linesmp = lambda_smp/radius_smp
sigma_ = Q/(4*pi*radius**2)

#Densidades de carga


print(sigma_)

