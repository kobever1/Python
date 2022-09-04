


def cal_cuad(numero):
    return numero**2



lista_num = [1,2,3,4,5,6,7,8]
lista_pares = []

for num in lista_num:
    if (cuadrado := cal_cuad(num)) %2 == 0:
        lista_pares.append(cuadrado)
        print(f"el cuadrado de {num} es {cuadrado}, es numero par")
    else:
        print(f"el cuadrado de {num} es {cuadrado}, es numero impar")

print(lista_pares)    

pares_comprehension = [cuadrado for num in lista_num if (cuadrado := cal_cuad(num)) %2 == 0]
print(pares_comprehension)