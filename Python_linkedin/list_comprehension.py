def cal_cuad(numero):
    return numero**2

lista_num = [2,4,5,6,7]

list_compreh = [num**2 for num in lista_num]
print(list_compreh)

lista_cuad_pares = [cal_cuad(num) for num in lista_num if num % 2 == 0]
print(lista_cuad_pares)