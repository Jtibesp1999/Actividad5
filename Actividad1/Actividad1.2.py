try:
    with open('hellomundo.txt', mode = 'w+', encoding= 'utf-8') as archivo:

        archivo.write('Hello World.\n')
        archivo.write('Hola Mundo.')
        
        posicion = 0
        archivo.seek(posicion)
        
        linea1 = archivo.readline()
        linea2 = archivo.readline()
        

except Exception as e:
    print (f'Se ha producido el error {e}.')

finally:
    print('Fin :)')
    