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

def func(x):
    return 7 * np.sin(x) * np.exp(-x) - 1

def diffunc(x):
    return -7*(np.e**-x)*np.sin(x)+7*(np.e**-x)*np.cos(x)

def mode(m):
    global x, iterasi, toleransi, eksak, epsT, epsA, dx
    if m == 1:
        x[1] = 0.3
        root, epsT, epsA = newrap(func, diffunc, x, iterasi, toleransi, eksak)
    elif m == 2: 
        x[1] = 0.4
        x[0] = 0.5
        root, epsT, epsA = secant(func, x[0], x[1], iterasi, toleransi, eksak)
    else:
        x[1] = 0.3
        dx = 0.01
        root, epsT, epsA = modsecant(func, dx, x, iterasi, toleransi, eksak)
    return root, epsT, epsA

iterasi = 10
toleransi = 1
eksak = 0.17018
x = np.zeros(iterasi, dtype=float)
epsT = np.zeros(iterasi+1, dtype=float)
epsA = np.zeros(iterasi+1, dtype=float)
dx = 0  # Inisialisasi dx

root, epsT, epsA = mode(3)

for i in range(1, len(root)):
    print("Iterasi {}: x = {}, epsT = {}, epsA = {}".format(i, root[i], epsT[i], epsA[i]))

xp = np.linspace(-1, 10, 400)
fx = func(xp)
plt.plot(xp, fx, label='y = 5x^3 - 5x^2 + 6x + 2')
plt.axhline(0, color='black', linewidth=0.5)  # Menambahkan garis horizontal di y = 0
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik y = 5x^3 - 5x^2 + 6x + 2 dan y = 0')
plt.grid(True)
plt.legend()
plt.show()
