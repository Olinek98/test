import requests
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get( orangutan)
text = surowe_info.text

# Cel:
# Lista linków (wszytkich).

# :) 
# :)) 
# przykładowe rozwiązanie:
lista = [
    "link1.pl",
    "link2.pl",
    "link3.pl"
]

# Przygotowanie:
lista_linii = text.split('</p>')

# Realizacja :)
linki = []
for linia in lista_linii:
    link = linia.replace('<p>', '')
    link = link.replace('- ', '')
    link = link.strip()
    
    if ' ' in link or '<' in link:
        continue
linki.append(link)
   
