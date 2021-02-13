from inspect import getsourcelines
def bisection(function, lower_x, upper_x, real_root = False, error_limit = 0.5, max_iteration = 20, table = False, summary = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = 0            # raíz inicial
    results = []        # matriz para los datos de la tabla
    # resumen de los datos de entrada
    if summary:
        summ = "\nFunction: " + str(getsourcelines(function)[0][0][:-1].split(":")[1][1:])
        summ += "\nLower X: " + str(lower_x)
        summ += "\nUpper X: " + str(upper_x)
        summ += "\nReal Root: " + str(real_root)
        summ += "\nError Limit: " + str(error_limit)
        summ += "\nMax Iteration: " + str(max_iteration)
        summ += "\n"
        print(summ)
    # algoritmo de BISECCIÓN
    while True:
        old_root = root
        root = (lower_x + upper_x) / 2
        iteration += 1
        if root != 0:
            relative_error = abs((root - old_root)/ root ) * 100
        test = function(lower_x) *  function(root)
        if test < 0:
            upper_x = root
        elif test > 0:
            lower_x = root
        else:
            relative_error = 0
        # si se especifica una raíz real, se calcula el error real
        if real_root:
            real_error = abs((real_root - root) / real_root) * 100
        else:
            real_error = "---"
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        results.append([iteration, lower_x, upper_x, root, old_root, relative_error, real_error])
        # condición de parada
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXL\tXU\tR\tOLD_R\tERR_A\tERR_R\n" + "-" * tableline)
        for row in results:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root

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

def fixpt(f, x0, err, imax, rr, verbose):
    i = 0
    xr = x0
    if verbose:
        print("N°\tx0\txr\terr_a\terr_t\n"+"-"*50)
    while True:
        xrold = xr
        xr = f(xrold)
        i += 1
        if xr != 0:
            err_a = abs((xr - xrold) / xr) * 100
        err_t = abs(rr - xr)
        if verbose:
            print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(i,x0,xr,err_a,err_t))
        if err_a < err or i >= imax:
            break
    return xr

# df = derivada de f.
def newton_raphson(f, df, x0, err, imax, rr, verbose):
    i = 0
    xr = x0
    if verbose:
        print("N°\tx0\txr\terr_a\terr_t\n"+"-"*50)
    while True:
        xrold = xr
        xr = xrold - f(xr) / df(xr)
        if xr != 0:
            err_a = abs((xr - xrold) / xr) * 100
        err_t = abs(rr - xr)
        if verbose:
            print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(i,x0,xr,err_a,err_t))
        if err_a < err or i >= imax:
            break
        i += 1
    return xr
