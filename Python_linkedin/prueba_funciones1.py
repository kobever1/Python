def suma(a,b):
    return a + b


retval = suma(12,2)
print("el valor de la suma es {}".format(retval))


nombres = ["Paco", "Emilio", "Javier"]

for elemento in nombres:
    if elemento == "Emilio":
        continue
    print(elemento)

serie_1 = range(5,20,3)

print(list(serie_1))