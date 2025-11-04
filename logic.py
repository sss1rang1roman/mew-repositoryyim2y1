from random import randint
import requests

class Pokemon:
    pokemons = {}
    
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1, 1000)
        
       
        self.name = self.get_name()
        self.img = self.get_img()
        self.type = self.get_type()
        self.hp = self.get_hp()
        self.attack = self.get_attack()
        self.defense = self.get_defense()
        
        Pokemon.pokemons[pokemon_trainer] = self

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"

    def get_type(self):
        """ тип покемона"""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['types'][0]['type']['name']
        else:
            return "electric"

    def get_hp(self):
        """ HP покемона"""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'hp':
                    return stat['base_stat']
        return 50

    def get_attack(self):
        """атаку покемона"""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'attack':
                    return stat['base_stat']
        return 50

    def get_defense(self):
        """ защиту покемона"""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'defense':
                    return stat['base_stat']
        return 50


    def info(self):
        return f"Имя  покемона: {self.name}"

    def show_img(self):
        return self.img

    def get_full_info(self):
        """ информация о покемоне"""
        return f"""
🐾 {self.name.capitalize()}
⚡ Тип: {self.type}
❤️ HP: {self.hp}
⚔️ Атака: {self.attack}
🛡️ Защита: {self.defense}
        """
