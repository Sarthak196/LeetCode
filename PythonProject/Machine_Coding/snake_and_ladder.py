import random

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

class Player():
    def __init__(self):
        self.name = input("Enter player name: ")
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position > 100:
            self.position = 100 - (self.position - 100)

        elif self.position in snakes:
            print(f"{self.name} encountered a snake! Moving down from {self.position} to {snakes[self.position]}.")
            self.position = snakes[self.position]

        elif self.position in ladders:
            print(f"{self.name} found a ladder! Moving up from {self.position} to {ladders[self.position]}.")
            self.position = ladders[self.position]

    def __str__(self):
        return f"{self.name} is at position {self.position}."

class Game():
    def __init__(self):
        self.players = []
        self.current_player_index = 0

    def add_player(self):
        player = Player()
        self.players.append(player)

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        steps = self.roll_dice()
        print(f"{current_player.name} rolled a {steps}.")
        current_player.move(steps)
        print(current_player)

        if current_player.position == 100:
            print(f"{current_player.name} wins!")
            return True

        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return False

def main():
    game = Game()
    num_players = int(input("Enter number of players: "))

    for _ in range(num_players):
        game.add_player()

    while True:
        if game.play_turn():
            break

    print("Game over!")

if __name__ == "__main__":
    main()

