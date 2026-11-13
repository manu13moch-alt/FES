# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Sant Cugat", "Sabadell", "Cerdanyola", "Matadepera", "Terrassa")
print(f"{ciutats[4]} malaraça {ciutats[1]} malapell")
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numeros = (1,2,3,4,3,3,2,7,8,3)
print(f"El numero 3 surt {numeros.count(3)} vegades a la tupla")
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(numros):
    l_numeros=list(numeros)
    l_numeros.sort()
    return tuple(l_numeros)
print(ordenar_tupla(numeros))