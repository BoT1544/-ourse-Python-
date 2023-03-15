from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message


bot = Bot('5881992329:AAHHDEGgXEvdDFtqvxmWCu4Bs0ULXHpfrt0')
dp = Dispatcher(bot)

async def on_start(_):
    print('Бот запущен !')

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    await message.reply('Здравствуйте, я умею складывать и вычитать ! )')

@dp.message_handler()
async def com_start(message: Message):
    # await message.reply(f'{message.from_user.first_name},' f'{message.text}')
    # if message.text.lower() == 'молодец':
    #     await message.reply(f' Спасибо, {message.from_user.first_name}, ты тоже')
    # elif message.text.lower() == 'дурак':
    #     await message.answer('Ой на себя посмотри')


    string = str(message.text)
    for i in string:
        if i == '+':
            num_1 = int(string.split('+')[0])
            num_2 = int(string.split('+')[1])
            sum = num_1 + num_2
            print(sum)
            await message.answer(f'Сумма чисел {num_1} и {num_2} равняется {sum}')
            break   
        elif i == '-':
            num_1 = int(string.split('-')[0])
            num_2 = int(string.split('-')[1])
            sum = num_1 - num_2
            print(sum)
            await message.answer(f'Разность чисел {num_1} и {num_2} равняется {sum}')
            break   
    await message.answer('fail ! (')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)
