import numpy as np

from scipy.interpolate import interp1d


class PREos:
    "Ecuaci\'on de estado de Peng-Robinson"

    def __init__(self,a,b, w=0.344):
        self.a = a
        self.b = b
        self.w = w
        pass

    
    def p(self,rho,T):
        "Presi\'on"


        theta = ( 1. + (0.37464 + 1.54226 * self.w - 0.26992 * self.w * self.w) * (1 - np.sqrt(T/self.Tc()))  )**2
        
        return rho * T / (1. - rho * self.b)  -  self.a * theta * rho * rho / ( 1.  +  2. * self.b * rho  -  self.b * self.b * rho * rho )


    def Tc(self):
        "Temperatura cr\'itica"

        return 0.0778 * self.a / (0.45724 * self.b)


    
    def Pc(self):
        "Presi\'on cr\'itica"

        return 0.0778 * self.Tc() / self.b


    
    def rhoc(self):
        "Densidad cr\'itica"

        return 0.253077 / self.b


    def initRho(self,T):
        "Densidad inicial. Ayuda a la convergencia"

        it = np.array([0.99*self.Tc(), 0.9*self.Tc(), 0.8*self.Tc(), 0.7*self.Tc(), 0.6*self.Tc(), 0.5*self.Tc()])

        ir = np.array([0.1, 0.05, 0.05, 0.01, 0.005, 7e-04])

        f = interp1d(it, ir)

        return f(T)

    
