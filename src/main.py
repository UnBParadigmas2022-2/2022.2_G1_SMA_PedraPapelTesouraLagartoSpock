from Models import *
from os import system, name
import pyfiglet

listDisp = [0, 0, 0, 0, 0, 0, 0, 0]
partida1 = []
partida2 = []

def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def showPlayers():
    list = ["Pedrao", "Papelao", "Bomsao", "Randao", "Arnaldo", "Ruanzão", "Tesourao", "Empatao"]

    for p in range(len(list)):
        if listDisp[p] == 0:
            print(str(p+1)+". "+list[p])

def checkChoice(choice, partida):
    list = ["Pedrao", "Papelao", "Bomsao", "Randao", "Arnaldo", "Ruanzão", "Tesourao", "Empatao"] 
    if choice == 1 and listDisp[0] == 0:
        partida.append("Pedrao")
        listDisp[0] = 1
    elif choice == 2 and listDisp[1] == 0:
        partida.append("Papelao")
        listDisp[1] = 1
    elif choice == 3 and listDisp[2] == 0:
        partida.append("Bomsao")
        listDisp[2] = 1
    elif choice == 4 and listDisp[3] == 0:
        partida.append("Randao")
        listDisp[3] = 1
    elif choice == 5 and listDisp[4] == 0:
        partida.append("Arnaldo")
        listDisp[4] = 1
    elif choice == 6 and listDisp[5] == 0:
        partida.append("Ruanzão")
        listDisp[5] = 1
    elif choice == 7 and listDisp[6] == 0:
        partida.append("Tesourao")
        listDisp[6] = 1
    elif choice == 8 and listDisp[7] == 0:
        partida.append("Empatao")
        listDisp[7] = 1
    elif choice == 9:
        for i in range(len(listDisp)):
            if listDisp[i] == 0:
                partida.append(list[i])
                listDisp[i] = 1
                return 0
    else:
        return 1

    return 0

def menu():
    fim = 0
    players = 0
    
    while fim < 2:
        clearScreen()
        print("BEM VINDO AO TORNEIO DE")
        print(pyfiglet.figlet_format("PEDRA PAPEL TESOURA LAGARTO SPOCK", justify='center'))
        if fim == 0 and players == 0:
            print("ESCOLHA O PRIMEIRO PARTICIPANTE DA PARTIDA 1:")
            showPlayers()
            choice = input()
            if checkChoice(int(choice), partida1) != 1:
                print("JOGADOR ADICIONADO A PARTIDA 1")
                players+=1
        elif fim == 0 and players == 1:
            print("ESCOLHA O SEGUNDO PARTICIPANTE DA PARTIDA 1:")
            showPlayers()
            choice = input()
            if checkChoice(int(choice), partida1) != 1:
                print("JOGADOR ADICIONADO A PARTIDA 1")
                fim+=1
                players = 0        
        elif fim == 1 and players == 0:
            print("ESCOLHA O PRIMEIRO PARTICIPANTE DA PARTIDA 2:")
            showPlayers()
            choice = input()
            if checkChoice(int(choice), partida2) != 1:
                print("JOGADOR ADICIONADO A PARTIDA 2")
                players += 1


        elif fim == 1 and players == 1:
            print("ESCOLHA O ULTIMO PARTICIPANTE DA PARTIDA 2:")
            showPlayers()
            choice = input()
            if checkChoice(int(choice), partida2) != 1:
                print("JOGADOR ADICIONADO A PARTIDA 2")
                fim+=1
        print("p1 ", partida1)
        print("p2 ", partida2)
        
        sleep(1)

def main():
    clearScreen()
    menu()
    clearScreen()
    print("_______________________________________________________")
    print("PARTIDA 1:")
    print(partida1)
    Match1 = GameModel(partida1[0], partida1[1])
    while Match1.isRunning:
        Match1.step()

    print("_______________________________________________________")
    print("PARTIDA 2:")
    print(partida2)
    
    Match2 = GameModel(partida2[0], partida2[1])
    while Match2.isRunning:
        Match2.step()
    print("_______________________________________________________")
    print(pyfiglet.figlet_format("PARTIDA FINAL"))
    print(Match1.winner, Match2.winner)
    Final = GameModel(str(Match1.winner), str(Match2.winner))
    while Final.isRunning:
        Final.step()

    


if __name__ == "__main__":
    main()
