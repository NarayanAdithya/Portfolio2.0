from . import bot
from app import db_m

@bot.route('/hello')
def bot_helloe():
    todos = db_m.todos
    todos.insert_one({'content': 'Trial', 'degree': 'Trial'})
    return "Bot Hello Here"