import telebot 
from config import token
from logic import Pokemon, Wizard, Fighter
from random import randint

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
      
        chance = randint(1, 4)  
        if chance == 1:
            pokemon = Wizard(message.from_user.username)
        elif chance == 2:
            pokemon = Fighter(message.from_user.username)
        else:  
            pokemon = Pokemon(message.from_user.username)
        
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if (message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and 
            message.from_user.username in Pokemon.pokemons.keys()):
            
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
        bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.info())
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['heal'])
def heal(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        heal_amount = randint(10, 30)
        pokemon.hp += heal_amount
        bot.send_message(message.chat.id, f"❤️ Твой покемон восстановил {heal_amount} HP!\nТеперь у него {pokemon.hp} здоровья")
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['mypokemon'])
def mypokemon(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        
       
        if isinstance(pokemon, Wizard):
            ptype = "🧙‍♂️ Волшебник"
        elif isinstance(pokemon, Fighter):
            ptype = "⚔️ Боец"
        else:
            ptype = "🎯 Обычный"
            
        response = f"{ptype}\n"
        response += f"📛 Имя: {pokemon.name}\n"
        response += f"⚡ Тип: {pokemon.type}\n"
        response += f"❤️ HP: {pokemon.hp}\n"
        response += f"💪 Сила: {pokemon.power}"
        
        bot.send_message(message.chat.id, response)
    else:
        bot.reply_to(message, "У тебя нет покемона! Создай командой /go")

bot.infinity_polling(none_stop=True)