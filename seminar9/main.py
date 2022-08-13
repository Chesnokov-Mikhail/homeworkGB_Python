import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import view_pole as view
import games
import robot
import user
from random import randint

# Включаем логироывние через logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Старт игры крестики-нолики
def start_tic_tac_toe(update: Update, context: CallbackContext) -> None:
    # Задаем пользователю вопрос о начале игры с кнопками встроенной клавиатуры
    keyboard = [[InlineKeyboardButton("Да", callback_data='1'), InlineKeyboardButton("Нет", callback_data='0')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Играем крестики-нолики?', reply_markup=reply_markup)

# обратная функция на нажатие кнопок встроенной клавиатуры
def button(update: Update, context: CallbackContext) -> None:
    # получаем текст нажатой кнопки
    query = update.callback_query
    query.answer()
    # Анализируем ответ пользователя на запуск игры
    if query.data:
        games.init_games()
        query.edit_message_text(text='Введите размер поля командой /size , например /size 3: ')
    else:
        games.game_start = False

# Установка размера игрового поля
def set_size_pole(update: Update, context: CallbackContext) -> None:
    if games.game_start and games.old_command == '/start' and not games.game_exit:
        try:
            if len(context.args) > 1:
                raise
            else:
                size = int(context.args[0])
        except:
            update.message.reply_text('Введите одно целое число.')
        else:
            games.pole = games.pole_game_init(size)
            update.message.reply_text(view.view_pole_game())
            games.old_command = '/size'
            # Кто первый ходит, робот (0) или пользователь (1)
            games.next_move = randint(0, 1)
            if not games.next_move:
                update.message.reply_text('Первым ходит бот')
                step_bot(update, context)
            else:
                update.message.reply_text('Делайте первый ход, команда /step номер строки, номер столбца, например, /step 2 3 ')
    else:
        update.message.reply_text('Необходимо начать игру, /start')

# Ход пользователя
def step_user(update: Update, context: CallbackContext) -> None:
    # Если играем и ход пользователя
    if games.game_start and not games.game_exit and games.next_move:
        # если пользователем задан размер игрового поля или сделан первый шаг
        if games.old_command == '/size' or games.old_command == '/step':
            mark = 'X'
            result_step = user.user_input(games.pole, context.args)
            # если получены от пользователя координаты ячейки. иначе выводим информацию об ошибке
            if type(result_step) == tuple:
                games.old_command = '/step'
                games.pole_game_mark(result_step, mark)
                update.message.reply_text(view.view_pole_game())
                # проверяем концовку игры
                result_game_end = games.game_end(mark)
                if result_game_end:
                    update.message.reply_text(games.game_end(mark))
                # передаем ход боту
                games.next_move = not games.next_move
                step_bot(update, context)
            else:
                update.message.reply_text(result_step)
        else:
            update.message.reply_text('Вначале необходимо установить размер поля, /size')
    else:
        update.message.reply_text('Игра окончена')

# Ход бота
def step_bot(update: Update, context: CallbackContext) -> None:
    # Если играем и ход бота
    if games.game_start and not games.game_exit and not games.next_move:
        mark = '0'
        robot_move = robot.robot_game()
        (i, j) = robot_move
        games.pole_game_mark((i, j), mark)
        update.message.reply_text(view.view_pole_game())
        # проверяем концовку игры
        result_game_end = games.game_end(mark)
        if result_game_end:
            update.message.reply_text(games.game_end(mark))
        # передаем ход пользователю
        games.next_move = not games.next_move
        update.message.reply_text('Делайте ваш ход, команда /step номер строки, номер столбца, например, /step 2 3 ')
    else:
        update.message.reply_text('Игра окончена')

# Обработчик помощи
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('1. Используйте /start для игры в крестики-нолики. \n'
                        '2. Используйте /size для установки размера поля. \n'
                        '3. Используйте для хода команду /step номер_строки номер_столбца, например, /step 2 3')

# Обработчик текстовых сообщений пользователя
def user_text(update: Update, context: CallbackContext):
    update.message.reply_text('Это бот для игры в крестики-нолики. Наберите /help чтобы получить инструкцию к игре')

# Обработчик для неизвестной команды
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text('Неизвестная команда, не могу обработать')

if __name__ == '__main__':
# Регистрируем
    updater = Updater('5505901446:AAHK62fNeDiY21JKGwUKATs-YrwRcwH95f0')

# регистрируем обработчики команд и текстовых сообщений
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), user_text))
    dispatcher.add_handler(CommandHandler('start', start_tic_tac_toe))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler('size', set_size_pole))
    dispatcher.add_handler(CommandHandler('step', step_user))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    print('Server start')
    updater.start_polling()
    updater.idle()
