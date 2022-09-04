import base64

micadena = b"hola munda"
micadenab64 = base64.b64encode(micadena)
print(micadenab64)