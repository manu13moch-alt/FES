###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_router="Juanjo Caminos"
ubi_router="Biblioteca"
estat_router="Apagat"
print(f"El router {nom_router} es troba a {ubi_router} i està {estat_router}")
# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
total_GB=256
consumits_GB=172
print(f"Queden {total_GB-consumits_GB}GB disponibles")