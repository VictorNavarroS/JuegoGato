"""
Juego del gato, tres en linea o ta-te-ti.
Creado por Victor Navarro S.
"""
# creacion de la matriz
tablero=[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_'],
]
posiciones=[
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
]
# conteo de filas y columnas
filas=len(tablero)
columnas=len(tablero[0])

# funcion para imprimir tablero para juegos y posiciones
def imprime_tablero():
    print('--------------------------------------------')   
    print('\n')
    for x in range(filas):
        for i in range(columnas):
            print('|'+tablero[x][i]+'|', end=' ')
        print(end='  ')
        for i in range(columnas):
            print('|'+posiciones[x][i]+'|', end=' ')                           
        print('\n')
    print('--------------------------------------------')   

# asocia un numero a cada posicion de la matriz
def posicion_en_matriz(numero,ficha):
    if numero ==1:
        if evalua_posicion(tablero[0][0]):
            tablero[0][0]=ficha
            return True
        else:
            return False
    elif numero ==2:        
        if evalua_posicion(tablero[0][1]):
            tablero[0][1]=ficha
            return True
        else:
            return False
    elif numero ==3:
        if evalua_posicion(tablero[0][2]):
            tablero[0][2]=ficha
            return True
        else:
            return False
    elif numero ==4:
        if evalua_posicion(tablero[1][0]):
            tablero[1][0]=ficha
            return True
        else:
            return False
    elif numero ==5:
        if evalua_posicion(tablero[1][1]):
            tablero[1][1]=ficha
            return True
        else:
            return False
    elif numero ==6:
        if evalua_posicion(tablero[1][2]):
            tablero[1][2]=ficha
            return True
        else:
            return False
    elif numero ==7:
        if evalua_posicion(tablero[2][0]):
            tablero[2][0]=ficha
            return True
        else:
            return False
    elif numero ==8:
        if evalua_posicion(tablero[2][1]):
            tablero[2][1]=ficha
            return True
        else:
            return False
    elif numero ==9:
        if evalua_posicion(tablero[2][2]):
            tablero[2][2]=ficha
            return True
        else:
            return False
    
# Verifica que la posicion este disponible
def evalua_posicion(posicion):
    estado=False
    if '_' in posicion:
        estado=True
    else:
        estado=False
    return estado
#comprueba tablero
def comprueba_tablero(disponible):
    for x in tablero:
        for i in x:
            est='_' in i
            if est:
                disponible=True
                return disponible
            else:
                disponible=False
    return disponible

# clase jugador
class Jugador():    
    def __init__(self,num,ficha):        
        self.Num_jugador=num
        self.ficha_usada: ficha

# instanciacion de jugadores
jug1= Jugador(1,"")
jug2= Jugador(2,"")

def jug_ganador(ta, fi):
 # devuelve True si el jugador ha ganado.
    return ((ta[0][0] == fi and ta[0][1] == fi and ta[0][2] == fi) or # horizontal superior
            (ta[1][0] == fi and ta[1][1] == fi and ta[1][2] == fi) or # horizontal medio
            (ta[2][0] == fi and ta[2][1] == fi and ta[2][2] == fi) or # horizontal inferior
            (ta[0][0] == fi and ta[1][0] == fi and ta[2][0] == fi) or # vertical izquierda
            (ta[0][1] == fi and ta[1][1] == fi and ta[2][1] == fi) or # vertical medio
            (ta[0][2] == fi and ta[1][2] == fi and ta[2][2] == fi) or # vertical derecha
            (ta[0][0] == fi and ta[1][1] == fi and ta[2][2] == fi) or # primera diagonal
            (ta[0][2] == fi and ta[1][1] == fi and ta[2][0] == fi))   # segunda diagonal

# Inicio del juego
print('----------------------------------------------------------')
print('-----          Bienvenido al juego del gato          -----')
print('-----           (tres en linea o ta-te-ti)           -----')
print('----------------------------------------------------------')
print("-----                    REGLAS                      -----")
print("----- El juego funciona de la siguiente forma:       -----")
print("----- El Jugador con la ficha 'X' inicia el juego    -----")
print("----- posicionando su ficha en la casilla deseada,   -----")
print("----- luego, se alternaran los turnos y cada jugador -----")
print("----- debe seleccionar la posicion en donde quiera   -----")
print("----- posicionar su ficha. Gana quien logre 3 fichas -----")
print("----- en linea ya se vertical, horizontal o diagonal -----")
imprime_tablero()
partida=True
sel_ficha=True
ganador=''

