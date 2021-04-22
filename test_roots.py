from metnum import bisection, fixpt, newton_raphson, falsepos, secant, secant_mod
from numpy import sin, exp, cos, sqrt, log

# Función original
f = lambda t: exp(sin(t*exp(-t))) - (t*exp(-t/10))/2 - (t**2)*sin(t*exp(-exp(-t)))
# Sumar exponencial de t y sacar logaritmo a todo (1ra raíz en 5 iteraciones).
g = lambda t: log(f(t) + exp(t))
# Derivada de función original
df = lambda t: exp(sin(exp(-t) * t) - t) * cos(exp(-t) * t) - exp(sin(exp(-t) * t) - t) * t * cos(exp(-t) * t) - 0.5 * exp(-0.1 * t) + 0.05 * exp(-0.1 * t) * t - 2 * t * sin(exp(-exp(-t))*t) - exp(-exp(-t)) * (t**2) * cos(exp(-exp(-t)) * t) - exp(-exp(-t) - t) * (t**3) * cos(exp(-exp(-t)) * t)

# Valores iniciales y raíz real
xl = 1; xu = 2; rr = 1.12745

# Métodos
print("BISECTION: {}".format(bisection(f, xl, xu, error_limit=0.001)))
print("FALSE POSITION: {}".format(falsepos(f, xl, xu, error_limit=0.001)))
print("FIXED POINT: {}".format(fixpt(g, xl, error_limit=0.001, max_iteration = 30)))
print("NEWTON-RAPHSON: {}".format(newton_raphson(f, df, xl, error_limit=0.001)))
print("SECANT: {}".format(secant(f, xl, xl-1, error_limit=0.001)))
print("MODIFIED SECANT: {}".format(secant_mod(f, xl, error_limit=0.001)))
