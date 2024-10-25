
if __name__ == "__main__":

    #tipos de datos basicos

 entero=42
decimal=3.14
complejo = 2 + 3j
booleano = True
cadena ="Hola, Python!"
binario = bytes([50, 100, 150])

print("Tipos básicos:")
print("Entero:", entero)
print("Decimal:", decimal)
print("Complejo:", booleano)
print("Cadena:",cadena)
print("Binario:", binario, "\n")

# Estructura de datos avanzados

lista=[1,2,3,"cuatro"]
tupla=(5,6,7, "ocho")
conjunto ={9,10,"once", "doce"}
diccionario= {"clave1": "valor1", "clave2": 20}

print("Estructura avanzada:")
print("Lista:", lista)
print("Tupla:",tupla)
print("Conjunto:", conjunto)
print("Diccionario:", diccionario , "\n")

#otros tipos especiales
nulo=None                                   #Nonetype
rango=range(3)                              #range (eqivale a [0,1,2]

print("tipos especiales:")
print("Nulo:", nulo)
print("Rango",list(rango)) #convertimos en lista

#ejemplo de iteracion con el tipo range
print("\nIterando sobre el rango:")
for numero in rango:
    print(numero)


