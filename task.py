import requests
from bs4 import BeautifulSoup

# URL del sitio web que queremos analizar
website = 'https://coinmarketcap.com/'

# Realizamos una solicitud GET a la URL
response = requests.get(website)
# Verificamos si la solicitud fue exitosa
if response.status_code != 200:
  raise Exception(f"No se ha podido conectar a la URL: {website}")

# Analizamos el contenido HTML de la respuesta
soup = BeautifulSoup(response.text, 'html.parser')

# Obtenemos el cuerpo de la tabla que contiene los datos
t_body = soup.tbody

# Obtenemos todos los elementos dentro del cuerpo de la tabla
data = t_body.contents

# Creamos un diccionario para almacenar los datos de ejemplo
example = {}

# Iteramos sobre los primeros 10 elementos de la tabla
for cell in data[:10]:
  # Extraemos el nombre y el precio de las criptomonedas
  name, precio = cell.contents[2:4]
  
  # Obtenemos el texto del nombre y el precio
  fixed_name = name.p.string
  fixed_price = precio.span.string
  
  # Almacenamos los datos en el diccionario
  example[fixed_name] = fixed_price
  
# Imprimimos el diccionario con los datos de ejemplo
print(example)
