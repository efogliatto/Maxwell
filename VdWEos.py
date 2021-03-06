import numpy as np

from scipy.interpolate import interp1d


class VdWEos:
    "Ecuaci\'on de estado de Van Der Waals"

    def __init__(self,a,b):
        self.a = a
        self.b = b
        pass

    def p(self,rho,T):
        "Presi\'on"
        
        return rho * T / (1 - rho*self.b) - self.a * rho**2


    def Tc(self):
        "Temperatura cr\'itica"

        return 8. * self.a / (27. * self.b)


    def Pc(self):
        "Presi\'on cr\'itica"

        return self.a / (27. * self.b**2)

    def rhoc(self):
        "Densidad cr\'itica"

        return 1. / (3. * self.b)

    
    def initRho(self,T):
        "Densidad inicial. Ayuda a la convergencia"

        it = np.array([0.99*self.Tc(), 0.9*self.Tc(), 0.8*self.Tc(), 0.7*self.Tc(), 0.6*self.Tc(), 0.5*self.Tc()])

        ir = np.array([0.08, 0.08, 0.08, 0.05, 0.005, 0.005])

        f = interp1d(it, ir)

        return f(T)
