import random
import time

lista_partida=[]
lista_palabrasecreta=[]
lisa_ahorcado=[]

seguir="s"
print("Bienvenido al juego del ahorcado")
seguir=input("Quieres echar una partida? (s/n): ").lower()

while seguir=="s":
    lista_palabrasecreta.append(random.choice(["guatemalteco","perro","gato","elefante","jirafa","tigre", "leon","mono","pajaro","pez","serpiente", "conejo","tortuga","cocodrilo","hipopotamo","rinoceronte","zebra","cebra","camello","delfin","ballena", "tiburon","pulpo","medusa","estrella de mar","caracol","mariposa","abeja","hormiga","araña","mosquito","mosca","mariposa nocturna", "libelula","grillo","saltamontes","cucaracha","termita","avispa","escarabajo","gallina","pato","pavo","ganso","pinguino","flamenco","cisne","aguila","halcon","buitre", "lechuza", "buho", "paloma", "cuervo", "gorrión", "loro", "canario", "periquito", "cotorra", "agapornis", "cacatua", "guacamayo", "tucan", "colibri", "cardenal", "azulejo", "verderon", "jilguero", "mirlo", "petirrojo", "ruiseñor", "zorzal", "tordo", "alondra", "avioneta", "helicoptero", "globo aerostatico", "paracaidas", "planeador", "drone", "cohete", "satélite", "estacion espacial", "ovni", "nave espacial", "astronauta","marte","venus","jupiter","saturno","urano","neptuno","pluton", "sol","luna","estrella","galaxia","universo","cometa","asteroide","meteorito", "constelacion", "supernova", "agujero", "negro", "blanco", "rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "gris", "marron", "violeta", "celeste", "turquesa", "fucsia", "lila", "beige", "dorado", "plateado","cielo","mar","montaña","río","bosque","desierto","selva","pradera","isla","océano","laguna","cascada","volcán","glaciar","cueva","valle","colina","playa","arena","roca","piedra","árbol","flor","hierba","hoja","fruto","semilla", "raíz", "tallo", "rama", "tronco", "corteza", "flor", "fruto", "semilla", "hoja", "hierba", "césped", "maleza", "arbusto", "seto", "jardín", "parque", "bosque", "selva","desierto","pradera","isla","océano","laguna","cascada","volcán","glaciar","cueva","valle","colina","playa","arena","roca","piedra"]))
    palabra=lista_palabrasecreta[0].upper()
    for i in range(len(palabra)):
        lista_partida.append("_")
    while "_" in lista_partida:
        print(lista_partida)
        respuesta=input("Di una letra o intenta adivinar la palabra: ").upper()
        print("")
        if len(respuesta)==1:
            if respuesta==palabra:
                print((f"¡Has acertado la palabra!"))
                lista_partida=[]
                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                if seguir!="s":
                    break
                else:
                    lista_palabrasecreta=[]
                    lista_partida=[]
                    break
            else:
                if respuesta in lista_partida:
                    print((f"¡Ya has puesto la letra {respuesta}!"))
                else:
                    if respuesta in palabra:
                        print((f"¡Has acertado la letra {respuesta}!"))
                        for i in range(len(palabra)):
                            if palabra[i]==respuesta:
                                lista_partida[i]=respuesta
                    else:
                        print((f"¡La letra {respuesta} no está en la palabra!"))
        else:
            if respuesta==palabra:
                print((f"¡Has acertado la palabra!"))
                lista_partida=[]
                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                if seguir!="s":
                    break
                else:
                    lista_palabrasecreta=[]
                    lista_partida=[]
                    break
print("¡Gracias por jugar!")