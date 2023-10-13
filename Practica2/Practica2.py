# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:52:30 2023

@author: guill
"""
from tabulate import tabulate  # Importar la biblioteca tabulate
# Crear una lista de personajes
personajes = [
    {"nombre": "Mario", "ojos_azules": True, "es_hombre": True, "lleva_sombrero": True},
    {"nombre": "Luigi", "ojos_azules": False, "es_hombre": True, "lleva_sombrero": True},
    {"nombre": "Peach", "ojos_azules": True, "es_hombre": False, "lleva_sombrero": False},
    # Agrega más personajes aquí
]

# Función para mostrar la tabla de personajes
def mostrar_personajes(personajes):
    if not personajes:
        print("No hay personajes en la lista.")
        return

    # Crear una lista de listas para la tabla
    tabla = []
    
    # Obtener la lista de todos los atributos
    atributos = list(personajes[0].keys())

    # Encabezados de la tabla
    headers = atributos.copy()
    
    for personaje in personajes:
        fila = [personaje[atributo] for atributo in atributos]
        tabla.append(fila)

    # Imprimir la tabla utilizando tabulate
    print("\nTabla de Personajes:")
    print(tabulate(tabla, headers, tablefmt="grid"))
    
# Función para hacer una pregunta al usuario
def hacer_pregunta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    while respuesta not in ["s", "n"]:
        print("Por favor, responde con 's' o 'n'.")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == "s"

def agregar_nuevo_personaje():
    nuevo_personaje = {}
    nuevo_personaje["nombre"] = input("Nombre del nuevo personaje: ")
    
    # Itera a través de todos los atributos existentes y pregunta si el personaje los tiene.
    for atributo in personajes[0].keys():
        if atributo != "nombre":
            respuesta = input(f"¿{nuevo_personaje['nombre']} tiene '{atributo}'? (s/n): ").strip().lower()
            nuevo_personaje[atributo] = respuesta == "s"

    # Agrega el nuevo personaje a la lista de personajes
    personajes.append(nuevo_personaje)
    print(f"Se ha agregado a {nuevo_personaje['nombre']} a la base de datos.")

def agregar_atributo_individual(atributo):
   for personaje in personajes:
        respuesta = input(f"¿El personaje '{personaje['nombre']}' tiene '{atributo}'? (s/n): ").strip().lower()
        if respuesta == "s":
            personaje[atributo] = True
        elif respuesta == "n":
            personaje[atributo] = False
        else:
            print("Respuesta no válida. Por favor, responde con 's' o 'n'.")

# Función para adivinar el personaje
def adivinar_personaje(personajes):
    print("Piensa en un personaje y responde las siguientes preguntas con 's' o 'n'.")
    atributos = list(personajes[0].keys())

    for atributo in atributos[1:]:  # Comienza desde el segundo atributo
        if hacer_pregunta(f"¿El personaje tiene {atributo}?"):
            personajes = [p for p in personajes if p[atributo]]
        else:
            personajes = [p for p in personajes if not p[atributo]]
    if len(personajes) == 0:
        print("No encontré ningún personaje con esos atributos.")
        print("Gracias por jugar.")
    elif len(personajes) == 1:
        respuesta_correcta = hacer_pregunta(f"¿Tu personaje es {personajes[0]['nombre']}? (s/n)")
        if respuesta_correcta:
            print("¡He adivinado correctamente!")
        else:
            print(f"No he adivinado correctamente. Tu personaje no es {personajes[0]['nombre']}.")
            if hacer_pregunta("¿Quieres agregar un nuevo personaje?"):
                # Llama a la función para agregar un nuevo personaje
                agregar_nuevo_personaje()
                nuevo_atributo = input("Nombre del nuevo atributo a agregar a cada personaje: ")
                agregar_atributo_individual(nuevo_atributo)
                 
            else:
                print("ok no.")
            
    else:
        print("No pude adivinar el personaje. ¡Has ganado!")

# Función para jugar de nuevo
def jugar_de_nuevo():
    respuesta = hacer_pregunta("¿Quieres jugar de nuevo?")
    return respuesta

# Juego principal
while True:
    mostrar_personajes(personajes)
    adivinar_personaje(personajes)
    if not jugar_de_nuevo():
        print("¡Gracias por jugar! Hasta luego.")
        break