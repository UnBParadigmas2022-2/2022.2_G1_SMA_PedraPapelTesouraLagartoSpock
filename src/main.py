from Models import *
from os import system, name

def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def main():
    clearScreen()

    print("||||||||||||||||||||||||||||||||||||||||||||||||")
    print("PARTIDA 1:")
    Match1 = GameModel("Pedrao", "Bomsao")
    while Match1.isRunning:
        Match1.step()

    print("||||||||||||||||||||||||||||||||||||||||||||||||")
    print("PARTIDA 2:")
    Match2 = GameModel("Papelao", "Randao")
    while Match2.isRunning:
        Match2.step()
    print("||||||||||||||||||||||||||||||||||||||||||||||||")
    print("PARTIDA FINAL:")
    Final = GameModel(str(Match1.winner), str(Match2.winner))
    while Final.isRunning:
        Final.step()

    


if __name__ == "__main__":
    main()
