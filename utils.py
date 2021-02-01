from aiogram.utils.helper import Helper, HelperMode, ListItem, Item


class States(Helper):
    mode = HelperMode.snake_case
    STATE_REG_B1 = Item()
    STATE_REG_B2 = Item()
    STATE_REG_B3 = Item()
    STATE_SRCH_B1 = Item()
    STATE_SRCH_B2 = Item()
    STATE_SRCH_B3 = Item()


if __name__ == '__main__':
    print(States.all())
