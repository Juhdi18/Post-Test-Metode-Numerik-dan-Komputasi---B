import matplotlib.pyplot as plt
import numpy as np

def newrap(func,diffunc,x, iterasi, toleransi,eksak):
    for i in range(1, iterasi-1):
        x[i+1] = x[i] - (func(x[i])/diffunc(x[i]))
        x[i] = x[i+1] 
        epsT[i] = abs((eksak - x[i])) * 100
        epsA[i] = abs((x[i] - x[i-1]) / x[i]) * 100 if i != 0 else 0
        if epsA[i] < toleransi:
            break
    return x,epsT, epsA

def secant(func, x0, x1, iterasi, toleransi, eksak):
    x = np.zeros(iterasi+1, dtype=float)
    x[0] = x0
    x[1] = x1
    epsT = np.zeros(iterasi+1, dtype=float)
    epsA = np.zeros(iterasi+1, dtype=float)
    for i in range(1, iterasi):
        x[i+1] = x[i] - (((func(x[i]))*(x[i-1]-x[i]))/(func(x[i-1])-func(x[i])))
        epsT[i] = abs((eksak - x[i])) * 100
        epsA[i] = abs((x[i] - x[i-1]) / x[i]) * 100 if x[i] != 0 else 0
        if epsA[i] < toleransi:
            break
    return x, epsT, epsA

def modsecant(func, dx, x, iterasi, toleransi, eksak) :
    modval = np.zeros(iterasi+1, dtype=float)
    for i in range(1, iterasi-1):
        modval[i] = x[i]*dx + x[i]
        x[i+1] = x[i] - (dx*x[i]*func(x[i]))/(func(modval[i])-func(x[i]))
        x[i] = x[i+1] 
        epsT[i] = abs((eksak - x[i])) * 100
        epsA[i] = abs((x[i] - x[i-1]) / x[i]) * 100 if i != 0 else 0
        if epsA[i] < toleransi:
            break
    return x,epsT, epsA

def func(x):
    a,b,c,d,e,f = k
    return a*x**5 + b*x**4+ c*x**3 + d*x**2 + e*x + f

def diffunc(x):
    a,b,c,d,e,f = k
    return 5*a*x**4 + 4*b*x**3 + 3*c*x**2 + 2*d*x**1 + e

k = [0,0,1, -6, 11, -6.1]
akar = np.roots(k)
iterasi = 10
toleransi = 0.00005
eksak = akar[0].real
x = np.zeros(iterasi, dtype=float)
epsT = np.zeros(iterasi+1, dtype=float)
epsA = np.zeros(iterasi+1, dtype=float)

x[1] = 3.5
root, epsT, epsA= newrap(func,diffunc,x,iterasi,toleransi,eksak)
#x[1] = 2.5
#x[0] = 3.5
#root, epsT, epsA= secant(func,x[0],x[1],iterasi,toleransi,eksak)
#x[1] = 2.5
#dx = 0.01
#root, epsT, epsA= modsecant(func,dx,x,iterasi,toleransi,eksak)
print(akar)

for i in range(1, len(root)):
    print("Iterasi {}: x = {}, epsT = {}, epsA = {}".format(i, root[i], epsT[i], epsA[i]))

xp = np.linspace(-10, 10, 400)
fx = func(xp)
plt.plot(xp, fx, label='y = 5x^3 - 5x^2 + 6x + 2')
plt.axhline(0, color='black', linewidth=0.5)  # Menambahkan garis horizontal di y = 0
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik y = 5x^3 - 5x^2 + 6x + 2 dan y = 0')
plt.grid(True)
plt.legend()
plt.show()