import json
from cupshelpers import Printer

from httplib2 import ProxiesUnavailableError

my_dict ={}

my_dict["nombre"]="miguel"
my_dict["apellido"]="arranz"


print(my_dict)
print(type(my_dict))

dict_json = json.dumps(my_dict)
print(type(dict_json))
print(dict_json)