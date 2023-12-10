from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from keyboards import graphkeys, mainkeys

router = Router()  # [1]


@router.message(F.text.lower() == "main analysis")
async def answer_analysis(message: Message):
    heatmap = FSInputFile("heatmap.png")
    pairplot = FSInputFile("pairplot.png")
    scatter = FSInputFile("scatter.png")
    
    await message.answer_photo(photo=heatmap, caption="Heatmap Graphic: it displays the correlation between different pairs of variables.\nFor example we can note positive correlation between GDP and dollar price.")
    await message.answer_photo(photo=pairplot, caption="Pairplot Graphic: this graphic shows relationshiop among all variables in different ways")
    await message.answer_photo(photo=scatter, caption="Scatter Graphic: it illustrates the correspondence between Raw Value and Gdp Per Capita")
    

@router.message(F.text.lower() == "comparison")
async def answer_comparison(message: Message):
    map = FSInputFile("map.mp4")
    histprice = FSInputFile("histprice.png")
    histvalue = FSInputFile("histvalue.png")
    numbigmac = FSInputFile("numbigmac.png")
    
    await message.answer_video(video=map, caption="Worldwide Graphic: it displays the number of USD Raw in percentage in every country in the period between 2000 and 2022")
    await message.answer_photo(photo=histprice, caption="Hystogram Graphic: this graphic shows difference between prices of Big Mac in 2021 and 2022 ")
    await message.answer_photo(photo=histvalue, caption="Hystogram Graphic: it illustrates number of repetitions of USD Raw and USD Adjusted values")
    await message.answer_photo(photo=numbigmac, caption="Horyzontal Bar Chart: this chart demonstrates number of Big Macs that can be bought in local currency for the price of one burger in America")

@router.message(F.text.lower() == "back to menu")
async def answer_menu(message: Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}\nWhat do you want to know about?",
        reply_markup=mainkeys()
        )