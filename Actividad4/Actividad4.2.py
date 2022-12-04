def numerosPrimos(n):
    return n%2==1
   
                        
lista =  [3, 4, 8, 5, 5, 22, 13]

listaPrimos = list(filter(numerosPrimos,lista))

print(listaPrimos)