import numpy as np
import matplotlib.pyplot as plt
import math as mt

def falsepos(func, xl, xu, iterasi, toleransi, eksak):
    fxl = np.zeros(iterasi+1)
    fxu = np.zeros(iterasi+1)
    fxr = np.zeros(iterasi+1)
    xr = np.zeros(iterasi+1)
    epsT = np.zeros(iterasi+1)
    epsA = np.zeros(iterasi+1)
    
    for i in range(iterasi):
        fxl[i] = func(xl)
        fxu[i] = func(xu)
        xr[i] = xu - (func(xu)*(xl-xu))/(func(xl)-func(xu))
        fxr[i] = func(xr[i])
        test = fxr[i] * fxl[i]
        
        if test < 0:
            xu = xr[i]
        elif test > 0:
            xl = xr[i]
        else:
            break
        
        epsT[i] = (abs((eksak - xr[i])) / 2)*100
        if i != 0:
            epsA[i] = abs((xr[i] - xr[i-1])/ xr[i]) * 100
        else:
            epsA[i] = np.inf
        
        if epsA[i] < toleransi:
            break
    return xr, epsT, epsA, fxr
    
def bisection(func, xl, xu, iterasi, toleransi, eksak):
    fxl = np.zeros(iterasi+1)
    fxu = np.zeros(iterasi+1)
    fxr = np.zeros(iterasi+1)
    xr = np.zeros(iterasi+1)
    epsT = np.zeros(iterasi+1)
    epsA = np.zeros(iterasi+1)

    for i in range(iterasi):
        fxl[i] = func(xl)
        fxu[i] = func(xu)
        xr[i] = (xl + xu) / 2
        fxr[i] = func(xr[i])
        test = fxr[i] * fxl[i]
        
        if test < 0:
            xu = xr[i]
        elif test > 0:
            xl = xr[i]
        else:
            break
        
        epsT[i] = (abs((eksak - xr[i])) / 2)*100
        if i != 0:
            epsA[i] = abs((xr[i] - xr[i-1])/ xr[i]) * 100
        else:
            epsA[i] = np.inf
        
        if epsA[i] < toleransi:
            break
    return xr, epsT, epsA, fxr

def func(x):
    return np.sin(x) - x**2

akar = 0.8767262345691
xl = 0.5
xu = 1
iterasi = 12
toleransi = 2
eksak = akar
root, epsT, epsA, fxr = bisection(func, xl, xu, iterasi, toleransi, eksak)
print(akar)
for i in range(len(root)):
    print("Iterasi {}: xr = {:.6f}, epsT = {:.6f}, epsA = {:.6f}".format(i+1, root[i], epsT[i], epsA[i]))

x = np.linspace(-10, 10, 400)
fx = func(x)
plt.plot(x, fx, label='y = ax^5 + bx^4 + cx^3 + dx^2 + e*sin(x) + f')
plt.axhline(0, color='black', linewidth=0.5)  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the Function')
plt.grid(True)
plt.legend()
plt.show()
