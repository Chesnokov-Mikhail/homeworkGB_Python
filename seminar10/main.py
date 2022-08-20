import logging
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import os.path

import common_function
import controller
import menu
import io
from contextlib import redirect_stdout
import export_bd

# Включаем логирование через logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Старт работы с ИС сотрудники
def start(update: telegram.Update, context: CallbackContext):
    # Перенаправляем стандартный вывод в stdout (например через print()) в строковую переменную
    with io.StringIO() as buf, redirect_stdout(buf):
        controller.prog_run()
        output = buf.getvalue()
    update.message.reply_text(output)

# Выбор пункта меню
def choice_menu(update: telegram.Update, context: CallbackContext):
    if controller.start_prog:
        try:
            if len(context.args) > 1:
                raise
            elif len(context.args) == 0:
                choice = -1
            else:
                choice = int(context.args[0])
        except:
            update.message.reply_text('Введите одно целое число.')
        else:
            # Перенаправляем стандартный вывод в stdout (например через print()) в строковую переменную
            with io.StringIO() as buf, redirect_stdout(buf):
                result = controller.choice_menu(choice, update, context)
                output = buf.getvalue()
            if controller.menu_select in [menu.menu_export, menu.menu_person]:
                if result:
                    if os.path.exists(result):
                        with open(result, 'r') as fr:
                            context.bot.send_document(chat_id=update.effective_chat.id, document=fr)
            # Проверяем что сообщение не превышает максимальную длину сообщения в символах.
            # При превышении отправляется ответ в виде файла txt
            if len(output) > telegram.constants.MAX_MESSAGE_LENGTH:
                output_file = export_bd.export_to_txt(output)
                with open(output_file,'r') as fr:
                    context.bot.send_document(chat_id=update.effective_chat.id,document=fr)
                    update.message.reply_text('Ответ большой, поэтому предоставлен в виде файла')
            else:
                if output:
                    update.message.reply_text(output)
    else:
        user_text(update, context)

# Вывод пользователю информации по связным таблицам в БД
def view_question_data(update: telegram.Update, context: CallbackContext, output):
    # Проверяем что сообщение не превышает максимальную длину сообщения в символах.
    # При превышении отправляется ответ в виде файла txt
    if len(output) > telegram.constants.MAX_MESSAGE_LENGTH:
        output_file = export_bd.export_to_txt(output)
        with open(output_file, 'r') as fr:
            context.bot.send_document(chat_id=update.effective_chat.id, document=fr)
            update.message.reply_text('Ответ большой, поэтому предоставлен в виде файла')
    else:
        if output:
            update.message.reply_text(output)

# Сообщение пользователю по результатам изменения данных в БД
def answer_document_data(update: telegram.Update, context: CallbackContext, output):
    if output:
        output_file = export_bd.export_to_txt(output)
        with open(output_file,'r') as fr:
            context.bot.send_document(chat_id=update.effective_chat.id,document=fr)

# Обработчик помощи
def help_command(update: telegram.Update, context: CallbackContext):
    update.message.reply_text('1. Используйте /start для начала работы с ИС "Сотрудники" \n'
                              '2. Используйте /menu <номер пункта> для перехода/выбора необходимого пункта меню \n'
                              '3. Используйте /menu для перехода в главное меню \n')

# Запрос данных у пользователя по полям модели данных
def question_field_model(update: telegram.Update, context: CallbackContext, model_record, key):
    update.message.reply_text(f'Введите {model_record[key][1].capitalize()}, не более {model_record[key][2]} символов: ')

# Запрос у пользователя дентификатора записи модели данных
def question_id_record_model(update: telegram.Update, context: CallbackContext, model_record, key):
    update.message.reply_text(f'Введите {model_record[key][1]}: ')

# Запрос у пользователя дентификатора записи модели связных данных
def question_id_record_rel_model(update: telegram.Update, context: CallbackContext, model_record, key, val_key):
    if val_key:
        update.message.reply_text(f'Введите {model_record[key][1]}, текущее значение {val_key}: ')
    else:
        update.message.reply_text(f'Введите {model_record[key][1]}, значение ещё не присвоено: ')

