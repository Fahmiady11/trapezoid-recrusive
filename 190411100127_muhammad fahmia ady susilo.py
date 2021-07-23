def rumus(x):
    return 1/(1+x**2)
def trapezoid(x, y, z):
    integerasi = rumus(x)+rumus(y)
    h=(y-x)/z
    i=1
    while i<z :
        integerasi = integerasi+(2*rumus(x+i*h))
        i+=1
    integerasi =integerasi * (h)/2
    return integerasi
print("RUMUS : 1/(1+x**2)")
batasBawah = int(input("Masukkan batas bawah :"))
batasAtas = int(input("masukkan batas atas :"))
Interval = int(input("masukkan interval :"))
result = trapezoid(batasBawah,batasAtas, Interval)
print("hasil integrasi metode trapezoid :%0.6f" % (result))
