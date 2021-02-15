import math

a = float(input("Qual o valor de a?:"))
b = float(input("Qual o valor de b?:"))
c = float(input("Qual o valor de c?:"))

delta = (b**2) - (4*a*c)



if delta == 0:
    raizDelta = math.sqrt(delta)
    raiz1 = (-b + raizDelta)/ (2*a)
    print("a raiz desta equação é",raiz1)
if delta < 0:
    print("esta equação não possui raízes reais")
if delta > 0:
    raizDelta = math.sqrt(delta)
    raiz1 = (-b + raizDelta)/ (2*a)
    raiz2 = (-b - raizDelta)/ (2*a)
    #ordem crescente 
    if raiz1 < raiz2:
        print("as raízes da equação são",raiz1,"e",raiz2)
    else:
         print("as raízes da equação são",raiz2,"e",raiz1)
    



