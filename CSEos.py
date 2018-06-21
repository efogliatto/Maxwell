import numpy as np

from scipy.interpolate import interp1d


class CSEos:
    "Ecuaci\'on de estado de Carnahan-Starling"

    def __init__(self,a,b):
        self.a = a
        self.b = b
        pass

    
    def p(self,rho,T):
        "Presi\'on"

        c = self.b * rho / 4.
        
        return rho * T * ( (1 + c + c**2 - c**3) / (1-c)**3) - self.a * rho**2


    def Tc(self):
        "Temperatura cr\'itica"

        return self.a * 0.18727 / (self.b * 0.4963)


    
    def Pc(self):
        "Presi\'on cr\'itica"

        return 0.18727 * self.Tc() / self.b


    
    def rhoc(self):
        "Densidad cr\'itica"

        return 0.5218 / self.b


    def initRho(self,T):
        "Densidad inicial. Ayuda a la convergencia"

        it = np.array([0.99*self.Tc(), 0.9*self.Tc(), 0.8*self.Tc(), 0.7*self.Tc(), 0.6*self.Tc(), 0.5*self.Tc()])

        ir = np.array([0.1, 0.02, 0.01, 0.01, 0.005, 7e-04])

        f = interp1d(it, ir)

        return f(T)

    
