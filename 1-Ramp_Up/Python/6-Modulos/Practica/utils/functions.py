# Funciones desarrolladas
import math

def dia_semana(dia_num):
    week = {1:"Lunes", 2:"Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado", 7:"Domingo"}
    return week.get(dia_num, "No es un día de la semana")

def ejercicio_2(n):
    lista = list(range(n,0,-1))
    for num in lista.copy():
        print(*lista)
        lista.pop(0)

def comparar(num_1:float, num_2:float):
    num_1 = float(num_1)
    num_2 = float(num_2)
    if num_1 == num_2:
        return "Son iguales"
    elif num_1 > num_2:
        return str(num_1) + " es mayor que " + str(num_2)
    else:
        return str(num_2) + " es mayor que " + str(num_1)

def contador_letras(texto, letra):
    texto = texto.lower()
    return texto.count(letra.lower())

def letter_count(texto):

    all_letters = {}

    for i in texto.lower():
        if i == " ":
            continue
        elif i in all_letters:
            all_letters[i] = all_letters[i] + 1
        else:
            all_letters[i] = 1

    return all_letters

def ejercicio_6(lista, comando, elemento=None):

    lista = list(lista)

    if comando == "add":
        if elemento == None:
            print("No ha introducido ningún elemento")
        else:
            lista.append(elemento)
    elif comando == "remove":
        try:
            lista.remove(elemento)
        except:
            print("El elemento no se encuentra para ser borrado")
    else:
        print("Comando no admitido")
    
    return lista

def junta_palabras(*args):
    return " ".join(args)


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return(fibonacci(n-1) + fibonacci(n-2))


def cuadrado(lado):
    return lado * lado

def triangulo(base, altura):
    return base * altura / 2

def circulo(radio):
    return math.pi * radio ** 2
