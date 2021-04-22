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

def convergence_criteria(a):
    sufficient_criteria = required_criteria = len(a)
    for i in range(0,len(a)):
        # cond. necesaria: el término de la diagonal es mayor al resto
        aux = a[i].copy()
        d = aux.pop(i)
        aux.sort(reverse = True)
        if d > aux[0]:
            required_criteria -= 1
        # cond. suficiente: el término de la diagonal es mayor a la sumatoria del resto
        if a[i][i] >= sum( [ abs(ele) for ele in a[i] ] ) - a[i][i]:
            sufficient_criteria -= 1
    if sufficient_criteria == 0 and required_criteria == 0:
        return True
    else:
        return False

def norm(a, prev):
    # norma entre 2 vectores (asumimos que tienen el mismo tamaño)
    summ = 0
    for i in range(len(a)):
        summ = summ + (a[i] - prev[i]) ** 2
    return sqrt(summ)

def jacobi(a, b, x_prev, max_iter = 25, tolerance = 0.0005):
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
            break
        else:
            x_prev = x_aprox
            k += 1
    return x_aprox
