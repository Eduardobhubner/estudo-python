var1 = float(input("Número 1:")) #1
var2 = float(input("Número 2:")) #2
var3 = float(input("Número 3:")) #3

if (var1 > var2) or (var1 > var3) or (var2 > var3):
    print("não está em ordem crescente")
else:
    print("crescente")