# bucle de juego
while partida:
    tablero=[
        ['_','_','_'],
        ['_','_','_'],
        ['_','_','_'],
    ]    
    seleccion=input("Desea empezar un juego nuevo? (S/N): ")
    seleccion=seleccion.upper()
    if seleccion=="N":
        print("¡¡¡Gracias!!! Hasta Luego")
        partida=False          
    elif seleccion=="S":    
        # bucle de seleccion de ficha
        while sel_ficha:
            ficha=input('Jugador 1- ¿Que ficha desea utilizar? (X , O): ')
            ficha=ficha.upper()
            # asignacion de fichas
            if ficha=="X":               
                jug1.ficha_usada="X"               
                jug2.ficha_usada="O"
                sel_ficha=False
            elif ficha=="O":
                jug1.ficha_usada="O"               
                jug2.ficha_usada="X"
                sel_ficha=False
            else:
                print("Debe ingresar X u O")
                continue; 
        print('--------------------------------------------')            
        print('Las fichas asignadas son:')
        print("Jugador 1: ",jug1.ficha_usada," y ","Jugador 2: ",jug2.ficha_usada) 
        if jug1.ficha_usada=="X":
            jug_activo=jug1.Num_jugador
        else:
            jug_activo=jug2.Num_jugador 
        print('--------------------------------------------')            
        print('             Comienzo del Juego          ')
        print('        Empieza jugador con ficha "X"           ')
        imprime_tablero()
        juego = True
        while juego:   
            try:    
                ubicacion=int(input('Jugador '+str(jug_activo)+' - Seleccione posicion de ficha(1 a 9): '))
                if ubicacion >0 and ubicacion<10:              
                    if jug_activo==1:
                        if posicion_en_matriz(ubicacion,jug1.ficha_usada):
                            print ('- Jugador 1 asigna ficha "'+jug1.ficha_usada+'" a posicion '+ str(ubicacion))                            
                            imprime_tablero()  
                            if jug_ganador(tablero, jug1.ficha_usada):
                                print('//////////////////////////////////////////////////')
                                print('------------Jugador 1 es el ganador----------------')
                                print('----------------Juego terminado----------------') 
                                print('//////////////////////////////////////////////////')
                                break
                            else:
                                juego=comprueba_tablero(juego)
                                jug_activo=jug2.Num_jugador 
                        else:
                            print('//////////////////////////////////////////////////////')
                            print('Posicion ya ocupada. Seleccione una posicion valida') 
                            print('//////////////////////////////////////////////////////')               
                    else:
                        if posicion_en_matriz(ubicacion,jug2.ficha_usada):
                            print ('- Jugador 2 asigna ficha "'+jug2.ficha_usada+'" a posicion '+ str(ubicacion))                            
                            imprime_tablero()  
                            if jug_ganador(tablero, jug2.ficha_usada):
                                print('//////////////////////////////////////////////////')
                                print('------------Jugador 2 es el ganador----------------')
                                print('----------------Juego terminado----------------') 
                                print('//////////////////////////////////////////////////')
                                break
                            else:
                                juego=comprueba_tablero(juego)
                                jug_activo=jug1.Num_jugador 
                        else:
                            print('//////////////////////////////////////////////////////')
                            print('Posicion ya ocupada. Seleccione una posicion valida') 
                            print('//////////////////////////////////////////////////////') 
                else:
                    print('//////////////////////////////////////////////////')
                    print('        Debe elegir un numero entre 1 y 9') 
                    print('//////////////////////////////////////////////////')
                    imprime_tablero()  
            except:
                print('//////////////////////////////////////////////////')
                print('       Debe elegir un valor numerico valido')              
                print('//////////////////////////////////////////////////')                   
                imprime_tablero()
        if juego==False:
            print('//////////////////////////////////////////////////')
            print('-------------- Empate ----------------')
            print('---------- Juego terminado ------------') 
            print('//////////////////////////////////////////////////')          
        sel_ficha=True
        continue;
    else:
        print("Debe ingresar S o N")
        continue;
