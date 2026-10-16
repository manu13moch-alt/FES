###
# EXERCICIS
###

print("Exercici 1: Comparar nombres")
# Donats els nombres:
nombre_a = 8
nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.
print(f"més gran: {nombre_a > nombre_b}")
print(f"més petit: {nombre_a < nombre_b}")
print(f"igual: {nombre_a == nombre_b}")

print("Exercici 2: Comparar cadenes de text")
# Donades les cadenes:
paraula_a = "Hola"
paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.
print(f"Iguals: {paraula_a == paraula_b}\nVeiem que python sí distingeix")

# Exercici 3: Connexió de xarxa
# Donats els valors booleans:
router_encès = True
connexio_activa = False
# Crea una variable anomenada xarxa_disponible que sigui True només si el
# router està encès i la connexió està activa. Mostra'n el resultat.
xarxa_disponible = False
if router_encès == 1 and connexio_activa == 1:
    xarxa_disponible = True
print(f"La xarxa està disponible: {xarxa_disponible}")

# Exercici 4: Avisos pendents
# Donats els valors booleans:
actualitzacio_disponible = False
alerta_critica = True
# Crea una variable anomenada cal_avisar que sigui True si hi ha una
# actualització disponible o una alerta crítica. Mostra'n el resultat.
cal_avisar = False
if actualitzacio_disponible == 1 or alerta_critica == 1:
    cal_avisar = True
print(f"Cal avisar:{cal_avisar}")

# Exercici 5: Accés a un compte
# Donats els valors booleans:
compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
# Crea una variable anomenada accés_permes que sigui True si el compte està
# actiu, la contrasenya és correcta, el compte no està bloquejat i, a més,
# el codi és correcte o el dispositiu és de confiança. Fes servir and, or i not.
# Mostra'n el resultat.
accés_permes = compte_actiu and contrasenya_correcta and not compte_bloquejat and (codi_correcte or dispositiu_de_confiança)
print(f"Accés permés:{accés_permes}")