import sys


print("dime dos numeros")

print("numero1")
try:
    numero1 = int(input())
except ValueError as e:
    print(e)
    sys.exit(1)

print("numero2")
numero2 = int(input())
#print("hola {}".format(nombre))
suma = numero1 + numero2

print(f"la suma es {suma}")