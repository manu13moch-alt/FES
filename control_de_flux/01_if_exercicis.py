###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
#RSSI = int(input("Entra el nivell de senyal Wi-Fi (RSSI) en dBm: "))
#if RSSI >= -50:
#    print("La cobertura és excel·lent")
#elif RSSI >= -67:
#    print("La cobertura és bona")
#elif RSSI >= -75:
#    print("La cobertura és feble")
#else:
#    print("La cobertura és molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
#pot_optica = int(input("Entra la potència òptica rebuda en dBm:"))
#if  -8 < pot_optica:
#    print("La potencia és massa alta")
#elif -27 <= pot_optica:
#    print("La potencia és acceptable")
#else:
#    print("La potencia és massa baixa")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
#dades = int(input("Introdueix el consum de dades mòbils:"))
#if dades < 0:
#    print("Valor de dades no vàlid")
#elif dades <= 20:
#    print("El consum és dins del límit")
#else:
#    print(f"El consum ha superat el limit en {dades - 20} GB")


# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
#Encès_LOS = input("L'indicador LOS del terminal òptic està encès? (sí/no): ")
#Encès_Internet = input("L'indicador d'Internet del router està encès? (sí/no): ")
#if Encès_LOS == "sí" and Encès_Internet == "sí":
#    print("La connexió sembla funcionar correctament")
#elif Encès_LOS == "sí" and Encès_Internet == "no":
#    print("Cal comprovar el servei del proveïdor")
#elif Encès_LOS == "no" and Encès_Internet == "sí":
#    print("Cal revisar el cable de fibra")
#else:
#    print("Cal revisar el cable de fibra i comprovar el servei del proveïdor")
# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
#bateria = int(input("Introdueix el percentatge de bateria disponible al SAI:"))
#if bateria<=100 and bateria>=0:
#    if bateria >=50:
#        print("Suficient")
#    elif bateria >=20:
#        print("baix")
#    else:
#        print("crític")
#else:
#    print("nivell fota de rang")
# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
#latencia = int(input("Introdueix la latència en mil·lisegons:"))
#perduts = int(input("Introdueix el percentatge de paquets perduts:"))
#if latencia < 0 or perduts < 0 or perduts > 100:
#    print("Valor de latència o pèrdua no vàlid")
#elif latencia <= 30 and perduts <= 1:
#    print("La connexió és excel·lent")
#elif latencia <= 80 and perduts <= 3:
#    print("La connexió és bona")
#elif latencia <= 150 and perduts <= 5:
#    print("La connexió és acceptable")
#else:
#    print("La connexió és deficient")

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
#pla = input("Introdueix el tipus de pla (bàsic o plus): ")
#consum = int(input("Introdueix el consum mensual en GB: "))
#if pla == "bàsic":
#    cost = 10
#    if consum > 10:
#        cost = cost + (consum-10)*1.5
#   print(f"El cost és de {cost}€")
#elif pla == "plus":
#    cost = 20
#    if consum > 30:
#        cost = cost + (consum-30)*0.75
#    print(f"El cost és de {cost}€")
#else:
#    print("Pla no vàlid")
# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
#actiu = input("El compte està actiu? (sí/no): ")
#contrasenya = input("La contrasenya és correcta? (sí/no): ")
#if actiu == "sí":
#    print("El compte està actiu")
#else:
#    print("El compte no està actiu")
#if contrasenya == "sí":
#    print("La contrasenya es correcte")
#else:
#    print("La contrasenya no és correcte")
#if contrasenya =="sí" and actiu == "sí":
#    verificació = input("La doble verificació es correcte? (sí/no): ")
#    if verificació == "sí":
#        print("Accés permés")

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
#router_encès = input("El router està encès? (sí/no): ")
#if router_encès == "no":
#   print("Cal encendre el router")
#elif "no" == input("LOS encès? (sí/no)"):
#    print("Cal revisar l'estat de la fibra")
#elif "no" == input("Internet encès? (sí/no)"):
#    print("Cal contactar amb el proveïdor")
#else:
#    print("La connexió funciona correctament")


# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
servei_crític = input("La incidència afecta un servei crític? (sí/no): ")
nombre_usuaris=int(input("introdueix el nombre d'usuaris:"))
alternativa=input("hi ha una alternativa disponible? (sí/no): ")
if nombre_usuaris<0:
    print("Nombre d'usuaris no vàlid")
elif servei_crític == "sí" and nombre_usuaris >= 50 and alternativa == "no":
    print("Prioritat crítica")
    prioritat_critica = 1
if servei_crític == "sí" or nombre_usuaris >= 10:
    print("Prioritat alta")
    prioritat_alta = 1
else:
    print("Prioritat baixa")
    prioritat_baixa = 1