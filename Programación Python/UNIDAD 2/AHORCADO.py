import random
import time

lista_partida=[]
lista_palabrasecreta=[]
lista_ahorcado=[]
errores=0
palabra=""
modo=""
listaerrores=[]

seguir="s"
print("Bienvenido al juego del ahorcado")
seguir=input("Quieres echar una partida? (s/n): ").lower()

while seguir!="n":
    while seguir!="s" and seguir!="n":
        print("¡Esa no es una respuesta válida!")
        seguir=input("Quieres echar una partida? (s/n): ").lower()
    if seguir=="n":
        break
    modo=""
    print("1. Modo fácil (El ahorcado de toda la vida)")
    print("2. Modo acentos (El ahorcado distingue entre vocales acentuadas y no acentuadas)")
    print("3. Modo difícil (Solo tres oportunidades para fallar)")
    print("4. Modo contrarreloj (Tienes 30 segundos para adivinar la palabra)")
    while modo!="1" and modo!="2" and modo!="3" and modo!="4":
        modo=input("¿Qué modo quieres jugar? (1/2/3/4): ")
        if modo=="1":
            lista_palabrasecreta.append(random.choice(["guatemalteco","perro","gato","elefante","jirafa","tigre","mono","pez","serpiente", "conejo","tortuga","cocodrilo","rinoceronte","cebra","camello","ballena","pulpo","medusa","caracol","mariposa","abeja","hormiga","araña","mosquito","mosca","grillo","saltamontes","cucaracha","termita","avispa","escarabajo","gallina","pato","pavo","ganso","flamenco","cisne","buitre", "lechuza", "paloma", "cuervo", "loro", "canario", "periquito", "cotorra", "agapornis", "guacamayo", "cardenal", "azulejo", "jilguero", "mirlo", "petirrojo", "ruiseñor", "zorzal", "tordo", "alondra", "avioneta", "planeador", "cohete", "ovni", "astronauta","marte","venus","saturno","urano","neptuno", "sol","luna","estrella","galaxia","universo","cometa","meteorito", "supernova", "agujero", "negro", "blanco", "rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "gris", "marron", "violeta" ]))
        elif modo=="2":
            lista_palabrasecreta.append(random.choice(["plutón","arlequín","árbol","canción","corazón","teléfono","camión","avión","ratón","león","camión","papá","mamá","sofá","café","azúcar","limón","melón", ]))
        elif modo=="3":        
            lista_palabrasecreta.append(random.choice(["guatemalteco","perro","gato","elefante","jirafa","tigre","mono","pez","serpiente", "conejo","tortuga","cocodrilo","rinoceronte","cebra","camello","ballena","pulpo","medusa","caracol","mariposa","abeja","hormiga","araña","mosquito","mosca","grillo","saltamontes","cucaracha","termita","avispa","escarabajo","gallina","pato","pavo","ganso","flamenco","cisne","buitre", "lechuza", "paloma", "cuervo", "loro", "canario", "periquito", "cotorra", "agapornis", "guacamayo", "cardenal", "azulejo", "jilguero", "mirlo", "petirrojo", "ruiseñor", "zorzal", "tordo", "alondra", "avioneta", "planeador", "cohete", "ovni", "astronauta","marte","venus","saturno","urano","neptuno", "sol","luna","estrella","galaxia","universo","cometa","meteorito", "supernova", "agujero", "negro", "blanco", "rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "gris", "marron", "violeta", "celeste", "turquesa", "fucsia", "lila", "beige", "dorado", "plateado","cielo","mar","montaña","bosque","desierto","selva","pradera","isla","laguna","cascada","glaciar","cueva","valle","colina","playa","arena","roca","piedra","flor","hierba","hoja","fruto","semilla", "tallo", "rama", "tronco", "corteza", "flor", "fruto", "semilla", "hoja", "hierba", "maleza", "arbusto", "seto", "parque", "bosque", "selva","desierto","pradera","isla","laguna","cascada","glaciar","cueva","valle","colina","playa","arena","roca","piedra"]))
        elif modo=="4":
            lista_palabrasecreta.append(random.choice(["guatemalteco","perro","gato","elefante","jirafa","tigre","mono","pez","serpiente", "conejo","tortuga","cocodrilo","rinoceronte","cebra","camello","ballena","pulpo","medusa","caracol","mariposa","abeja","hormiga","araña","mosquito","mosca","grillo","saltamontes","cucaracha","termita","avispa","escarabajo","gallina","pato","pavo","ganso","flamenco","cisne","buitre", "lechuza", "paloma", "cuervo", "loro", "canario", "periquito", "cotorra", "agapornis", "guacamayo", "cardenal", "azulejo", "jilguero", "mirlo", "petirrojo", "ruiseñor", "zorzal", "tordo", "alondra", "avioneta", "planeador", "cohete", "ovni", "astronauta","marte","venus","saturno","urano","neptuno", "sol","luna","estrella","galaxia","universo","cometa","meteorito", "supernova", "agujero", "negro", "blanco", "rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosa", "gris", "marron", "violeta", "celeste", "turquesa", "fucsia", "lila", "beige", "dorado", "plateado","cielo","mar","montaña","bosque","desierto","selva","pradera","isla","laguna","cascada","glaciar","cueva","valle","colina","playa","arena","roca","piedra","flor","hierba","hoja","fruto","semilla", "tallo", "rama", "tronco", "corteza", "flor", "fruto", "semilla", "hoja", "hierba", "maleza", "arbusto", "seto", "parque", "bosque", "selva","desierto","pradera","isla","laguna","cascada","glaciar","cueva","valle","colina","playa","arena","roca","piedra"]))
        else:
            print("Ese modo de juego no es válido.")
    palabra=str(lista_palabrasecreta[0].upper())
    iniciotiem=time.perf_counter()
    totaltiem=0
    for i in range(1_000_000):
        totaltiem=totaltiem+i
    for i in range(len(palabra)):
        lista_partida.append("_")
    while "_" in lista_partida:
        if modo=="4":
            fintiem=time.perf_counter()
            tiempo=round(fintiem-iniciotiem,2)
            if tiempo>30:
                print(f"¡Has perdido por tiempo! La palabra era: {palabra}")
                lista_partida=[]
                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                if seguir!="s":
                    break
                else:
                    lista_palabrasecreta=[]
                    lista_partida=[]
                    lista_ahorcado=[]
                    break
        print(lista_partida)
        respuesta=""
        while not respuesta.isalpha():
            respuesta=""
            respuesta=input("Di una letra o intenta adivinar la palabra: ").upper()
            if respuesta=="":
                print("¡No has escrito nada!")
                print(lista_partida)
            elif not respuesta.isalpha():
                print("¡Eso no es un carácter válido!")
                print(lista_partida)
            else:
                break
        print("")
        if len(respuesta)==1:
            if respuesta==palabra:
                print((f"¡Has acertado la palabra: {palabra}!"))
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
                        if "_" not in lista_partida:
                            print((f"¡Has acertado la palabra: {palabra}!"))
                            fintiem=time.perf_counter()
                            tiempo=round(fintiem-iniciotiem,2)
                            print(f"Tiempo de juego: {tiempo} segundos")
                            lista_partida=[]
                            seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                            if seguir!="s":
                                break
                            else:
                                lista_palabrasecreta=[]
                                lista_partida=[]
                                lista_ahorcado=[]
                                break
                    else:
                        print((f"¡La letra {respuesta} no está en la palabra!"))
                        if modo=="3":
                             errores+=1
                             print(f"¡Te quedan {3-errores} oportunidades!")
                             if errores==3:
                                print(f"¡Has perdido! La palabra era: {palabra}")
                                fintiem=time.perf_counter()
                                tiempo=round(fintiem-iniciotiem,2)
                                print(f"Tiempo de juego: {tiempo} segundos")
                                lista_partida=[]
                                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                                if seguir!="s":
                                    break
                                else:
                                    lista_palabrasecreta=[]
                                    lista_partida=[]
                                    lista_ahorcado=[]
                                    errores=0
                                    break
                        else:
                            if lista_ahorcado==[]:
                                lista_ahorcado.append("A")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A"]:
                                lista_ahorcado.append("H")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A","H"]:
                                lista_ahorcado.append("O")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A","H","O"]:
                                lista_ahorcado.append("R")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A","H","O","R"]:
                                lista_ahorcado.append("C")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A","H","O","R","C"]:
                                lista_ahorcado.append("A")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A","H","O","R","C","A"]:
                                lista_ahorcado.append("D")
                                print(lista_ahorcado)
                            elif lista_ahorcado==["A","H","O","R","C","A","D"]:
                                lista_ahorcado.append("O")
                                print(lista_ahorcado)
                                print(f"¡Has perdido! La palabra era: {palabra}")
                                fintiem=time.perf_counter()
                                tiempo=round(fintiem-iniciotiem,2)
                                print(f"Tiempo de juego: {tiempo} segundos")
                                lista_partida=[]
                                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                                if seguir!="s":
                                    break
                                else:
                                    lista_palabrasecreta=[]
                                    lista_partida=[]
                                    lista_ahorcado=[]
                                    break
        else:
            if respuesta==palabra:
                print((f"¡Has acertado la palabra: {palabra}!"))
                fintiem=time.perf_counter()
                tiempo=round(fintiem-iniciotiem,2)
                print(f"Tiempo de juego: {tiempo} segundos")
                lista_partida=[]
                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                if seguir!="s":
                    break
                else:
                    lista_palabrasecreta=[]
                    lista_partida=[]
                    lista_ahorcado=[]
                    break
            else:
                print((f"¡La palabra {respuesta} no es correcta!"))
                if modo=="3":
                             errores+=1
                             print(f"¡Te quedan {3-errores} oportunidades!")
                             if errores==3:
                                print(f"¡Has perdido! La palabra era: {palabra}")
                                fintiem=time.perf_counter()
                                tiempo=round(fintiem-iniciotiem,2)
                                print(f"Tiempo de juego: {tiempo} segundos")
                                lista_partida=[]
                                seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                                if seguir!="s":
                                    break
                                else:
                                    lista_palabrasecreta=[]
                                    lista_partida=[]
                                    lista_ahorcado=[]
                                    errores=0
                                    break
                else:
                    if lista_ahorcado==[]:
                        lista_ahorcado.append("A")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A"]:
                        lista_ahorcado.append("H")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A","H"]:
                        lista_ahorcado.append("O")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A","H","O"]:
                        lista_ahorcado.append("R")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A","H","O","R"]:
                        lista_ahorcado.append("C")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A","H","O","R","C"]:
                        lista_ahorcado.append("A")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A","H","O","R","C","A"]:
                        lista_ahorcado.append("D")
                        print(lista_ahorcado)
                    elif lista_ahorcado==["A","H","O","R","C","A","D"]:
                        lista_ahorcado.append("O")
                        print(lista_ahorcado)
                        print(f"¡Has perdido! La palabra era: {palabra}")
                        fintiem=time.perf_counter()
                        tiempo=round(fintiem-iniciotiem,2)
                        print(f"Tiempo de juego: {tiempo} segundos")
                        lista_partida=[]
                        seguir=input("¿Quieres echar otra partida? (s/n): ").lower()
                        if seguir!="s":
                            break
                        else:
                            lista_palabrasecreta=[]
                            lista_partida=[]
                            lista_ahorcado=[]
                            errores=0
                            break
if palabra=="":
    print("¡Está bien, ya jugaremos otro día!")
else:
    print("¡Gracias por jugar!")