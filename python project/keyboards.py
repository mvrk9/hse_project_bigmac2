from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder



def mainkeys() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="INFO")
    kb.button(text="DATASET")
    kb.button(text="GRAPHICS")
    kb.button(text="HYPOTHESIS")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def graphkeys() -> ReplyKeyboardMarkup:
   kb = ReplyKeyboardBuilder()
   kb.button(text="MAIN ANALYSIS")
   kb.button(text="COMPARISON")
   kb.button(text="BACK TO MENU")
   kb.adjust(2)
   return kb.as_markup(resize_keyboard=True)

def datakeys() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="GENERAL STATISTICS")
    kb.button(text="RAW DATASET")
    kb.button(text="TRANSFORMED DATASET")
    kb.button(text="BACK TO MENU")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)