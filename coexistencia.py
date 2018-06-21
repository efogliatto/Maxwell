import scipy.optimize as op

from .eosIntegral import eosIntegral

from .roots import roots


def coexistencia(eos, T):
    """
    Densidades de coexistencia

    Argumentos
    eos: Ecuacion de estado
    T: temperatura (no reducida)
    """


    # Funcion lambda para integral

    intFunc = lambda x: eosIntegral( x, eos, T )


    # Resolucion: presion de equilibrio
    
    p0 = op.fsolve( intFunc, eos.p(0.08,T) )


    # Resolucion: densidades de coexistencia a partir de presion de equilibrio

    f=lambda x:p0 - eos.p(x,T)

    a = roots(f, 0, 1)[0:3]
    
    

    rl = a[2]

    rg = a[0]

    return rl, rg
    
