def cal_cuad(numero):
    return numero**2



lista_num = [1,2,3,4,5]
# lista_cuad = []


# for num in lista_num:
#     cuadrado = cal_cuad(num)
#     lista_cuad.append(cuadrado)

# print(lista_cuad)

map_cuad = list(map(cal_cuad, lista_num))
print(map_cuad)