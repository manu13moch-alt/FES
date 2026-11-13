###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio} {nom}")
saludar_a("Manu")
# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    if numero%2==0:
        parell=True
    else:
        parell=False
    return parell
print(es_parell(9))
# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma=0
    for numero in numeros:
        suma += numero
    mitjana=suma/len(numeros)
    return mitjana
print(mitjana([1,2,3,4,5]))
# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    suma=0
    for numeros in args:
        suma+=numeros
    return suma
print(sumar_tot(1,2,3,4))
print(sumar_tot(2,4,5))
# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero,limit=10):
    for num in range(1,limit+1):
        print(f"{numero}x{num}={numero*num}")
taula_multiplicar(8)
# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
    for clau,valor in kwargs.items():
        print(f"{clau}:{valor}")
mostrar_perfil(nom="Manu",edat="19",grau="Telecos")
# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(num):
    while num<1:
        num=int(input("Entra un numero positiu:"))
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    return factorial
def llista_max(numeros):
    max=0
    for numero in numeros:
        if numero > max:
            max = numero
    print(f"El màxim és {max}")
print(factorial(4))
print(llista_max([5,56,43,2,-4,77]))
# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    comptador=0
    vocals="aàeèéiíoòóuú"
    for lletr in text.lower():
        if lletr in vocals:
            comptador+=1
    return comptador
print(comptar_vocals("HolaA"))

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    max=numeros[0]
    min=numeros[0]
    for numero in numeros:
        if numero > max:
            max = numero
        if numero < min:
            min = numero
    return max,min
max,min=minim_i_maxim([1,3,45,-23,4])
print(f"max={max} i min={min}")
# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
    text_min=text.lower()
    return text_min == text_min[::-1]
print(es_palindrom("Anna"))
print(es_palindrom("Juan"))
