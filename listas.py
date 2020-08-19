'''programa realizado por Yurany Zuluaga V Grupo 1 ACDI-VOCA'''
# Escriba un programa que tenga dos listas y que, a continuación, cree las
# siguientes listas(en las que no debe haber repeticiones):
# - Lista de palabras que aparecen en las dos listas.
# - Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# - Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# - Lista de palabras que aparecen en ambas listas.

# - Lista de palabras que aparecen en las dos listas.
ropa=["zapato", "camisa","gorra","pantalon","sombrero"]
productos=["gorra","sombrero","boina"]
aviso1=print("los elementos que coinciden son")
coincide= print(set(ropa) & set(productos))

# - Lista de palabras que aparecen en la primera lista, pero no en la segunda.
union=(set(ropa) | set(productos))
aviso2=print("los elementos que estan en la primera pero no en la segunda")
nocoinciden=print(set(ropa) - set(productos))

# - Lista de palabras que aparecen en la segunda lista, pero no en la primera.
aviso3=print("los elementos que estan en segunda pero no en la primera")
nocoinciden=print(set(productos) - set(ropa))

# - Lista de palabras que aparecen en ambas listas.
ropa=["zapato", "camisa","gorra","pantalon","sombrero"]
productos=["gorra","sombrero","boina"]
aviso1=print("los elementos que coinciden son")
coincide= print(set(ropa) & set(productos))

# - Lista de palabras que aparecen en ambas listas.
lista1 = set(["mueble", "comedor", "mesa","cuadro","televisor"])
lista2 = set(["cama", "televisor", "tocador","mesa","repiza","cajonera"])

final = lista1 & lista2
if len(final) > 0:
    print("hay {} elementos que coinciden".format(len(final)))
    print(final)
else:
    print("no hay repeticiones")