# Запрос у пользователя данных для поиска записи модели данных
def question_search_record_model(update: telegram.Update, context: CallbackContext, model_record, key):
    update.message.reply_text(f'Введите данные для поиска по полю "{model_record[key][1]}": ')

# Сообщение пользователю по результатам изменения данных в БД
def answer_save_model(update: telegram.Update, context: CallbackContext, id):
    if id:
        update.message.reply_text(f'Данные сохранены под № {id}')
    else:
        update.message.reply_text(f'Ошибка записи данных с № {id}')

# Обработчик текстовых сообщений пользователя
def user_text(update: telegram.Update, context: CallbackContext):
    # Если работа с ИС Сотрудники начата
    if controller.start_prog:
        # Перенаправляем стандартный вывод в stdout (например через print()) в строковую переменную
        with io.StringIO() as buf, redirect_stdout(buf):
            # Анализ ввода данных по внесению данных по полям моделей БД
            if controller.model_select and controller.key_model and controller.record_model and controller.key_model_select:
                new_value = update.message.text.strip()
                if new_value:
                    controller.record_model[controller.key_model] = \
                        controller.model_select[controller.key_model][0](new_value,
                                                                                controller.model_select[controller.key_model][2])
                if not controller.record_model[controller.key_model]:
                    update.message.reply_text('Ошибка в формате данных. Повторите ввод или выберите выход.')
                # Если ошибок нет, то переходим к следующему полю в модели
                else:
                    if controller.model_record_rel_select:
                        if not common_function.record_get_id(controller.record_model[controller.key_model],
                                                      controller.model_select[controller.key_model][4].bd_path,
                                                    controller.model_select[controller.key_model][4].primary_key):
                            update.message.reply_text('Запись с № {new_value} не найдена в БД'
                                                      ' {controller.model_select[controller.key_model][4].bd_path}. '
                                                      'Повторите ввод или выберите выход.')
                        else:
                            controller.telegram_get_field_model(update, context, controller.model_select,
                                                                controller.record_model,
                                                                controller.bd_path, controller.primary_key)
                    else:
                        controller.telegram_get_field_model(update, context, controller.model_select,
                                                            controller.record_model,
                                                            controller.bd_path, controller.primary_key)
            # Ввод идентификатора записи модели данных
            elif controller.model_select and controller.key_model == controller.primary_key[0] and controller.record_model:
                new_value = update.message.text.strip()
                if new_value:
                    controller.record_model[controller.key_model] = controller.model_select[controller.key_model][0](new_value,
                                                                                controller.model_select[controller.key_model][2])
                if not controller.record_model[controller.key_model]:
                    update.message.reply_text('Ошибка в формате данных. Повторите ввод или выберите выход.')
                else:
                    controller.get_record_model(update, context, controller.model_select, controller.record_model,
                                                        controller.bd_path, controller.primary_key)
            # Ввод для поиска записи модели данных
            elif controller.model_select and controller.key_model and not controller.record_model:
                new_value = update.message.text.strip()
                if new_value:
                     new_value = controller.model_select[controller.key_model][0](new_value,
                                                                    controller.model_select[controller.key_model][2])
                if not new_value:
                    update.message.reply_text('Ошибка в формате данных. Повторите ввод или выберите выход.')
                else:
                    controller.view_search_record_model(update, context, controller.model_select, controller.record_model,
                                                controller.bd_path, controller.primary_key, new_value)
            output = buf.getvalue()
        if output:
            update.message.reply_text(output)
#        update.message.reply_text('Для продолжения работы с ИС "Сотрудники", наберите /help чтобы получить инструкции')
    else:
        update.message.reply_text('Это бот для работы с ИС "Сотрудники". Наберите /help чтобы получить инструкции')

# Обработчик для неизвестной команды
def unknown(update: telegram.Update, context: CallbackContext):
    update.message.reply_text('Неизвестная команда, не могу обработать')

if __name__ == '__main__':
# Регистрируем
    updater = Updater('5505901446:AAHK62fNeDiY21JKGwUKATs-YrwRcwH95f0')

# регистрируем обработчики команд и текстовых сообщений
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), user_text))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('menu', choice_menu))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    print('Server start')
    updater.start_polling()
    updater.idle()
