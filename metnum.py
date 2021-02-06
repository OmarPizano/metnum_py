# f = función
# xl = intervalo inferior
# xu = interfalo superior
# xr = raíz inicial de la iteración, al principio es 0
# imax = máximo número de iteraciones (condición de parada)
# i = iteración actual, al principio es 0
# err = error relativo fijado (condición de parada)
# err_a = error relativo, al principio es 0
# rr = raíz real
def bisection(f, xl, xu, xr, err, err_a, i, imax, rr):
    xrold = xr
    xr = (xl + xu) / 2
    i += 1
    if xr != 0:
        err_a = abs((xr - xrold) / xr) * 100
    err_t = abs(rr - xr)
    print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(i,xl,xu,xr,err_a,err_t))
    test = f(xl) * f(xr)
    if test < 0:
        xu = xr
    elif test > 0:
        xl = xr
    else:
        err_a = 0
    if err_a > err and i < imax:
        xr = bisection(f,xl,xu,xr,err,err_a,i,imax, rr)
    return xr

def falsepos(f, xl, xu, xr, err, err_a, i, imax, rr):
    xrold = xr
    xr = xu - (f(xu) * (xl - xu) / (f(xl) - f(xu)) )
    i += 1
    if xr != 0:
        err_a = abs((xr - xrold) / xr) * 100
    err_t = abs(rr - xr)
    print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(i,xl,xu,xr,err_a,err_t))
    test = f(xl) * f(xr)
    if test < 0:
        xu = xr
    elif test > 0:
        xl = xr
    else:
        err_a = 0
    if err_a > err and i < imax:
        xr = bisection(f,xl,xu,xr,err,err_a,i,imax, rr)
    return xr

def fixpt(f, x0, err, imax, rr):
    i = 0
    xr = x0
    while True:
        xrold = xr
        xr = f(xrold)
        i += 1
        if xr != 0:
            err_a = abs((xr - xrold) / xr) * 100
        err_t = abs(rr - xr)
        print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(i,x0,xr,err_a,err_t))
        if err_a < err or i >= imax:
            break
    return xr
