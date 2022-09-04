from subprocess import list2cmdline


def saluda(nombre,apellido):
    print("hola {}, tu apellido es {}".format(nombre, apellido))

saluda ("carlos", "coliver")

calcular_cuadrado = lambda x: x ** 2
print(calcular_cuadrado(5))

lista_numeros = [1,2,3,4,5,6,7,8]

lista_pares = list(filter(lambda x: x %2 == 0, lista_numeros))
print(lista_pares)

nueva_lista = list(map(lambda x: x*10, lista_numeros))
print(nueva_lista)