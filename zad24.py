# pronaci hrvatsku stranicu (npr. nogomet (liga, ljestvica), horoskop,
# banka (konverzija valuta), statisticki podaci) pa skrejpati

import requests
from bs4 import BeautifulSoup
import json

osnova='https://www.m.tecajna.info/kretanje-tecaja.php?'
nastavak_1='i=0&valuta=JPY'

URL=f'{osnova}{nastavak_1}'

podaci=requests.get(URL).content
sadrzaj=BeautifulSoup(podaci,'html.parser')

# print(sadrzaj)

script_tag = sadrzaj.find('script', text=lambda text: text and 'var line1=[' in text)

script_content = script_tag.get_text()

print (script_content)

start_index = script_content.find('var line1=[')
end_index = script_content.find('];', start_index) + 1

# Extract the JSON string
line1_data = script_content[start_index + len('var line1='):end_index].strip()
    
# Parse the JSON string to a Python list
line1 = json.loads(line1_data)
print(line1)
