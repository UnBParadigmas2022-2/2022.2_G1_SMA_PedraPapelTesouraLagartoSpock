from mesa import Model
from Agents import *
from mesa.time import RandomActivation
from time import sleep


class GameModel(Model):
    def __init__(self, player1, player2):
        self.isRunning = True
        self.schedule = RandomActivation(self)
        self.players = []
        self.i = 1
        self.round = 1
        self.possible_players = {
            "Pedrao": Pedrao,
            "Papelao": Papelao,
            "Randao": Randao,
            "Bomsao": Bomsao,
            "Arnaldo": Arnaldo,
            "Ruanzão": Ruanzão,

        }
        self.player1_wins = 0
        self.player2_wins = 0

        self.players.append(self.possible_players[player1](self.i, self))
        self.i += 1
        self.players.append(self.possible_players[player2](self.i, self))
        for player in self.players:
            self.schedule.add(player)

    def step(self):
        self.schedule.step()

        # Determine o vencedor aqui
        player1 = self.players[0]
        player2 = self.players[1]

        if self.player1_wins < 3 and self.player2_wins < 3:
            print(f"Rodada: {self.round}")
            self.round += 1
            print(f"{player1.name} jogou {player1.move}!\t{player2.name} jogou {player2.move}!")
            if player1.move == player2.move:
                print("Empate!")
                player1.previous_result = "empate"
                player2.previous_result = "empate"
            elif (
                (player1.move == "pedra" and player2.move == "tesoura")
                or (player1.move == "pedra" and player2.move == "lagarto")
                or (player1.move == "papel" and player2.move == "pedra")
                or (player1.move == "papel" and player2.move == "spock")
                or (player1.move == "tesoura" and player2.move == "papel")
                or (player1.move == "tesoura" and player2.move == "lagarto")
                or (player1.move == "spock" and player2.move == "tesoura")
                or (player1.move == "spock" and player2.move == "pedra")
                or (player1.move == "lagarto" and player2.move == "papel")
                or (player1.move == "lagarto" and player2.move == "spock")
            ):
                print(f"{player1.name} ganhou!")
                player1.previous_result = "ganhou"
                player2.previous_result = "perdeu"
                self.player1_wins += 1
                # self.players[1].status = False
            else:
                print(f"{player2.name} ganhou!")
                player1.previous_result = "perdeu"
                player2.previous_result = "ganhou"
                self.player2_wins += 1
                # self.players[0].status = False
        else:
            self.isRunning = False
            if self.player1_wins - self.player2_wins > 0:
                print(f"{player1.name} ganhou a partida!")
                self.winner = player1.name
            else:
                print(f"{player2.name} ganhou a partida!")
                self.winner = player2.name
        print()
        # sleep(2)
