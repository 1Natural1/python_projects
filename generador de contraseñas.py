import random
print ("Este es su generador de credenciales, donde podra elegir entre si quiere minusculas, mayusculas y caracteres especiales, y hasta la longitud! (siempre se recomienda la mayor variedad de los distintos caracteres, pero igual puedes elegir si en donde quieres ingresar la credencial no se admiten ciertos caracteres, como en un PIN.")
minusculas = input("Desea minusculas?(recomendable) s/n (escriba entre comillas si se encuentra en python 2): ")
mayusculas = input("Desea mayusculas?(recomendable) s/n (escriba entre comillas si se encuentra en python 2): ")
especiales = input("Desea caracteres especiales?(recomendable) s/n (escriba entre comillas si se encuentra en python 2): ")
numeros = input("Desea numeros?(recomendable) s/n (escriba entre comillas si se encuentra en python 2): ")
def minuscula_aleatoria():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    salto_aleatorio = random.randint (0,len (alfabeto)-1)
    minuscula = alfabeto[salto_aleatorio]
    return minuscula

def mayuscula_aleatoria():
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salto_aleatorio = random.randint (0,len (alfabeto)-1)
    mayuscula = alfabeto[salto_aleatorio]
    return mayuscula

def especial_aleatorio():
    caracteres = "!#$%&/*+@"
    salto_aleatorio = random.randint (0,len (caracteres)-1)
    caracter_especial = caracteres[salto_aleatorio]
    return caracter_especial

def numero_aleatorio():
    caracteres = "0123456789"
    salto_aleatorio = random.randint (0,len (caracteres)-1)
    numero = caracteres[salto_aleatorio]
    return numero

def credencial_aleatoria(longitud):
    credencial = ""
    for i in range (1,longitud):
        while len(credencial) < longitud:
            elegir_numero = 0, 1, 2, 3
            numero_random = random.choice(elegir_numero)
            if minusculas == "s":
                if numero_random == 0:
                    credencial += minuscula_aleatoria()
            if mayusculas == "s":
                if numero_random == 1:
                    credencial += mayuscula_aleatoria()
            if especiales == "s":
                if numero_random == 2:
                    credencial += especial_aleatorio()
            if numeros == "s":
                if numero_random == 3:
                    credencial +=  numero_aleatorio()
    return credencial
print (credencial_aleatoria(int(input("Que longitud de credencial desea? (inserte en forma numerica. Ej: 1): "))))