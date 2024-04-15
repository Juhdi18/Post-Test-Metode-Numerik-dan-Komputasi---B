import matplotlib.pyplot as plt
import numpy as np

def newrap(func, diffunc, x, iterasi, toleransi, eksak):
    for i in range(1, iterasi-1):
        x[i+1] = x[i] - (func(x[i])/diffunc(x[i]))
        x[i] = x[i+1] 
        epsT[i] = abs((eksak - x[i])/eksak) * 100
        epsA[i] = abs((x[i] - x[i-1]) / x[i]) * 100 if i != 0 else 0
        if epsA[i] < toleransi:
            break
    return x, epsT, epsA

def secant(func, x0, x1, iterasi, toleransi, eksak):
    x = np.zeros(iterasi+1, dtype=float)
    x[0] = x0
    x[1] = x1
    epsT = np.zeros(iterasi+1, dtype=float)
    epsA = np.zeros(iterasi+1, dtype=float)
    for i in range(1, iterasi):
        x[i+1] = x[i] - (((func(x[i]))*(x[i-1]-x[i]))/(func(x[i-1])-func(x[i])))
        epsT[i] = abs((eksak - x[i])/eksak) * 100
        epsA[i] = abs((x[i] - x[i-1]) / x[i]) * 100 if x[i] != 0 else 0
        if epsA[i] < toleransi:
            break
    return x, epsT, epsA

def modsecant(func, dx, x, iterasi, toleransi, eksak):
    modval = np.zeros(iterasi+1, dtype=float)
    for i in range(1, iterasi-1):
        modval[i] = x[i]*dx + x[i]
        x[i+1] = x[i] - (dx*x[i]*func(x[i]))/(func(modval[i])-func(x[i]))
        x[i] = x[i+1] 
        epsT[i] = abs((eksak - x[i])/eksak) * 100
        epsA[i] = abs((x[i] - x[i-1]) / x[i]) * 100 if i != 0 else 0
        if epsA[i] < toleransi:
            break
    return x, epsT, epsA

def bisection(func, xl, xu, iterasi, toleransi,eksak):
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
        epsA[i] = abs((xr[i] - xr[i-1])/ xr[i]) * 100 if xr[i] != 0 else 0
        
        
        if epsA[i] < toleransi:
            break
    return xr, epsT, epsA
def func(x):
    return -2*x**6-1.5*x**4 + 10*x +2

def diffunc(x):
    return -2*6*x**5-1.5*4*x**3 + 10

def mode(m):
    global x, iterasi, toleransi, eksak, epsT, epsA, dx
    if m == 1:
        x[1] = 1
        root, epsT, epsA = newrap(func, diffunc, x, iterasi, toleransi, eksak)
    elif m == 2: 
        x[1] = 1
        x[0] = 0
        root, epsT, epsA = secant(func, x[0], x[1], iterasi, toleransi, eksak)
    elif m ==3:
        x[1] = 1
        dx = 0.01
        root, epsT, epsA = modsecant(func, dx, x, iterasi, toleransi, eksak)
    elif m== 4:
        xl = 0
        xu = 1
        root, epsT, epsA = bisection(func, xl, xu, iterasi, toleransi, eksak)
    return root, epsT, epsA

iterasi = 10
toleransi = 5
eksak = 1.3212754800477
#eksak = -0.1997485011916
x = np.zeros(iterasi, dtype=float)
epsT = np.zeros(iterasi+1, dtype=float)
epsA = np.zeros(iterasi+1, dtype=float)
dx = 0  

root, epsT, epsA = mode(3)

for i in range(1, len(root)):
    print("Iterasi {}: x = {}, epsT = {}, epsA = {}".format(i, root[i], epsT[i], epsA[i]))

xp = np.linspace(-100, 100, 400)
fx = func(xp)
plt.plot(xp, fx, label='y = 5x^3 - 5x^2 + 6x + 2')
plt.axhline(0, color='black', linewidth=0.5)  # Menambahkan garis horizontal di y = 0
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik y = 5x^3 - 5x^2 + 6x + 2 dan y = 0')
plt.grid(True)
plt.legend()
plt.show()
