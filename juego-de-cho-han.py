
from random import *

print()
x = input("bienvenido al juego de cho-han, presiona enter para continuar")
print()

money = 10


#* este bucle contiene todo el juego

#* this loop contains all the game


while True:


    #* se muestra el saldo, se decide la cantidad a apostar y se verifica que sea un monto válido

    #* show the balance, the amount to bet is decided and a valid amount is verified


    print("tu saldo es de ",money,"$")
    bet = int(input("¿cuanto deseas apostar?: "))
    print()

    while bet > money and bet <= 0:

        if bet > money:

            print("no tienes esa cantidad de dinero!")
            bet = int(input("ingresa un monto valido: "))
            print()

        elif bet <= 0:

            print("así no es como se apuesta .-.")
            bet = int(input("ingresa un monto valido: "))
            print()


    #* se decide si el resultado será par o impar y se determina el resultado de los dados

    #* odd or even result will be decided and the result of the dices are calculated

        
    elec = input("¿crees que saldrá par o impar?: ")
    print()

    while elec != "par" and elec != "impar":

        elec = input("ingresa si esperas que sea par o impar: ")
        print()

    dado = [1,2,3,4,5,6]

    shot_a = choice(dado)
    shot_b = choice(dado)

    result = shot_a + shot_b

    print("salió: ",result)
    print()


    #* en base al resultado, se determina si ganó la apuesta o si la perdió, se suma o resta el saldo en base a esto

    #* following the result, the won or lose of the player is decided, plus or minus the amount based on this


    if result%2 == 0:
    
        if elec == "par":

            print("acertaste!  ->  +",bet,"$")
            print()
            money += bet
            print("tienes",money,"$")
            print()

        else:

            print("perdiste!  ->  -",bet,"$")
            print()
            money -= bet
            print("tienes",money,"$")
            print()

    else:

        if elec == "impar":

            print("acertaste!  ->  +",bet,"$")
            print()
            money += bet
            print("tienes",money,"$")
            print()


        else:

            print("perdiste!  ->  -",bet,"$")
            print()
            money -= bet
            print("tienes",money,"$")
            print()


    #* se determina el final del juego o el reinicio del mismo

    #* end or restart the game is decided


    if money <= 0:

        print("no tienes dinero, no puedes seguir jugando :'(")
        break

    answ = input("¿quieres volver a apostar?: ")
    print()

    while answ != "si" and answ != "no":

        answ = input("elije si o no: ")
        print()

    if answ == "si":

        continue

    elif answ == "no":

        print("gracias por jugar! :)")
        break