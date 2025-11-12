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
        
        self.hp = randint(50, 100)  
        self.power = randint(10, 30)  
        
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
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['types'][0]['type']['name']
        else:
            return "electric"

    def info(self):
        return f"Имя твоего покемона: {self.name}\n❤️ Здоровье: {self.hp}\n💪 Сила: {self.power}"

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    def show_img(self):
        return self.img

class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp = randint(80, 120)
        self.power = randint(5, 20)

    def info(self):
        base_info = super().info()
        return f"У тебя покемон-волшебник\n{base_info}"

    def attack(self, enemy):
        return super().attack(enemy)

class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.hp = randint(40, 80)
        self.power = randint(25, 40)

    def info(self):
        base_info = super().info()
        return f"У тебя покемон-боец\n{base_info}"

    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "


if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))