from numpy import array, diagflat, dot
from numpy.linalg import inv, eig
from math import sqrt
# TODO: documentar
def bisection(function, lower_x, upper_x, error_limit = 0.5, max_iteration = 20):
    iteration = 0
    root = 0
    while True:
        old_root = root
        root = (lower_x + upper_x) / 2
        iteration += 1
        if root != 0:
            relative_error = abs((upper_x - lower_x) / (upper_x + lower_x)) * 100
        test = function(lower_x) *  function(root)
        if test < 0:
            upper_x = root
        elif test > 0:
            lower_x = root
        else:
            relative_error = 0
        if relative_error < error_limit or iteration >= max_iteration:
            break
    return root

# TODO: documentar
def falsepos(function, lower_x, upper_x, error_limit = 0.5, max_iteration = 20):
    iteration = 0
    root = 0
    while True:
        old_root = root
        root = upper_x - (function(upper_x) * (lower_x - upper_x)) / (function(lower_x) - function(upper_x))
        iteration += 1
        if root != 0:
            relative_error = abs((root - old_root) / root ) * 100
        test = function(lower_x) *  function(root)
        if test < 0:
            upper_x = root
        elif test > 0:
            lower_x = root
        else:
            relative_error = 0
        if relative_error < error_limit or iteration >= max_iteration:
            break
    return root

# TODO: documentar
def fixpt(function, init_x, error_limit = 0.5, max_iteration = 20):
    iteration = 0
    root = init_x
    while True:
        old_root = root
        root = function(old_root)
        iteration += 1
        if root != 0:
            relative_error = abs((root - old_root) / root ) * 100

        if relative_error < error_limit or iteration >= max_iteration:
            break
    return root

# TODO: documentar
def newton_raphson(function, derivative, init_x, error_limit = 0.5, max_iteration = 20):
    iteration = 0
    root = init_x
    while True:
        old_root = root
        root = old_root - function(root) / derivative(root)
        iteration += 1
        if root != 0:
            relative_error = abs((root - old_root) / root) * 100
        if relative_error < error_limit or iteration >= max_iteration:
            break
    return root

# TODO: documentar
def secant(function, init_x, prev_x, error_limit = 0.5, max_iteration = 20):
    iteration = 0
    root = init_x
    prev_x = prev_x
    while True:
        old_root = root
        root = root - (function(root) * (prev_x - root)) / (function(prev_x) - function(root))
        prev_x = old_root
        iteration += 1
        if root != 0:
            relative_error = abs((root - old_root) / root) * 100
        if relative_error < error_limit or iteration >= max_iteration:
            break
    return root

# TODO: documentar
def secant_mod(function, init_x, inc_x = 0.01, error_limit = 0.5, max_iteration = 20):
    iteration = 0
    root = init_x
    while True:
        old_root = root
        root = root - (inc_x * root * function(root)) / (function(root + inc_x*root) - function(root))
        iteration += 1
        if root != 0:
            relative_error = abs((root - old_root) / root) * 100
        if relative_error < error_limit or iteration >= max_iteration:
            break
    return root

def convergence_criteria(matrix, priority = 0, converg_type = 0):
    if converg_type == 0:
        sufficient_criteria = required_criteria = len(matrix)
        for i in range(0,len(matrix)):
            # cond. necesaria: el término de la diagonal es mayor al resto
            aux = matrix[i].copy()
            d = aux.pop(i)
            aux.sort(reverse = True)
            if d > aux[0]:
                required_criteria -= 1
            # cond. suficiente: el término de la diagonal es mayor a la sumatoria del resto
            if matrix[i][i] >= sum(matrix[i]) - matrix[i][i]:
                sufficient_criteria -= 1
        if priority == 0 and required_criteria == 0:
            return True
        elif priority == 1 and sufficient_criteria == 0 and required_criteria == 0:
            return True
        else:
            return False
    elif converg_type == 1:
        # radio espectral
        m = array(matrix)
        d = diagflat(m.diagonal())
        lu = m - d
        spectral_ratio = max(eig(dot(inv(d), lu))[0])
        if spectral_ratio < 1:
            return True
        else:
            return False
    else:
        return False

def norm(a, prev):
    # norma entre 2 vectores (asumimos que tienen el mismo tamaño)
    summ = 0
    for i in range(len(a)):
        summ = summ + (a[i] - prev[i]) ** 2
    return sqrt(summ)

# TODO: Añadir el número de iteraciones a la salida.
# TODO: Parámetro para ignorar total o parcialmente el criterio de convergencia.
def jacobi(a, b, x_prev, max_iter = 25, tolerance = 0.0005, priority = 0, converg_type = 0):
    if convergence_criteria(a, priority, converg_type):
        k = 0
        while True:
            x_aprox = []
            for i in range(0,len(a)):
                Rx = 0
                for j in range(0,len(a)):
                    if j != i:
                        Rx = Rx + a[i][j] * x_prev[j]
                x_aprox.append((b[i] - Rx) / a[i][i])
            if k > max_iter or norm(x_aprox, x_prev) < tolerance:
                print(k)    # debug
                break
            else:
                x_prev = x_aprox
                k += 1
            print(x_aprox)  # debug
        return x_aprox
    else:
        return None

# TODO: Añadir el número de iteraciones a la salida.
# TODO: Parámetro para ignorar total o parcialmente el criterio de convergencia.
def gauss_seidel(a, b, x_prev, max_iter = 25, tolerance = 0.0005):
    if convergence_criteria(a):
        k = 0
        while True:
            x_aprox = x_prev.copy()
            for i in range(0,len(a)):
                Rx = 0
                for j in range(0,len(a)):
                    if j != i:
                        Rx = Rx + a[i][j] * x_aprox[j]
                x_aprox[i] = (b[i] - Rx) / a[i][i]
            if k > max_iter or norm(x_aprox, x_prev) < tolerance:
                print(k)    # debug
                break
            else:
                x_prev = x_aprox
                k += 1
            print(x_aprox)  # debug
        return x_aprox
    else:
        return None
