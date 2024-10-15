spanish_letter_frequencies = {
    'A': 12.53,
    'B': 1.42,
    'C': 4.68,
    'D': 5.86,
    'E': 13.68,
    'F': 0.69,
    'G': 1.01,
    'H': 0.70,
    'I': 6.25,
    'J': 0.44,
    'K': 0.02,
    'L': 4.97,
    'M': 3.15,
    'N': 6.71,
    'Ñ': 0.31,
    'O': 8.68,
    'P': 2.51,
    'Q': 0.88,
    'R': 6.87,
    'S': 7.98,
    'T': 4.63,
    'U': 3.93,
    'V': 0.90,
    'W': 0.02,
    'X': 0.22,
    'Y': 0.90,
    'Z': 0.52
}

def contar_letras(texto):
  
  conteo_letras = {}
  for letra in texto:
    letra = letra.upper()
    if letra.isalpha():  
      conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
  return sort_dict(conteo_letras)

def sort_dict(dic):
  return sorted(dic.items(), key=lambda item: item[1])

mi_texto = """

"""

print("Texto:")
resultado = contar_letras(mi_texto)
print(resultado)

print("Espanol:")
print(sort_dict(spanish_letter_frequencies))

reemplazar = {
  'N': 'a',
  





}

def reemplazar_letras (texto):
  texto = texto.upper()
  for item in reemplazar.items():
    texto = texto.replace(item[0], item[1])
  return texto

nuevo_texto1= reemplazar_letras(mi_texto,)
print (nuevo_texto1)
