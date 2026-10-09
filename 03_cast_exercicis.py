###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets=input("Quants paquets ha rebut el router?")
print(int(paquets)+1200)
# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_connexió_Mbps=input("Entra la velocitat de connexió en Mbps:")
velocitat_connexió_MBps=float(velocitat_connexió_Mbps)/8
print(f"La velocitat de connexió en MBps es {velocitat_connexió_MBps}")