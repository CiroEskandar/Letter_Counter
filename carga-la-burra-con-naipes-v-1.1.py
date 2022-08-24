
from random import *



#! este juego se diferencia de la V 2.0 en la zona donde se decide el desempate, aquí se toma en cuenta el empate en el resultado del desempate
#! la versión 2.0 no permite que eso exista, y la aleatoriedad del proceso se da cuando se decide el orden de lanzamiento 
#! (allí si se toma en cuenta en empate y el proceso para resolverlo)

#! this game differs from V 2.0 in the area where the tie-breaker is decided, here the tie is taken into account in the result of the tie-breaker.
#! version 2.0 does not allow this, and the randomness of the process is given when deciding the order of the toss. 
#! (there the tie and the process to resolve it are taken into account).


#* listas para el registro de las cartas, en este caso son barajas de poker

#* lists for registration of the cards, in this case poker decks.


diam = ["2-d","3-d","4-d","5-d","6-d","7-d","8-d","9-d","10-d","j-d","q-d","k-d","a-d"]
cor = ["2-c","3-c","4-c","5-c","6-c","7-c","8-c","9-c","10-c","j-c","q-c","k-c","a-c"]
treb = ["2-t","3-t","4-t","5-t","6-t","7-t","8-t","9-t","10-t","j-t","q-t","k-t","a-t"]
pic = ["2-p","3-p","4-p","5-p","6-p","7-p","8-p","9-p","10-p","j-p","q-p","k-p","a-p"]

cartas = ["a-d","2-d","3-d","4-d","5-d","6-d","7-d","8-d","9-d","10-d","j-d","q-d","k-d",
    "a-c","2-c","3-c","4-c","5-c","6-c","7-c","8-c","9-c","10-c","j-c","q-c","k-c",
    "a-t","2-t","3-t","4-t","5-t","6-t","7-t","8-t","9-t","10-t","j-t","q-t","k-t",
    "a-p","2-p","3-p","4-p","5-p","6-p","7-p","8-p","9-p","10-p","j-p","q-p","k-p"]


#* reparticion de cartas de los jugadores, ninguna carta está repetida.

#* dealing of cards among the players, none of the cards are duplicated


jug1 = sample(cartas,5)

cartas.remove(jug1[0])
cartas.remove(jug1[1])
cartas.remove(jug1[2])
cartas.remove(jug1[3])
cartas.remove(jug1[4])

jug2 = sample(cartas,5)

cartas.remove(jug2[0])
cartas.remove(jug2[1])
cartas.remove(jug2[2])
cartas.remove(jug2[3])
cartas.remove(jug2[4])

jug3 = sample(cartas,5)

cartas.remove(jug3[0])
cartas.remove(jug3[1])
cartas.remove(jug3[2])
cartas.remove(jug3[3])
cartas.remove(jug3[4])

jug4 = sample(cartas,5)

ciclo = 1


#* este while es el bucle más grande, engloba toda la parte jugable del programa.

#* this "while" is te biggest loop, include all the playable part of the program.


