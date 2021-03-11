from inspect import getsourcelines
def bisection(function, lower_x, upper_x, real_root = False, error_limit = 0.5, max_iteration = 20, table = False, summary = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = 0            # raíz inicial
    table_data = []     # matriz para los datos de la tabla
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
        current_data = []   # lista para los datos de la iteración actual
        old_root = root
        root = (lower_x + upper_x) / 2
        iteration += 1
        current_data.extend([iteration, lower_x, upper_x, root, old_root])
        if root != 0:
#            relative_error = abs((root - old_root) / root ) * 100
            relative_error = abs((upper_x - lower_x) / (upper_x + lower_x)) * 100
            current_data.append(relative_error)
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
        current_data.append(real_error)
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        table_data.append(current_data)
        # condición de parada
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXL\tXU\tR\tOLD_R\tERR_A\tERR_R\n" + "-" * tableline)
        for row in table_data:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root

def falsepos(function, lower_x, upper_x, real_root = False, error_limit = 0.5, max_iteration = 20, table = False, summary = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = 0            # raíz inicial
    table_data = []     # matriz para los datos de la tabla
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
    # algoritmo de FALSA POSICIÓN
    while True:
        current_data = []   # lista para los datos de la iteración actual
        old_root = root
        root = upper_x - (function(upper_x) * (lower_x - upper_x)) / (function(lower_x) - function(upper_x))
        iteration += 1
        current_data.extend([iteration, lower_x, upper_x, root, old_root])
        if root != 0:
            relative_error = abs((root - old_root) / root ) * 100
            current_data.append(relative_error)
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
        current_data.append(real_error)
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        table_data.append(current_data)
        # condición de parada
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXL\tXU\tR\tOLD_R\tERR_A\tERR_R\n" + "-" * tableline)
        for row in table_data:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root

def fixpt(function, init_x, real_root, error_limit = 0.5, max_iteration = 20, summary = False, table = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = init_x       # raíz inicial
    table_data = []     # matriz para los datos de la tabla
    # resumen de los datos de entrada
    if summary:
        summ = "\nFunction: " + str(getsourcelines(function)[0][0][:-1].split(":")[1][1:])
        summ += "\nInit X: " + str(init_x)
        summ += "\nReal Root: " + str(real_root)
        summ += "\nError Limit: " + str(error_limit)
        summ += "\nMax Iteration: " + str(max_iteration)
        summ += "\n"
        print(summ)
    while True:
        current_data = []   # lista para los datos de la iteración actual
        old_root = root
        root = function(old_root)
        iteration += 1
        current_data.extend([iteration, root])
        if root != 0:
            relative_error = abs((root - old_root) / root ) * 100
            current_data.append(relative_error)
        # si se especifica una raíz real, se calcula el error real
        if real_root:
            real_error = abs((real_root - root) / real_root) * 100
        else:
            real_error = "---"
        current_data.append(real_error)
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        table_data.append(current_data)
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXI\tERR_A\tERR_R\n" + "-" * tableline)
        for row in table_data:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root

def newton_raphson(function, derivative, init_x, real_root, error_limit = 0.5, max_iteration = 20, summary = False, table = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = init_x       # raíz inicial
    table_data = []     # matriz para los datos de la tabla
    # resumen de los datos de entrada
    if summary:
        summ = "\nFunction: " + str(getsourcelines(function)[0][0][:-1].split(":")[1][1:])
        summ = "\nDerivative: " + str(getsourcelines(derivative)[0][0][:-1].split(":")[1][1:])
        summ += "\nInit X: " + str(init_x)
        summ += "\nReal Root: " + str(real_root)
        summ += "\nError Limit: " + str(error_limit)
        summ += "\nMax Iteration: " + str(max_iteration)
        summ += "\n"
        print(summ)
    while True:
        current_data = []   # lista para los datos de la iteración actual
        old_root = root
        root = old_root - function(root) / derivative(root)
        iteration += 1
        current_data.extend([iteration, root])
        if root != 0:
            relative_error = abs((root - old_root) / root) * 100
            current_data.append(relative_error)
        # si se especifica una raíz real, se calcula el error real
        if real_root:
            real_error = abs((real_root - root) / real_root) * 100
        else:
            real_error = "---"
        current_data.append(real_error)
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        table_data.append(current_data)
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXI\tERR_A\tERR_R\n" + "-" * tableline)
        for row in table_data:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root

def secant(function, init_x, prev_x, real_root, error_limit = 0.5, max_iteration = 20, summary = False, table = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = init_x       # raíces iniciales
    prev_x = prev_x
    table_data = []     # matriz para los datos de la tabla
    # resumen de los datos de entrada
    if summary:
        summ = "\nFunction: " + str(getsourcelines(function)[0][0][:-1].split(":")[1][1:])
        summ += "\nInit X: " + str(init_x)
        summ += "\nPrev X: " + str(prev_x)
        summ += "\nReal Root: " + str(real_root)
        summ += "\nError Limit: " + str(error_limit)
        summ += "\nMax Iteration: " + str(max_iteration)
        summ += "\n"
        print(summ)
    while True:
        current_data = []   # lista para los datos de la iteración actual 
        old_root = root
        root = root - (function(root) * (prev_x - root)) / (function(prev_x) - function(root))
        prev_x = old_root
        iteration += 1
        current_data.extend([iteration, root])
        if root != 0:
            relative_error = abs((root - old_root) / root) * 100
            current_data.append(relative_error)
        # si se especifica una raíz real, se calcula el error real
        if real_root:
            real_error = abs((real_root - root) / real_root) * 100
        else:
            real_error = "---"
        current_data.append(real_error)
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        table_data.append(current_data)
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXI\tERR_A\tERR_R\n" + "-" * tableline)
        for row in table_data:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root

def secant_mod(function, init_x, real_root, inc_x = 0.01, error_limit = 0.5, max_iteration = 20, summary = False, table = False):
    tableline = 55      # tamaño de las líneas de la tabla
    iteration = 0       # contador de iteración
    root = init_x       # raíces iniciales
    table_data = []     # matriz para los datos de la tabla
    # resumen de los datos de entrada
    if summary:
        summ = "\nFunction: " + str(getsourcelines(function)[0][0][:-1].split(":")[1][1:])
        summ += "\nInit X: " + str(init_x)
        summ += "\nIncrement: " + str(inc_x)
        summ += "\nReal Root: " + str(real_root)
        summ += "\nError Limit: " + str(error_limit)
        summ += "\nMax Iteration: " + str(max_iteration)
        summ += "\n"
        print(summ)
    while True:
        current_data = []   # lista para los datos de la iteración actual 
        old_root = root
        root = root - (inc_x * root * function(root)) / (function(root + inc_x*root) - function(root))
        iteration += 1
        current_data.extend([iteration, root])
        if root != 0:
            relative_error = abs((root - old_root) / root) * 100
            current_data.append(relative_error)
        # si se especifica una raíz real, se calcula el error real
        if real_root:
            real_error = abs((real_root - root) / real_root) * 100
        else:
            real_error = "---"
        current_data.append(real_error)
        # en este punto, ya se calcularon todos los datos de esta iteración, por lo que se añaden
        table_data.append(current_data)
        if relative_error < error_limit or iteration >= max_iteration:
            break
    # tabla con los datos de cada iteración
    if table:
        print("ITER\tXI\tERR_A\tERR_R\n" + "-" * tableline)
        for row in table_data:
            if real_root:
                print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t".format(\
                        row[0], row[1], row[2], row[3]))
            else:
                print("{}\t{:.3f}\t{:.3f}\t{}\t".format(\
                        row[0], row[1], row[2], row[3]))
        print("-" * tableline)
    # regresar la raíz encontrada
    return root
