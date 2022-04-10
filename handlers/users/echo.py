import aiogram
from aiogram import types
from aiogram import Bot, Dispatcher, executor
from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from googletrans import Translator
from keyboards.inline.languages import button
from aiogram.types import CallbackQuery
from states.languages import GoogleTarjima

tarjimon=Translator()


@dp.message_handler(Text('Tilni sozlash'))
async def test(message:types.Message):
    await message.answer('Tarjima turini tanlang', reply_markup=button)
    await GoogleTarjima.til.set()

@dp.callback_query_handler(state=GoogleTarjima.til)
async def test1(call:CallbackQuery,state:FSMContext):
    lang=call.data
    if lang=='uzen':
        src='uz'
        dest='en'
    elif lang=='enuz':
        src='en'
        dest='uz'
    elif lang=='uzru':
        src='uz'
        dest='ru'
    elif lang=='ruuz':
        src='ru'
        dest='uz'
    elif lang=='uztr':
        src='uz'
        dest='tr'
    elif lang=='truz':
        src='tr'
        dest='uz'
    elif lang=='uzar':
        src='uz'
        dest='ar'
    elif lang=='aruz':
        src='ar'
        dest='uz'
    await state.update_data(
        {
            'src':src,'dest':dest
        }
    )

    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer('<b>Matin kiriting</>', parse_mode='html')
    await GoogleTarjima.next()
@dp.message_handler(state=GoogleTarjima.matn)
async def test2(message:types.Message, state:FSMContext):
    text=message.text

    await state.update_data(
        {'text':text}
    )


    # Maulmotlarni qayta o'qish

    data=await state.get_data()
    src=data.get("src")
    dest=data.get('dest')
    text=data.get('text')

    if message.text=="Tilni sozlash":
        await state.finish()
        await message.answer('Tarjima turini tanlang', reply_markup=button)
        await GoogleTarjima.til.set()
    else:
        xabar=tarjimon.translate(text, dest=dest, src=src)
    await message.answer(xabar.text)
