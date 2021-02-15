val = float(input("Qual número deseja verificar?"))

if (val % 3 == 0) and (val % 5 == 0):
    print("FizzBuzz")
else:
    print(val)
