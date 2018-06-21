import math

from .rootsearch import rootsearch

from .bisect import bisect


def roots(f, a, b, eps=1e-6):

    r = []
    
    while 1:
        x1,x2 = rootsearch(f,a,b,eps)
        if x1 != None:
            a = x2
            root = bisect(f,x1,x2,1)
            if root != None:
                pass

                r.append(round(root,-int(math.log(eps, 10))))
        else:
            break

    return r
