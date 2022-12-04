import pdb

pdb.set_trace()


lista = [[2,4,1], [1,2,3,4,5,6,7,8], [100,250,43]]

listaMaximos = [e for i in lista for e in i if e==max(i)]
print (listaMaximos)