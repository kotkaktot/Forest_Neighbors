from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN, OWNER_ID
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
import keyboards as kb
from utils import States
from connections import get_db_session
from model import Users
import logging
from datetime import datetime
import os

# Init
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename='{}/logs/logs_{}.log'.format(BASE_DIR, datetime.today().strftime('%Y%m%d')),
                    format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)
session = get_db_session(expire_on_commit=False)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# dp.middleware.setup(LoggingMiddleware())


def db_write_user(data):
    summary = Users(**data)
    session.add(summary)

    # pushing data to db
    session.commit()
    session.close()


@dp.message_handler(state=States.STATE_REG_B1)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if message.text == '*':
        await state.reset_state()
        await bot.send_message(message.from_user.id, 'Ваша регистрация отмена.')
        return
    else:
        try:
            room = int(message.text)
            data = session.query(Users).filter(Users.room == room).filter(Users.build == 1).first()
            if data:
                await bot.send_message(message.from_user.id, 'К сожалению, такая квартира уже зарегистрирована'
                                                             ' в базе пользователем @{}.'.format(data.username))
                await state.reset_state()
                return
            else:
                db_write_user({'user_id': message.from_user.id,
                               'first_name': message.from_user.first_name,
                               'last_name': message.from_user.last_name,
                               'username': message.from_user.username,
                               'build': 1,
                               'room': room})

                await bot.send_message(message.from_user.id, 'Спасибо! Мы зарегистрировали Вашего пользователя telegram'
                                                             ' как соседа из квартиры {}.'.format(room))
                await state.reset_state()
                return
        except:
            await bot.send_message(message.from_user.id, 'Номер квартиры задан не верно, '
                                                         'введите число без каких-либо дополнительных символов.'
                                                         ' Например «123».')


@dp.message_handler(state=States.STATE_REG_B2)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if message.text == '*':
        await state.reset_state()
        await bot.send_message(message.from_user.id, 'Ваша регистрация отмена.')
        return
    else:
        try:
            room = int(message.text)
            data = session.query(Users).filter(Users.room == room).filter(Users.build == 2).first()
            if data:
                await bot.send_message(message.from_user.id, 'К сожалению, такая квартира уже зарегистрирована'
                                                             ' в базе пользователем @{}.'.format(data.username))
                await state.reset_state()
                return
            else:
                db_write_user({'user_id': message.from_user.id,
                               'first_name': message.from_user.first_name,
                               'last_name': message.from_user.last_name,
                               'username': message.from_user.username,
                               'build': 2,
                               'room': room})

                await bot.send_message(message.from_user.id, 'Спасибо! Мы зарегистрировали Вашего пользователя telegram'
                                                             ' как соседа из квартиры {}.'.format(room))
                await state.reset_state()
                return
        except:
            await bot.send_message(message.from_user.id, 'Номер квартиры задан не верно, '
                                                         'введите число без каких-либо дополнительных символов.'
                                                         ' Например «123».')


@dp.message_handler(state=States.STATE_REG_B3)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if message.text == '*':
        await state.reset_state()
        await bot.send_message(message.from_user.id, 'Ваша регистрация отмена.')
        return
    else:
        try:
            room = int(message.text)
            data = session.query(Users).filter(Users.room == room).filter(Users.build == 3).first()
            if data:
                await bot.send_message(message.from_user.id, 'К сожалению, такая квартира уже зарегистрирована'
                                                             ' в базе пользователем @{}.'.format(data.username))
                await state.reset_state()
                return
            else:
                db_write_user({'user_id': message.from_user.id,
                               'first_name': message.from_user.first_name,
                               'last_name': message.from_user.last_name,
                               'username': message.from_user.username,
                               'build': 3,
                               'room': room})

                await bot.send_message(message.from_user.id, 'Спасибо! Мы зарегистрировали Вашего пользователя telegram'
                                                             ' как соседа из квартиры {}.'.format(room))
                await state.reset_state()
                return
        except:
            await bot.send_message(message.from_user.id, 'Номер квартиры задан не верно, '
                                                         'введите число без каких-либо дополнительных символов.'
                                                         ' Например «123».')


@dp.message_handler(state=States.STATE_SRCH_B1)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if message.text == '*':
        await state.reset_state()
        await bot.send_message(message.from_user.id, 'Ваш поиск отменён.')
        return
    else:
        try:
            room = int(message.text)
            data = session.query(Users).filter(Users.room == room).filter(Users.build == 1).first()
            if data:
                msg_text = 'Ура! Сосед нашелся:\n\n' \
                           'Корпус 1\n' \
                           'Квартира {}\n' \
                           'Сосед @{}'.format(room, data.username)
                await bot.send_message(message.from_user.id, msg_text)
                await state.reset_state()
                return
            else:
                await bot.send_message(message.from_user.id, 'Соседи из квартиры {} в базе не найдены. '
                                                             'Для отмены поиска введите «*» или введите другой'
                                                             ' номер квартиры:'.format(room))
        except:
            await bot.send_message(message.from_user.id, 'Номер квартиры задан не верно, '
                                                         'введите число без каких-либо дополнительных символов.'
                                                         ' Например «123».')


