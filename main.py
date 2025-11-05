import telebot 
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "❌ Ты уже создал себе покемона!")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.get_full_info())
    else:
        bot.reply_to(message, "❌ Сначала создай покемона командой /go")


@bot.message_handler(commands=['mypokemon'])
def mypokemon(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        response = f" Твой покемон:\n"
        response += f" Имя: {pokemon.name.title()}\n"
        response += f" Тип: {pokemon.type}\n"
        response += f" HP: {pokemon.hp}\n"
        response += f" Атака: {pokemon.attack}\n"
        response += f" Защита: {pokemon.defense}"
        bot.send_message(message.chat.id, response)
    else:
        bot.reply_to(message, "❌ У тебя нет покемона! Создай командой /go")

@bot.message_handler(commands=['allpokemons'])
def allpokemons(message):
    if not Pokemon.pokemons:
        bot.reply_to(message, "📭 Пока никто не создал покемонов!")
        return
    
    pokemon_list = "🎮 Все покемоны в игре:\n\n"
    for username, pokemon in Pokemon.pokemons.items():
        pokemon_list += f"👤 @{username}: {pokemon.name.title()} ({pokemon.type})\n"
    
    bot.send_message(message.chat.id, pokemon_list)

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """
 КОМАНДЫ ПОКЕМОН БОТА:

/go - 🎯 Создать своего покемона
/info - 📊 Полная информация о покемоне
/mypokemon - 👤 Мой покемон
/allpokemons - 📋 Список всех покемонов
/help - 🆕 Помощь по командам

    """
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = f"""
👋 Привет, {message.from_user.first_name}!

Я - Покемон Бот! 🎮
Создай своего покемона и сражайся с друзьями!

📝 Используй /go чтобы начать
🆕 Нужна помощь? /help
    """
    bot.send_message(message.chat.id, welcome_text)

bot.infinity_polling(none_stop=True)