def maximo(x ,y, z):   #20,30,10
    if x > y and x > z:
        return x
    else:
        if y > x and y > z:
            return y
        else:
            if z > x and z > y:
                return z
            else:
                return x  # os parametros são todos iguais