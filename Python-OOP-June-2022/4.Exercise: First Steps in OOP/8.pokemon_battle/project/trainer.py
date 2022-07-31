from project2 import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        self.pokemon_to_add = pokemon.name
        self.pokemon_full_info = pokemon.pokemon_details()
        if self.pokemon_to_add in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon.name)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):

        if pokemon_name not in self.pokemons:
            return "Pokemon is not caught"
        else:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemons)}\n'
        for _ in self.pokemons:
            result += f"- {self.pokemon_full_info}\n"

        return result
