import telebot 
from config import token
from logic import Pokemon, Wizard, Fighter
from random import choice

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon_type = choice(['wizard', 'fighter', 'normal'])
        
        if pokemon_type == 'wizard':
            pokemon = Wizard(message.from_user.username)
        elif pokemon_type == 'fighter':
            pokemon = Fighter(message.from_user.username)
        else:
            pokemon = Pokemon(message.from_user.username)
        
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты еще не создал покемона")
        return
    
    if not message.reply_to_message:
        bot.reply_to(message, "Ответь на сообщение пользователя, чтобы атаковать его покемона!")
        return
    
    target_username = message.reply_to_message.from_user.username
    
    if target_username not in Pokemon.pokemons.keys():
        bot.reply_to(message, f"У этого пользователя нет покемона!")
        return
    
    if target_username == message.from_user.username:
        bot.reply_to(message, "Нельзя атаковать самого себя!")
        return
    
    attacker = Pokemon.pokemons[message.from_user.username]
    defender = Pokemon.pokemons[target_username]
    
    battle_result = attacker.attack(defender)
    bot.reply_to(message, battle_result)

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
    else:
        bot.reply_to(message, "Ты еще не создал покемона")

bot.infinity_polling(none_stop=True)