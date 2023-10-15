# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:08:34 2023

@author: guill
"""

import random

# Define los personajes, habitaciones y armas
personajes = ["Sr. Blanco", "Sra. Escarlata", "Profesor Ciruela", "Sra. Pardo", "Coronel Mostaza"]
habitaciones = ["Jardin", "Cocina", "Biblioteca", "Sótano", "Comedor"]
armas = ["Candelabro", "Cuchillo", "Pistola", "Cuerda", "Llave inglesa"]

# Genera una solución aleatoria
def Aleatorio():
    solucion = {
        "personaje": random.choice(personajes),
        "habitacion": random.choice(habitaciones),
        "arma": random.choice(armas)
    }
    return solucion

def hacer_pregunta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    while respuesta not in ["s", "n"]:
        print("Por favor, responde con 's' o 'n'.")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == "s"

def jugar_de_nuevo():
    respuesta = hacer_pregunta("¿Quieres jugar de nuevo?")
    return respuesta

def jugar():
    intentos = 0
    solucion = Aleatorio()
    while True:
        intentos += 1

        if solucion['personaje']=="Sr. Blanco":
            texto = '''
                Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo, después del postre,
                se escuchó un estruendo proveniente de la sala de estar. Los invitados corrieron hacia donde escucharon el ruido
                y encontraron el cuerpo sin vida del anfitrión, el Sr. Negro, tendido en el suelo. Junto a él, se encontraba
                un candelabro manchado de sangre, y no había señales de entrada forzada.
                
                La investigación comenzó de inmediato, y cada uno de los personajes principales proporcionó sus coartadas:
                    
                -El Sr. Blanco afirmó que había salido al jardín para fumar un cigarro.
                -La Sra. Escarlata dijo que estaba en la biblioteca buscando un libro en ese momento.
                -El Profesor Ciruela mencionó que estaba en la cocina preparando una taza de té mientras veía a la Sra. Pardo cortar las flores.
                -La Sra. Pardo alegó que había estado en el jardín sola cortando flores.
                -El Coronel Mostaza declaró que estaba en el comedor ordenando la vajilla.
                '''
            print(texto)
            suposicion_asesino = input("\n-----Quien es el asesino?-----\na)Sr. Blanco \nb)Sra. Escarlata \nc)Profesor Ciruela \nd)Sra. Pardo \ne)Coronel Mostaza\n")
            suposicion_ubicacion = input("\nDonbde ocurrio?:\na)Jardin \nb)Cocina \nc)Biblioteca \nd)Sotano \ne)Comedor\n")
            suposicion_arma = input("\nCon que arma?:\na)Candelabro \nb)Cuchillo \nc)Pistola \nd)Cuerda \ne)Llave inglesa\n")
            if suposicion_asesino == 'a' and suposicion_ubicacion == 'd' and suposicion_arma == 'a':
                texto = '''
                    Felicidade, acertaste!!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto!!
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")
                
                
        if solucion['personaje']=="Sra. Escarlata":
            texto = '''
                Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo, después del postre,
                se escuchó un estruendo proveniente de la sala de estar. Los invitados corrieron hacia donde escucharon el ruido
                y encontraron el cuerpo sin vida del anfitrión, el Sr. Negro, tendido en el suelo. Junto a él, se encontraba
                el arma manchada de sangre, y no había señales de entrada forzada.
                
                La investigación comenzó de inmediato, y cada uno de los personajes principales proporcionó sus coartadas:
                    
                -El Sr. Blanco afirmó que estaba comiendo una manzana en la biblioteca con el Profesor Ciruela.
                -La Sra. Escarlata dijo que estaba en el comedor lavando los platos.
                -El Profesor Ciruela mencionó que estaba con el Sr Blanco mientras sostenia una Cuerda para colgar un candelabro.
                -La Sra. Pardo alegó que no encontraba su pistola en el sotano por lo que fue a la cocina donde a veces tambien la esconde .
                -El Coronel Mostaza declaró que estaba arreglando el sistema de riego del jardin pero se dio cuenta que no habia agua en toda la casa.
                '''
            print(texto)
            suposicion_asesino = input("\n-----Quien es el asesino?-----\na)Sr. Blanco \nb)Sra. Escarlata \nc)Profesor Ciruela \nd)Sra. Pardo \ne)Coronel Mostaza\n")
            suposicion_ubicacion = input("\nDonbde ocurrio?:\na)Jardin \nb)Cocina \nc)Biblioteca \nd)Sotano \ne)Comedor\n")
            suposicion_arma = input("\nqCon que arma?:\na)Candelabro \nb)Cuchillo \nc)Pistola \nd)Cuerda \ne)Llave inglesa\n")
            if suposicion_asesino == 'b' and suposicion_ubicacion == 'e' and suposicion_arma == 'b':
                texto = '''
                    Felicidade, acertaste!!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto!!
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")
                
                
        if solucion['personaje']=="Profesor Ciruela":
            texto = '''
                Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo, después del postre,
                se escuchó un estruendo proveniente de la sala de estar. Los invitados corrieron hacia donde escucharon el ruido
                y encontraron el cuerpo sin vida del anfitrión, el Sr. Negro, tendido en el suelo. Junto a él, se encontraba
                el arma manchada de sangre, y no había señales de entrada forzada.
                
                La investigación comenzó de inmediato, y cada uno de los personajes principales proporcionó sus coartadas:
                    
                -El Sr. Blanco afirmó que estaba haciendo yoga en el jardin con cuerdas.
                -La Sra. Escarlata dijo que estaba en la cocina lavando los platos y cuchillos.
                -El Profesor Ciruela mencionó que estaba cerrando la ventana de la biblioteca porque llovio fuerte dijo que tenia su pistola con el.
                -La Sra. Pardo alegó que estaba arreglando el candelabro del sotano, ya que el calor no lo dejaba salir.
                -El Coronel Mostaza declaró que estaba buscando su llave inglesa en el comedor.
                '''
            print(texto)
            suposicion_asesino = input("\n-----Quien es el asesino?-----\na)Sr. Blanco \nb)Sra. Escarlata \nc)Profesor Ciruela \nd)Sra. Pardo \ne)Coronel Mostaza\n")
            suposicion_ubicacion = input("\nDonbde ocurrio?:\na)Jardin \nb)Cocina \nc)Biblioteca \nd)Sotano \ne)Comedor\n")
            suposicion_arma = input("\nqCon que arma?:\na)Candelabro \nb)Cuchillo \nc)Pistola \nd)Cuerda \ne)Llave inglesa\n")
            if suposicion_asesino == 'c' and suposicion_ubicacion == 'a' and suposicion_arma == 'd':
                texto = '''
                    !!Felicidades, acertaste!!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto!!
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")
                
                
        if solucion['personaje']=="Sra. Pardo":
            texto = '''
                Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo, después del postre,
                se escuchó un estruendo proveniente de la sala de estar. Los invitados corrieron hacia donde escucharon el ruido
                y encontraron el cuerpo sin vida del anfitrión, el Sr. Negro, tendido en el suelo. Junto a él, se encontraba
                el arma manchada de sangre, y no había señales de entrada forzada.
                
                La investigación comenzó de inmediato, y cada uno de los personajes principales proporcionó sus coartadas:
                    
                -El Sr. Blanco afirmó que estaba recogiendo la nieve del jardin pero se tropezo con cuerdas
                -La Sra. Escarlata dijo que estaba temblando de frio en la cocina lavando los platos y cuchillos.
                -El Profesor Ciruela mencionó que estaba cerrando la ventana de la biblioteca porque nevo fuerte dijo que tenia su pistola con el.
                -La Sra. Pardo alegó que estaba arreglando el candelabro del sotano, ya que el calor no lo dejaba salir.
                -El Coronel Mostaza declaró que estaba buscando su llave inglesa en el comedor para arrglar el clima.
                '''
            print(texto)
            suposicion_asesino = input("\n-----Quien es el asesino?-----\na)Sr. Blanco \nb)Sra. Escarlata \nc)Profesor Ciruela \nd)Sra. Pardo \ne)Coronel Mostaza\n")
            suposicion_ubicacion = input("\nDonbde ocurrio?:\na)Jardin \nb)Cocina \nc)Biblioteca \nd)Sotano \ne)Comedor\n")
            suposicion_arma = input("\nqCon que arma?:\na)Candelabro \nb)Cuchillo \nc)Pistola \nd)Cuerda \ne)Llave inglesa\n")
            if suposicion_asesino == 'd' and suposicion_ubicacion == 'd' and suposicion_arma == 'a':
                texto = '''
                    Felicidade, acertaste!!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto!!
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")
        if solucion['personaje']=="Sra. Pardo":
            texto = '''
                Durante la cena, todos disfrutaban de una conversación amigable. Sin embargo, después del postre,
                se escuchó un estruendo proveniente de la sala de estar. Los invitados corrieron hacia donde escucharon el ruido
                y encontraron el cuerpo sin vida del anfitrión, el Sr. Negro, tendido en el suelo. Junto a él, se encontraba
                el arma manchada de sangre, y no había señales de entrada forzada.
                
                La investigación comenzó de inmediato, y cada uno de los personajes principales proporcionó sus coartadas:
                    
                -El Sr. Blanco afirmó que estaba recogiendo la nieve del jardin pero se tropezo con cuerdas
                -La Sra. Escarlata dijo que estaba en la cocina lavando los platos y cuchillos.
                -El Profesor Ciruela mencionó que estaba cerrando la ventana de la biblioteca porque nevo fuerte dijo que tenia su pistola con el.
                -La Sra. Pardo alegó que estaba arreglando el candelabro del sotano cuando escucho al Sr Blanco caer en el jardin.
                -El Coronel Mostaza declaró que estaba buscando su llave inglesa en el Jardin.
                '''
            print(texto)
            suposicion_asesino = input("\n-----Quien es el asesino?-----\na)Sr. Blanco \nb)Sra. Escarlata \nc)Profesor Ciruela \nd)Sra. Pardo \ne)Coronel Mostaza\n")
            suposicion_ubicacion = input("\nDonbde ocurrio?:\na)Jardin \nb)Cocina \nc)Biblioteca \nd)Sotano \ne)Comedor\n")
            suposicion_arma = input("\nqCon que arma?:\na)Candelabro \nb)Cuchillo \nc)Pistola \nd)Cuerda \ne)Llave inglesa\n")
            if suposicion_asesino == 'e' and suposicion_ubicacion == 'e' and suposicion_arma == 'e':
                texto = '''
                    Felicidade, acertaste!!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto!!
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")
                
                
if __name__ == "__main__":
    print("Bienvenido al juego de Clue en Python.")
    while True:
        jugar()
        if not jugar_de_nuevo():
            print("¡Gracias por jugar! Hasta luego.")
            break