@dp.message_handler(state=States.STATE_SRCH_B2)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if message.text == '*':
        await state.reset_state()
        await bot.send_message(message.from_user.id, 'Ваш поиск отменён.')
        return
    else:
        try:
            room = int(message.text)
            data = session.query(Users).filter(Users.room == room).filter(Users.build == 2).first()
            if data:
                msg_text = 'Ура! Сосед нашелся:\n\n' \
                           'Корпус 2\n' \
                           'Квартира {}\n' \
                           'Сосед @{}'.format(room, data.username)
                await bot.send_message(message.from_user.id, msg_text)
                await state.reset_state()
                return
            else:
                await bot.send_message(message.from_user.id, 'Соседи из квартиры {} в базе не найдены. '
                                                             'Для отмены поиска введите «*» или введите другой'
                                                             ' номер квартиры:'.format(room))
        except:
            await bot.send_message(message.from_user.id, 'Номер квартиры задан не верно, '
                                                         'введите число без каких-либо дополнительных символов.'
                                                         ' Например «123».')


@dp.message_handler(state=States.STATE_SRCH_B3)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    if message.text == '*':
        await state.reset_state()
        await bot.send_message(message.from_user.id, 'Ваш поиск отменён.')
        return
    else:
        try:
            room = int(message.text)
            data = session.query(Users).filter(Users.room == room).filter(Users.build == 3).first()
            if data:
                msg_text = 'Ура! Сосед нашелся:\n\n' \
                           'Корпус 3\n' \
                           'Квартира {}\n' \
                           'Сосед @{}'.format(room, data.username)
                await bot.send_message(message.from_user.id, msg_text)
                await state.reset_state()
                return
            else:
                await bot.send_message(message.from_user.id, 'Соседи из квартиры {} в базе не найдены. '
                                                             'Для отмены поиска введите «*» или введите другой'
                                                             ' номер квартиры:'.format(room))
        except:
            await bot.send_message(message.from_user.id, 'Номер квартиры задан не верно, '
                                                         'введите число без каких-либо дополнительных символов.'
                                                         ' Например «123».')


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_btn_profile(callback_query: types.CallbackQuery):
    user_id = callback_query.message.chat.id
    state = dp.current_state(user=user_id)
    button_name = callback_query.data[4:]

    await bot.answer_callback_query(callback_query.id)

    if button_name == 'build1':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали *КОРПУС 1*', parse_mode=ParseMode.MARKDOWN)

        await bot.send_message(callback_query.from_user.id, 'Введите номер квартиры для окончания регистрации или'
                                                            ' символ «*» для отмены:')
        await state.set_state(States.STATE_REG_B1)
    elif button_name == 'build2':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали *КОРПУС 2*', parse_mode=ParseMode.MARKDOWN)

        await bot.send_message(callback_query.from_user.id, 'Введите номер квартиры для окончания регистрации или'
                                                            ' символ «*» для отмены:')
        await state.set_state(States.STATE_REG_B2)
    elif button_name == 'build3':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали *КОРПУС 3*', parse_mode=ParseMode.MARKDOWN)

        await bot.send_message(callback_query.from_user.id, 'Введите номер квартиры для окончания регистрации или'
                                                            ' символ «*» для отмены:')
        await state.set_state(States.STATE_REG_B3)
    elif button_name == 'build1_search':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали *КОРПУС 1*', parse_mode=ParseMode.MARKDOWN)

        await bot.send_message(callback_query.from_user.id, 'Введите искомый номер квартиры или'
                                                            ' символ «*» для отмены:')
        await state.set_state(States.STATE_SRCH_B1)
    elif button_name == 'build2_search':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали *КОРПУС 2*', parse_mode=ParseMode.MARKDOWN)

        await bot.send_message(callback_query.from_user.id, 'Введите искомый номер квартиры или'
                                                            ' символ «*» для отмены:')
        await state.set_state(States.STATE_SRCH_B2)
    elif button_name == 'build3_search':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали *КОРПУС 3*', parse_mode=ParseMode.MARKDOWN)

        await bot.send_message(callback_query.from_user.id, 'Введите искомый номер квартиры или'
                                                            ' символ «*» для отмены:')
        await state.set_state(States.STATE_SRCH_B3)

    await callback_query.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.reply('Привет! Я бот соседей ЖК FoRest.\n\n'
                    'С помощью меня Вы сможете найти соседа по номеру квартиры,'
                    ' а также поделиться своими данными с остальными.\n\n'
                    'Всё необходимое Вы сможете найти в навигационном меню 👇', reply_markup=kb.main_kb)


@dp.message_handler()
async def text_message(msg: types.Message):
    if msg.text == '🙋 Регистрация':
        data = session.query(Users).filter(Users.user_id == msg.from_user.id).first()
        if data:
            await msg.reply(text='Вы уже зарегистрированы в базе, как собственник квартиры {}'.format(data.room))
        else:
            await msg.reply('Выполняя регистрацию Вы соглашаетесь с '
                            'политикой обработки и раскрытия персональных данных.\n\n'
                            'https://docs.google.com/document/d/1BLFumis5xte8XbXfyj7R6NNbz2WQUcbWk9dpkPA4Lmw/edit?usp=sharing')
            await msg.reply(text='Выберите Ваш корпус:', reply_markup=kb.inline_kb_buildings)
    elif msg.text == '🕵️ Поиск соседа':
        await msg.reply(text='Выберите корпус:', reply_markup=kb.inline_kb_buildings_search)

    # state = dp.current_state(user=msg.from_user.id)
    # print(await state.get_state())


if __name__ == '__main__':
    executor.start_polling(dp)
