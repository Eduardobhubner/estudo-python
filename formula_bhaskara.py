import math

a = float(input("Qual o valor de A?:"))
b = float(input("Qual o valor de B?:"))
c = float(input("Qual o valor de C?:"))

delta = (b**2) - (4*a*c)
raizDelta = math.sqrt(delta)

raiz1 = ((-(b)) + raizDelta)/2*a
raiz2 = ((-(b)) - raizDelta)/2*a

if delta == 0:
    print("A equação contem apenas uma raiz:",raiz1)
if delta < 0:
    print("A equação não contem raizes reais")
if delta > 0:
    print("A equação contem duas raizes:",raiz1,"e",raiz2)



