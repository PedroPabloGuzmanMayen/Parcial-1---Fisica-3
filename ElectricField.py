import sympy as smp
class ElectricField:
    
    def __init__(self):
        self.charge = 1e-06
        self.constant = 9e09

    def calcRing(self, ratio, cordinate):
        variable = smp.symbols("S", real=True)
        return smp.integrate((((self.constant)*(self.charge/(2*smp.pi*ratio))*cordinate)/((cordinate**2+ratio**2)**1.5)), (variable, 0, ((2*smp.pi)*ratio)))

hola = ElectricField
print(hola.calcRing(3,3))
