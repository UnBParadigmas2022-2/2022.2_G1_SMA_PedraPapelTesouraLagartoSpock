from Models import *


def main():
    model = GameModel("Pedrao", "Bomsao")
    while model.isRunning:
        model.step()


if __name__ == "__main__":
    main()
