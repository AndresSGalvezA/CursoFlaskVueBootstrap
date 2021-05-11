string = "El dijo: 'sss'"
string2 = "El dijo: \"sss\""
parrafo = '''
Esto es un texto
en varias lineas... :) '''
print(string)
print(string2)
print(parrafo)
parrafo = parrafo.replace("Esto", "Aquello", 1) # El ultimo parametro es el numero de coincidencias que se desean reemplazar (opcional)
print(parrafo)
print(parrafo.count("a"))