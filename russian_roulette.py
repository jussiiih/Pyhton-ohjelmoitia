from random import randint, shuffle

class RussianRoulette:
    def __init__ (self, player_list):
        self.players_in_game = {}
        self.result = {}
        self.dead_players = {}
        self.order_list = []
        self.bullet_in_chamber = 0
        self.current_chamber = 1
        for player in player_list:
            self.players_in_game[player] = 0

    def start_game (self):
        print('Lets play Russian roulette!')
        self.order_list = list(self.players_in_game.keys())
        shuffle(self.order_list)
        self.bullet_in_chamber = randint(1,6)
        self.loop()
        
        
    def loop(self):
      #  while True:
            self.choice(self.order_list[0])
        
    def choice(self, player):
        print('#######')
        print(f"It's {player}'s turn")
        choice = input('Type shoot or quit!: ')
        #choice = "quit"
        if choice.lower() == 'shoot':
            self.pull_trigger(player)
        elif choice.lower() == 'quit':
            self.quit(player)
        else:
            print('Incorrect command, try again!')

    def quit(self, player):
        self.result[player] = self.players_in_game[player]
        self.order_list.pop(0)
        del self.players_in_game[player]
        print('#######')
        print (f'{player} quitted with {self.result[player]} points')
        if len(self.players_in_game) == 0:
            self.game_over()
        else:
             self.show_remainig_score()
             self.loop()


    def pull_trigger(self, player):
        if self.current_chamber == self.bullet_in_chamber:
            self.current_chamber += 1
            self.gun_shoots(player)
        else:
            self.current_chamber += 1
            self.gun_misses(player)

    def gun_shoots(self, player):
        self.dead_players[player] = self.players_in_game[player]
        del self.players_in_game[player]
        self.order_list.pop(0)
        print('BANG!')
        print(f'{player} is out of roulette!')
        for player_remaining in self.players_in_game:
            self.result[player_remaining] = self.players_in_game[player_remaining]
        self.game_over()

    def gun_misses (self, player):
        print(f'PHEOW!\nNo bullet in chamber and {player} earns 100 points!')
        self.players_in_game[player] += 100
        self.order_list.append(player)
        self.order_list.pop(0)
        if len(self.players_in_game) == 0:
            self.game_over()
        else:
            self.show_remainig_score()
            self.loop()

    def game_over (self):
        print('RESULTS')
        
        print('#######')
        print('Alive Players')
        alive_players = self.result.items()
        for player in alive_players:
            print(f'{player[0]}, {player[1]} points')
        print('#######')
        print('Dead Players')
        dead_players = self.dead_players.items()
        for player in dead_players:
            print(f'{player[0]}, {player[1]} points')
        print('#######')

    def show_remainig_score(self):
        print('#######')
        print('Players still in the game:')
        remaining_players = self.players_in_game.items()
        for remaining_player in remaining_players:
            print(f'{remaining_player[0]}: {remaining_player[1]} points')
        

players = []
print('Welcome to Russian roulette!')
print('#######')
print('RULES')
print('#######')
print('In your turn you can either quit or shoot.')
print('If you miss a bullet, you earn 100 points')
print('Alive player with most points win!')
print('#######')

while True:
    player_input = input('Type player name. If all players are inputted, type GO to start the game. ')
    if player_input.lower() == 'go':
        break
    else:
        players.append(player_input)
shuffle(players)
game = RussianRoulette(players)
game.start_game()


