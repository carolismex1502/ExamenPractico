def contar_letras(texto):
  
  conteo_letras = {}
  for letra in texto:
    if letra.isalpha():  
      conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
  return conteo_letras


mi_texto = ""
resultado = contar_letras(mi_texto)
print(resultado)

def reemplazar_letras (texto, letra_original, letra_nueva):
  return texto.replace(letra_original, letra_nueva)

nuevo_texto1= reemplazar_letras(mi_texto, "","").replace("","").replace("","")
print (nuevo_texto1)
