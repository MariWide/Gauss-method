from math import *

def f(x):
    return x**2

def lejandr(n, x):
    Px = [1, x]
    for i in range(2, n + 1):
        Px.append((2*i-1)/i * x * Px[i - 1] - (i - 1)/i * Px[i - 2])
    return n/(1 - x**2)*(Px[n-1] - x*Px[n])  
    
def val_x(i, n):
    x = cos(pi*(4*i - 1)/(4*n + 2))
    return x

def w(x, P):
    return 2/((1 - x**2)*P**2)
 

point = int(input('Порядок точности '))  
xi = []
wi = []

for i in range(1, point + 1):
    xi.append(val_x(i, point))
    wi.append(w(val_x(i, point), lejandr(point, val_x(i, point))))
    
integral = wi[0] * f(xi[0])

for i in range(1, point):
    integral += wi[i] * f(xi[i])
    
print(f'Интеграл на отрезке [-1, 1] равен {integral}')    