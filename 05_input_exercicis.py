###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic=input("Entra el nom del tecnic responsable:")
nom_xarxa=input("Entra el nom de la xarxa en que està instal·lant:")
print(f"En {nom_tecnic} és el responsable de la instal·lació de la xarxa {nom_xarxa}")
# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_enllaç, velocitat_transmissió=input("Entra la longitud de l'enllaç(km) i la velocitat de transmissió:").split()
temps_propagacio=float(longitud_enllaç)/200000
temps_transmissio=8/float(velocitat_transmissió)
print(f"Per transmetre 1GB caldrien {temps_propagacio+temps_transmissio}")
# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina, preu_hora, preu_material=input("Entra el nombre d'hores de feina, el preu per hora i el preu del material:").split()
print(f"El cost total de la instal·lació és de {float(hores_feina)*float(preu_hora)+float(preu_material)}€")