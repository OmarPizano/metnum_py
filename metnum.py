from inspect import getsourcelines
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
