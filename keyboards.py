from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

reg_button = KeyboardButton('🙋 Регистрация')
check_button = KeyboardButton('🕵️ Поиск соседа')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.row(reg_button, check_button)

inline_btn_build1 = InlineKeyboardButton('Корпус 1', callback_data='btn_build1')
inline_btn_build2 = InlineKeyboardButton('Корпус 2', callback_data='btn_build2')
inline_btn_build3 = InlineKeyboardButton('Корпус 3', callback_data='btn_build3')
inline_kb_buildings = InlineKeyboardMarkup(row_width=1).add(inline_btn_build1,
                                                            inline_btn_build2,
                                                            inline_btn_build3)

inline_btn_build1_search = InlineKeyboardButton('Корпус 1', callback_data='btn_build1_search')
inline_btn_build2_search = InlineKeyboardButton('Корпус 2', callback_data='btn_build2_search')
inline_btn_build3_search = InlineKeyboardButton('Корпус 3', callback_data='btn_build3_search')
inline_kb_buildings_search = InlineKeyboardMarkup(row_width=1).add(inline_btn_build1_search,
                                                            inline_btn_build2_search,
                                                            inline_btn_build3_search)
