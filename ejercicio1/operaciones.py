
def suma(x,y):
    if (type(x) and type(y))==(int or float) :
        return x+y
    else:
        raise Exception('Solo se pueden sumar numeros')
def resta(x,y):
    if (type(x)and type(y))==(int or float) :
        return x-y
    else:
        raise Exception('Solo se pueden restar numeros')
def producto(x,y):
    if (type(x) and type(y))==(int or float) :
        return x*y
    else:
        raise Exception('Solo se pueden multiplicar numeros')
def division(x,y):
    if y==0:
        raise Exception('No se puede dividir por 0')
    elif (type(x) and type(y))==(int or float):
        return x/y
    else:
        raise Exception('Solo se pueden dividir numeros')
