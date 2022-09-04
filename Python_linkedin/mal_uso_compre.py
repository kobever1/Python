lista_anidada = [[1,2],[3,4],[5,6]]

valores_lista = []
for i in lista_anidada:
    for j in i:
        valores_lista.append(j)

print(valores_lista)