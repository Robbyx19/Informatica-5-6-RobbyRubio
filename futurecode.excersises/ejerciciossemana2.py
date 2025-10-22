nombre = 'Mundo'
linea = ''
for _ in nombre:
    linea += '-'
print(nombre)
print(linea)  
   


# 2 
nombre = 'Mundo'
linea = ''
for _ in nombre:
    linea += '-'
    linea = '+'+ linea + '+'
    print (linea)
    print ('|' + nombre + '|')
    print (linea)