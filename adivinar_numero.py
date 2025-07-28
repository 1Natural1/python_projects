import random
def elegir_numero(pregunta):
    while True:
        try:
            numero = input ("Elija un numero" + pregunta)
            if numero.isnumeric():
                return numero
            else:
                print ("Formato invalido")
        except ValueError:
            print ("Formato invalido.")
def respuesta_sn(pregunta):
    while True:
        respuesta = input (pregunta + "(s/n): ")
        if respuesta in ("s", "n"):
            return respuesta
        else:
            print ("Inserte una respuesta valida")
def intentos(pregunta):
    while True:
        intentos = input (pregunta)
        if intentos.isnumeric() and int (intentos) > 0:
            return intentos
        else:
            print ("Inserte valor valido")
def cercania(numeroAdivinado, numero):
    numeroAdivinado_int = int (numeroAdivinado)
    numero_int = int (numero)
    diferencia = abs (numeroAdivinado_int - numero_int)
    if diferencia == 1:
        return "Estas en fuego!"
    if diferencia <= 3:
        return "Estas cerca!"
    if diferencia >= 4:
        return "Lejos!"

def numero_adivinado(minum, maxnum):
    while True:
        try:
            numero = input ("Adivina un numero: ")
            if numero.isnumeric() and int(minum)<=int(numero)<=int(maxnum):
                return numero
            else: 
                print ("Inserte un numero valido")
        except ValueError:
            print ("Inserte un numero valido")
def adivinar_numero():
    numero_minimo = elegir_numero(" minimo: ")
    numero_maximo = elegir_numero(" maximo: ")
    sn_numIntentos = respuesta_sn("Desea un numero de intentos maximos?: ")
    numero_aleatorio = random.randint(int (numero_minimo), int (numero_maximo))
    numero_intentos = 0
    if sn_numIntentos == "s":
        numeros_intentos_maximos = intentos ("Cuantos intentos maximos quiere: ")
        while True:
            numero_elejido = numero_adivinado(numero_minimo, numero_maximo)
            numero_intentos += 1
            if int(numero_elegido) != numero_aleatorio:
                print (cercania(numero_elejido, numero_aleatorio))
            else:
                return "Ganaste En " + str (numero_intentos) + " intentos! Si era el " + str (numero_aleatorio) 
            if numero_intentos == int (numeros_intentos_maximos):
                return "Lo siento, Perdiste! Era el " + str (numero_aleatorio)
    else:
        while True:
            numero_elejido = numero_adivinado(numero_minimo, numero_maximo)
            numero_intentos += 1
            if int(numero_elejido) != numero_aleatorio:
                print (cercania(numero_elejido, numero_aleatorio))
            else:
                return "Ganaste en " + str (numero_intentos) + " intentos! Si era el " + str (numero_aleatorio) 
print (adivinar_numero())
