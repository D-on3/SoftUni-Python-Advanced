class SteamUser:

    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        self.game = game
        self.hours = hours
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, new_game):
        self.add_game = new_game
        if new_game not in self.games:
            self.games.append(new_game)
            return f"{self.username} bought {new_game}"
        elif new_game in self.games:
            return f"{new_game} is already in your library"

    def status(self):

        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
