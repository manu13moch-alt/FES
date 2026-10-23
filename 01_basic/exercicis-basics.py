###
# ejercicios.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Manu Moya\nSabadell, Concordia")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
print(type(a))
b = 3.14159
print(type(b))
c = "Hola mundo"
print(type(c))
d = True
print(type(d))
e = None
print(type(e))

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print(int("12345"))
print(float("12345"))
print(int(3.99))

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

nombre="Manu"
edad=19
altura=1.78
print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura} metros.")

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
PI = None
PI = 3.14159
print(PI)
print("2. Redondea el número con round()")
print(round(PI))
print("3. Haz la división entera entre el número que te salió y el número 2")
print(round(PI) // 2)
print("4. El resultado debería ser 1")

print("--------------")

print("\nEjercicio 6: Conversor de temperatura")
print("Pide al usuario una temperatura en grados Celsius.")
grados_celsius = input("Introduce una temperatura en grados Celsius:")
print("Convierte ese valor a Fahrenheit con la fórmula: F = (C * 9/5) + 32")
grados_fahrenheit = (float(grados_celsius) * 9/5) + 32
print("Muestra ambos valores con un mensaje claro.")
print(f"Has introducido {grados_celsius} grados celsius, que son {grados_fahrenheit} grados fahrenheit")

### Completa aquí

print("--------------")

print("\nEjercicio 7: Calculadora de propina")
print("Pide el total de una cuenta y el porcentaje de propina.")
total_cuenta, porcentaje_propina = input("Introduce el total de una cuenta y el porcentaje de propina separado por un espacio:").split()
print(f"Total cuenta = {total_cuenta}\nPorcentaje propina = {porcentaje_propina}")
print("Calcula cuánto es la propina y el total final a pagar.")
propina = (float(porcentaje_propina)/100)*float(total_cuenta)
total_final = float(total_cuenta)+propina 
print("Muestra los resultados con 2 decimales.")
print(f"Total final a pagar = {total_final}€\nDel cual propina = {propina}€")

### Completa aquí

print("--------------")

print("\nEjercicio 8: Validador de contraseña simple")
print("Pide una contraseña al usuario.")
print("Comprueba si tiene al menos 8 caracteres.")
print("Muestra 'Contraseña válida' o 'Contraseña no válida'.")
contraseña = input("Introduce una contraseña:")
if len(contraseña) >= 8:
    print("Contraseña válida")
else:
    print("Contraseña no válida")

### Completa aquí