from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode

from keyboards import mainkeys, graphkeys, datakeys

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}\nWhat do you want to know about?",
        reply_markup=mainkeys()
    )

@router.message(F.text.lower() == "info")
async def answer_info(message: Message):
    await message.answer(
        "The Big Mac Index was created by The Economist magazine in 1986 as a means to evaluate purchasing-power parity in different currencies by comparing the price of a Big Mac.\n\nThe data includes the date the data was recorded, the local price, the dollar price (calculated using the dollar exchange rate at the time), the percentage difference from the US price of a Big Mac based on the raw data, the GDP per capita of the country, adjusted prices and adjusted percentage difference and other values.\n\nDuring this project i have made different types of analysis of available information and check my hypothesis.",
        reply_markup=mainkeys()
    )
    await message.answer(
        "<b>Definition of values</b>\n\n<u>date</u>: Date of observation\n\n<u>iso_a3</u>: Country code\n\n<u>currency_code</u>: Currency code of the country\n\n<u>name</u>: Country name\n\n<u>local_price</u>: Price of a Big Mac in the local currency\n\n<u>dollar_ex</u>: Local currency units per dollar\n\n<u>dollar_price</u>: Price of a Big Mac in dollars in the specified\n\n<u>usd_raw</u>: Raw index, relative to the US dollar\n\n<u>gdp_dollar</u>: GDP per person, in dollars\n\n<u>adj_price</u>: GDP-adjusted price of a Big Mac, in dollars\n\n<u>number_of_bigmacs</u>: Number of Big Macs that can be bought in the specified country for the price of 1 Big Mac in USA.",
        parse_mode=ParseMode.HTML,
        reply_markup=mainkeys() 
    )

@router.message(F.text.lower() == "graphics")
async def answer_graphs(message: Message):
    await message.answer(
        "What part of graph analysis do you want to explore?",
        reply_markup=graphkeys()
    )
@router.message(F.text.lower() == "dataset")
async def answer_data(message: Message):
    await message.answer(
        "Which one do you want to see?",
        reply_markup=datakeys()
    )
@router.message(F.text.lower() == "hypothesis")
async def answer_analysis(message: Message) -> None:
    await message.answer("During my project i have tested my hypothesis: <b>Does the price of a big mac depend on GDP per capita?</b>\nAnd give the results below.",parse_mode=ParseMode.HTML)
    await message.answer("Correlation coefficient: -0.06544177857750072\np-value: 0.014820023506269807\nReject the null hypothesis - Price of Big Mac depends on GDP per capita.")
    hypo = FSInputFile("hypo.png")

    await message.answer_photo(photo=hypo, caption="Looking at this graphic we can see that that there are no correlation between considered variables")