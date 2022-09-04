def divide(numerador, denominador):
    try:
        return(numerador/denominador)
    except Exception:
        raise Exception("errorDivision")

try:
    resultado = divide(10,0)
    print(resultado)
except Exception:
    print("ha habido un error en la funcion")