from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from keyboards import mainkeys, graphkeys

router = Router()  # [1]


@router.message(F.text.lower() == "raw dataset")
async def answer_raw(message: Message):
    rawdata = FSInputFile("rawdata.png")
    rawinfo = FSInputFile("rawinfo.png")
    
    await message.answer_photo(photo=rawinfo, caption="This table gives us all information about our dataset(<i>types of information, number of colomns and raws and their names</i>)",parse_mode=ParseMode.HTML)
    await message.answer_photo(photo=rawdata, caption="This chart shows first 20 rows of our dataset to understand which data we have.")

@router.message(F.text.lower() == "transformed dataset")
async def answer_new(message: Message):
    newdata = FSInputFile("newdata.png")
    newinfo = FSInputFile("newinfo.png")
    
    await message.answer_photo(photo=newinfo, caption="This table gives us all information about our transformed dataset(<i>types of information, number of colomns and raws and their names</i>)",parse_mode=ParseMode.HTML)
    await message.answer_photo(photo=newdata, caption="This chart shows first 20 rows of our transformed dataset with new colomns to understand which data we have")

@router.message(F.text.lower() == "general statistics")
async def answer_stat(message: Message):
    sumstat = FSInputFile("sumstat.png")
    lowstat = FSInputFile("lowstat.png")
    highstat = FSInputFile("highstat.png")
    
    await message.answer_photo(photo=sumstat, caption="General Statistic")
    await message.answer_photo(photo=lowstat, caption="Statistic which shows lowest percentage difference to US price")
    await message.answer_photo(photo=highstat, caption="Statistic which shows highest percentage difference to US price")


@router.message(F.text.lower() == "back to menu")
async def answer_menu(message: Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}\nWhat do you want to know about?",
        reply_markup=mainkeys()
        )