while ciclo < 6 :
    print("es la ronda ",ciclo,"presiona enter para iniciar----------------------------------------------------------")
    x = input("")
    print()


    #* en esta sección se decide el orden de juego de cada uno, quien lanza primero y quien después.

    #* in this section, the order of play of each player is decided, who throws first and who throws second.


    dado = ["1","2","3","4"]

    turno1 = choice(dado)
    dado.remove(turno1)   

    turno2 = choice(dado)
    dado.remove(turno2)

    turno3 = choice(dado)
    dado.remove(turno3)
    
    turno4 = choice(dado)
    dado.remove(turno4)


    turnos = [0,1,2,3,4]

    turnos[int(turno1)] = jug1

    turnos[int(turno2)] = jug2

    turnos[int(turno3)] = jug3

    turnos[int(turno4)] = jug4

    print(turnos)
    print()



    print("j1 vas de",turno1,"y tus cartas son:",jug1,"     j2 vas de",turno2,"y tus cartas son:",jug2)
    print()
    print("j3 vas de",turno3,"y tus cartas son:",jug3,"     j4 vas de",turno4,"y tus cartas son:",jug4)
    print()


    #* se solicitan las jugadas de cada jugador en base a las cartas de su mano, que ya fueron repartidas anteriormente. Para cada jugador hay un bucle
    #* que se activa cuando no entra una jugada valida (una carte de su mano)

    #* the moves of each player are requested on the basis of the cards in his hand, which have already been dealt previously. For each player exist a loop
    #* that start when not give a valid choise (some card on his hand)


    jugada1 = input("primer turno, ingresa tu jugada: ")
    print()

    while jugada1 not in turnos[1]:

        jugada1 = input("primer turno esa carta no está en tu mano, ingresa una carta de tu mano: ")
        print()

        if jugada1 in turnos[1]:   break

    turnos[1].remove(jugada1)

    jugada2 = input("segundo turno, ingresa tu jugada: ")
    print()

    while jugada2 not in turnos[2]:

        jugada2 = input("segundo turno esa carta no está en tu mano, ingresa una carta de tu mano: ")
        print()

        if jugada2 in turnos[2]:   break

    turnos[2].remove(jugada2)


    jugada3 = input("tercer turno, ingresa tu jugada: ")
    print()

    while jugada3 not in turnos[3]:

        jugada3 = input("tercer turno esa carta no está en tu mano, ingresa una carta de tu mano: ")
        print()

        if jugada3 in turnos[3]:   break

    turnos[3].remove(jugada3)    
    

    jugada4 = input("cuarto turno, ingresa tu jugada: ")
    print()

    while jugada4 not in turnos[4]:

        jugada4 = input("cuarto turno esa carta no está en tu mano, ingresa una carta de tu mano: ")
        print()

        if jugada4 in turnos[4]:   break

    turnos[4].remove(jugada4)


    #* se ponderan las jugadas de cada participante y le incluyen en una lista

    #* the moves of each participant are weighted and included on a list


    ubi1 = jugada1.split("-")

    if ubi1[1] == "d":
        val1 = diam.index(jugada1)

    elif ubi1[1] == "p":
        val1 = pic.index(jugada1)

    elif ubi1[1] == "t":
        val1 = treb.index(jugada1)

    elif ubi1[1] == "c":
        val1 = cor.index(jugada1)



    ubi2 = jugada2.split("-")

    if ubi2[1] == "d":
        val2 = diam.index(jugada2)

    elif ubi2[1] == "p":
        val2 = pic.index(jugada2)

    elif ubi2[1] == "t":
        val2 = treb.index(jugada2)

    elif ubi2[1] == "c":
        val2 = cor.index(jugada2)



    ubi3 = jugada3.split("-")

    if ubi3[1] == "d":
        val3 = diam.index(jugada3)

    elif ubi3[1] == "p":
        val3 = pic.index(jugada3)

    elif ubi3[1] == "t":
        val3 = treb.index(jugada3)

    elif ubi3[1] == "c":
        val3 = cor.index(jugada3)



    ubi4 = jugada4.split("-")

    if ubi4[1] == "d":
        val4 = diam.index(jugada4)

    elif ubi4[1] == "p":
        val4 = pic.index(jugada4)

    elif ubi4[1] == "t":
        val4 = treb.index(jugada4)

    elif ubi4[1] == "c":
        val4 = cor.index(jugada4)


    val = [val1,val2,val3,val4]


    #* esta porción de codigo se encarga de realizar el desempate entre dos jugadores (en caso de haberlo), funciona con lanzamientos de dado

    #* this portion of the code is in charge of performing the tie-breaker between 2 players (if any), it works with die rolls.


    if val.count(max(val)) == 2:

        rep1 = val.index(max(val))
        rep2 = val.index(max(val),rep1+1)

        print("hay un empate entre en turno",rep1+1,"y el turno",rep2+1)
        print()

        print("turno",rep1+1,"aprieta enter para tirar el dado")
        vez1 = input("")

        dado1 = ["1","2","3","4","5","6"]

        tiro1 = choice(dado1)
        print("sacaste:",tiro1)
        print()

        print("turno",rep2+1,"aprieta enter para tirar el dado")
        vez2 = input("")

        tiro2 = choice(dado1)
        print("sacaste: ",tiro2)
        print()

        if tiro1 != tiro2:
            gana = [tiro1,tiro2]
            print("gana el que tiro el",max(gana))


        while tiro1 == tiro2:
            print("hay un empate entre en turno",rep1+1,"y el turno",rep2+1)
            print()

            print("turno",rep1+1,"aprieta enter para tirar el dado")
            vez1 = input("")

            dado1 = ["1","2","3","4","5","6"]

            tiro1 = choice(dado1)
            print("sacaste:",tiro1)
            print()

            print("turno",rep2+1,"aprieta enter para tirar el dado")
            vez2 = input("")

            tiro2 = choice(dado1)
            print("sacaste: ",tiro2)
            print()

            if tiro1 != tiro2:
                break

            if tiro1 != tiro2:
                gana = [tiro1,tiro2]
                print("gana el tiro",max(gana))


    #* esta porción de codigo se encarga de realizar el desempate entre 3 jugadores (en caso de haberlo), funciona con lanzamientos de dado

    #* this portion of the code is in charge of performing the tie-breaker between 3 players (if any), it works with die rolls.


    if val.count(max(val))== 3:

        rep1 = val.index(max(val))
        rep2 = val.index(max(val),rep1+1)
        rep3 = val.index(max(val),rep2+1)

        print("hay un empate entre en turno",rep1+1,"el turno",rep2+1,"y el turno",rep3+1)
        print()

        print("turno",rep1+1,"aprieta enter para tirar el dado")
        vez1 = input("")

        dado1 = ["1","2","3","4","5","6"]

        tiro1 = choice(dado1)
        print("sacaste:",tiro1)
        print()

        print("turno",rep2+1,"aprieta enter para tirar el dado")
        vez2 = input("")

        tiro2 = choice(dado1)
        print("sacaste: ",tiro2)
        print()

        print("turno",rep3+1,"aprieta enter para tirar el dado")
        vez3 = input("")

        tiro3 = choice(dado1)
        print("sacaste: ",tiro3)
        print()

        tiros1 = [tiro1,tiro2,tiro3]

        if tiros1.count(max(tiros1))== 1:
            print("gana el que tiró",max(tiros1))


        while tiros1.count(max(tiros1))== 3:
            print("hay un empate entre en turno",rep1,"el turno",rep2,"y el turno",rep3)
            print()

            print("turno",rep1+1,"aprieta enter para tirar el dado")
            vez1 = input("")

            dado1 = ["1","2","3","4","5","6"]

            tiro1 = choice(dado1)
            print("sacaste:",tiro1)
            print()

            print("turno",rep2+1,"aprieta enter para tirar el dado")
            vez2 = input("")

            tiro2 = choice(dado1)
            print("sacaste: ",tiro2)
            print()

            print("turno",rep3,"aprieta enter para tirar el dado")
            vez3 = input("")

            tiro3 = choice(dado1)
            print("sacaste: ",tiro3)
            print()

            tiros1 = [tiro1,tiro2,tiro3]

            if tiros1.count(max(tiros1))== 1:
                break

            if tiros1.count(max(tiros1))== 1:
                print("gana el que tiró",max(tiros1))
        
            if tiros1.count(max(tiros1)) == 2:

                rep1 = tiros1.index(max(tiros1))
                rep2 = tiros1.index(max(tiros1),rep1+1)

                print("hay un empate entre en turno",rep1+1,"y el turno",rep2+1)
                print()

                print("turno",rep1,"aprieta enter para tirar el dado")
                vez1 = input("")

                dado1 = ["1","2","3","4","5","6"]

                tiro1 = choice(dado1)
                print("sacaste:",tiro1)
                print()

                print("turno",rep2,"aprieta enter para tirar el dado")
                vez2 = input("")

                tiro2 = choice(dado1)
                print("sacaste: ",tiro2)
                print()

                if tiro1 != tiro2:
                    gana = [tiro1,tiro2]
                    print("gana el tiro",max(gana))
            
                while tiro1 == tiro2:
                    print("hay un empate entre en turno",rep1,"y el turno",rep2)
                    print()

                    print("turno",rep1,"aprieta enter para tirar el dado")
                    vez1 = input("")

                    dado1 = ["1","2","3","4","5","6"]

                    tiro1 = choice(dado1)
                    print("sacaste:",tiro1)
                    print()

                    print("turno",rep2,"aprieta enter para tirar el dado")
                    vez2 = input("")

                    tiro2 = choice(dado1)
                    print("sacaste: ",tiro2)
                    print()

                    if tiro1 != tiro2:
                        break

                    if tiro1 != tiro2:
                        gana = [tiro1,tiro2]
                        print("gana el tiro",max(gana))


    #* aquí solo hay una respuesta en el caso de haber una empate cuadruple, ya que es muy difícil que eso pase.

    #* There is only one response in the case of a four-way tie, is very difficult for that to happen.


    if val.count(max(val)) == 4:
        print("hay que reiniciar el juego, ya que se acaba de romper")


    #* este código imprime por pantalla al ganador de la ronda y lleva la cuenta de los juegos ganados por cada jugador

    #* this code print in the screen the winner of the round and have the count of the games win for each player


    j1 = 0
    j2 = 0
    j3 = 0
    j4 = 0

    if max(val) == val1 and val.count(max(val))== 1:
        print("el ganador de la ronda es el jugador 1, ya que lanzó",jugada1,"!!!")
        print()
        j1 += 1

    elif max(val) == val2 and val.count(max(val))== 1:
        print("el ganador de la ronda es el jugador 2, ya que lanzó",jugada2,"!!!")
        print()
        j2 += 1

    elif max(val) == val3 and val.count(max(val))== 1:
        print("el ganador de la ronda es el jugador 3, ya que lanzó",jugada3,"!!!")
        print()
        j3 += 1

    elif max(val) == val4 and val.count(max(val))== 1:
        print("el ganador de la ronda es el jugador 4, ya que lanzó",jugada4,"!!!")
        print()
        j4 += 1

    
    print("victorias:    j1 =",j1,"        j2 =",j2,"       j3 =",j3,"       j4 =",j4)
    print()

    ciclo +=1


print("el juego se ha terminado, es victoria en el juego para el jugador que más rondas ganó")