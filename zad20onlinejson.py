import requests
import json

IP='192.168.1.1'
SM='24'
URL=f'https://networkcalc.com/api/ip/{IP}/{SM}'

response=requests.get(URL)

json_string=response.text

print(json_string)

dict_json=json.loads(json_string)

print(dict_json)
print(type(dict_json))

print(f"Zadana IP adresa: {dict_json['address']['cidr_notation']}")
print(f"Adresa mreze: {dict_json['address']['network_address']}")
print(f"Broadcast adresa: {dict_json['address']['broadcast_address']}")
print(f"Broj racunala u mrezi: {dict_json['address']['assignable_hosts']}")