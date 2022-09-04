numerador = 10
denominador = 0

try:
    resultado = numerador / denominador
    print(resultado)
except Exception as e:
    print("Algo ha fallado")
    print(e)

