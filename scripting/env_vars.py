import os

os.environ["MIPRUEBA"] = "fijadainternamente"
os.environ.clear()
miprueba = os.environ.get('MIPRUEBA')


#print(os.environ.get('HOME'))
if not os.environ.get('MIPRUEBA'):
    print("la variable no existe")
else:
    print(os.environ.get('MIPRUEBA'))