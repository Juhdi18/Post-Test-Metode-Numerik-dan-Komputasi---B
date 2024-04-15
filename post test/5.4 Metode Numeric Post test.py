import numpy as np
import matplotlib.pyplot as plt

def falsepos(func, xl, xu, iterasi, toleransi,eksak):
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
        epsA[i] = abs((xr[i] - xr[i-1])/ xr[i]) * 100 if xr[i] != 0 else 0
        
        
        if epsA[i] < toleransi:
            break
    return xr, epsT, epsA,fxr
    
def bisection(func, xl, xu, iterasi, toleransi,eksak):
    fxl = np.zeros(iterasi+1)
    fxu = np.zeros(iterasi+1)
    fxr = np.zeros(iterasi+1)
    xr = np.zeros(iterasi+1)
    epsT = np.zeros(iterasi+1)
    epsA = np.zeros(iterasi+1)

    for i in range(1, iterasi):
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
    return xr, epsT, epsA,fxr

def func(x):
    a,b,c,d,e,f = k
    return a*x**5 + b*x**4+ c*x**3 + d*x**2 + e*x + f

k = [0,0,-2.75, 18, -21, -12]
akar = np.roots(k)
xl = -1
xu = 0
iterasi = 10
toleransi = 1
eksak = akar[2].real
root, epsT, epsA,fxr = falsepos(func, xl, xu,iterasi,toleransi,eksak)
print(akar)

for i in range(len(root)):
    print("Iterasi {}: xr = {:.6f}, epsT = {:.6f}, epsA = {:.6f}".format(i+1, root[i], epsT[i], epsA[i]))

x = np.linspace(-10, 10, 400)
plt.plot(x, func(x), label='y = ax^5 + bx^4 + cx^3 + dx^2 + ex + f')
plt.axhline(0, color='black', linewidth=0.5)  # Menambahkan garis horizontal di y = 0
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik y = 5x^3 - 5x^2 + 6x + 2 dan y = 0')
plt.grid(True)
plt.legend()
plt.show()
