from mesa import Agent
from random import choice


class Randao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Randao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = choice(["pedra", "papel", "tesoura", "lagarto", "spock"])


class Pedrao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Pedrao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = "pedra"


class Papelao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.move = None
        self.name = "Papelao"
        self.previous_result = None
        # self.status = True

    def step(self):
        self.move = "papel"


class Bomsao(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.previous_move = ""
        self.previous_result = None
        self.move = None
        self.name = "Bomsao"
        # self.status = True
        self.moves = {
            "ganhou": {
                "pedra": ["lagarto", "tesoura"],
                "papel": ["pedra", "spock"],
                "tesoura": ["papel", "lagarto"],
                "lagarto": ["spock", "papel"],
                "spock": ["tesoura", "pedra"],
            },
            "perdeu": {
                "pedra": ["papel", "spock"],
                "papel": ["tesoura", "lagarto"],
                "tesoura": ["spock", "pedra"],
                "lagarto": ["pedra", "tesoura"],
                "spock": ["lagarto", "papel"],
            },
        }

    def step(self):
        if not self.previous_move or self.previous_result == "empate":
            self.move = choice(["pedra", "papel", "tesoura", "lagarto", "spock"])
        else:
            self.move = choice(self.moves[self.previous_result[self.previous_move]])
