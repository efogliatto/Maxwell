import scipy.integrate as integrate

from .roots import roots


def eosIntegral(p0, eos, T):

    f=lambda x:p0 - eos.p(x,T)

    a = roots(f, 0, 1)[0:3]

    g=lambda r:f(r)/r**2
    
    return integrate.quad(g, a[0], a[2])
