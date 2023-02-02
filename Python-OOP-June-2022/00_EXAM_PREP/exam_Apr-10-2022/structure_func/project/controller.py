from project.player import Player
# from project.supply.supply import Supply
# from project.supply.drink import Drink
# from project.supply.food import Food


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        added_players = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(p for p in added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    @staticmethod
    def __find_player_by_name(name, players):
        for player in players:
            if player.name == name:
                return player
        return None

    @staticmethod
    def __type_in_supplies(supplies, type_s):
        for product in supplies:
            if product.__class__.__name__ == type_s:
                return True
        return False

    def sustain(self, player_name, sustenance_type: str):
        player = self.__find_player_by_name(player_name, self.players)
        valid_types = ('Food', 'Drink')
        if player is None:
            return
        if sustenance_type not in valid_types:
            return
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        last_supply, index = self.__find_last_supply(sustenance_type)
        if last_supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + last_supply.energy, Player.STAMINA_MAX)
        self.supplies.pop(index)

        return f"{player.name} sustained successfully with {last_supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.__find_player_by_name(first_player_name, self.players)
        second_player = self.__find_player_by_name(second_player_name, self.players)

        error_message = ''
        if self.__cannot_fight(first_player):
            error_message += f"Player {first_player.name} does not have enough stamina."
        if self.__cannot_fight(second_player):
            error_message += '\n' + f"Player {second_player.name} does not have enough stamina."
        if error_message:
            return error_message.strip()

        if second_player.stamina < first_player.stamina:
            second_player, first_player = first_player, second_player

        if self.__first_win(first_player, second_player):
            return f'Winner: {first_player.name}'

        if self.__first_win(second_player, first_player):
            return f'Winner: {second_player.name}'

        winner = first_player.name if first_player.stamina > second_player.stamina else second_player.name
        return f'Winner: {winner}'

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'
        return result.strip()


    def __find_last_supply(self, sustenance_type):
        for i in range(len(self.supplies) -1, -1, -1):
            supply = self.supplies[i]
            if supply.__class__.__name__ == sustenance_type:
                return supply, i
        return None, -1

    @staticmethod
    def __cannot_fight(player):
        return player.stamina == Player.STAMINA_MIN

    @staticmethod
    def __first_win(attacker, enemy):
        attacker_damage = attacker.stamina / 2
        enemy.stamina = max(0, enemy.stamina - attacker_damage)
        return enemy.stamina == 0
