from aiogram.dispatcher.filters.state import StatesGroup,State


class GoogleTarjima(StatesGroup):
    til=State()
    matn=State()