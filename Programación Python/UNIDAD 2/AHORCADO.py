import random
import time

lista_partida=[]
lista_palabrasecreta=[]
lista_acentos=[]
lista_ahorcado=[]
errores=0
palabra=""
modo=""
listaerrores=[]
numvictorias=0
numderrotas=0
palabranueva=""
listanoacentos=["perro","gato","elefante","jirafa","tigre","mono","pez","serpiente", "conejo","tortuga"]
listasiacentos=["plutón","arlequín","árbol","canción","corazón","teléfono","camión","avión","ratón","león"]
lista_aciertos=[]
lista_errores=[]

seguir="s"
print("Bienvenido al juego del ahorcado")
seguir=input("Quieres echar una partida? (s/n): ").lower()

while seguir!="n":
    while seguir!="s" and seguir!="n":
        print("¡Esa no es una respuesta válida!")
        seguir=input("Quieres echar una partida? (s/n): ").lower()
    if seguir=="n":
        break
    print(f"Victorias: {numvictorias} | Derrotas: {numderrotas}")
    print("")
    modo=""
    palabranueva=input("Quieres introducir una palabra nueva? (s/n): ").lower()
    while palabranueva!="s" and palabranueva!="n":
        print("¡Esa no es una respuesta válida!")
        palabranueva=input("Quieres introducir una palabra nueva? (s/n): ").lower()
    if palabranueva=="s":
        palabranueva=input("Introduce la palabra nueva: ").lower()
        if "áéíóú" in palabranueva:
            listasiacentos.append(palabranueva)
        else:
            listanoacentos.append(palabranueva)
    lista_aciertos.clear()
    lista_errores.clear()
    print("1. Modo fácil (El ahorcado de toda la vida)")
    print("2. Modo acentos (El ahorcado distingue entre vocales acentuadas y no acentuadas)")
    print("3. Modo difícil (Solo tres oportunidades para fallar)")
    print("4. Modo contrarreloj (Tienes 30 segundos para adivinar la palabra)")
    while modo!="1" and modo!="2" and modo!="3" and modo!="4":
        modo=input("¿Qué modo quieres jugar? (1/2/3/4): ")
        if modo=="1":
            lista_palabrasecreta.append(random.choice(listanoacentos))
        elif modo=="2":
            lista_palabrasecreta.append(random.choice(listasiacentos))
        elif modo=="3":        
            lista_palabrasecreta.append(random.choice(listanoacentos))
        elif modo=="4":
            lista_palabrasecreta.append(random.choice(listanoacentos))
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
                numderrotas=numderrotas+1
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
            print("")
            print("LETRAS ACERTADAS: ", lista_aciertos)
            print("LETRAS FALLADAS: ", lista_errores)
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
                numvictorias=numvictorias+1
                fintiem=time.perf_counter()
                tiempo=round(fintiem-iniciotiem,2)
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
                        lista_aciertos.append(respuesta)
                        for i in range(len(palabra)):
                            if palabra[i]==respuesta:
                                lista_partida[i]=respuesta
                        if "_" not in lista_partida:
                            print((f"¡Has acertado la palabra: {palabra}!"))
                            numvictorias=numvictorias+1
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
                        lista_errores.append(respuesta)
                        if modo=="3":
                             errores+=1
                             print(f"¡Te quedan {3-errores} oportunidades!")
                             if errores==3:
                                print(f"¡Has perdido! La palabra era: {palabra}")
                                numderrotas=numderrotas+1
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
                                numderrotas=numderrotas+1
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
                numvictorias=numvictorias+1
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
                                numderrotas=numderrotas+1
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
                        numderrotas=numderrotas+1
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