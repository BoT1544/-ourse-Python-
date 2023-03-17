from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message


bot = Bot('5881992329:AAHHDEGgXEvdDFtqvxmWCu4Bs0ULXHpfrt0')
dp = Dispatcher(bot)

async def on_start(_):
    print('Бот запущен !')

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    name = message.from_user.first_name
    await message.reply(f'Привет {name}, я Кальк_Ботяо ! )\nЕсли напишешь "/help", то раскажу что умею ! )')

@dp.message_handler(commands=['help'])
async def com_start(message: Message):
    name = message.from_user.first_name
    await message.answer(f'{name} ну смотри ниже я приведу примеры:\n'
                         '1) Складываю вот так: "1+1"\n'
                         '2) Вычитаю вот так: "2-1"\n'
                         '3) Умножаю вот так: "2*2"\n'
                         '4) Делю вот так: "2/2"\n'
                         'Пока что это всё, но я учусь ! )')


@dp.message_handler()
async def com_start(message: Message):
    name = message.from_user.first_name
    string = str(message.text)
    for i in string:
        if i == '+':
            if string.split('+')[0].isdigit():
                if string.split('+')[1].isdigit():
                    num_1 = int(string.split('+')[0])
                    num_2 = int(string.split('+')[1])
                    sum = num_1 + num_2
                    print(sum)
                    await message.answer(f'Пуп-Бип, у меня получилось ! ! ! )\nСумма чисел {num_1} и {num_2} равняется {sum}')
                    break
                await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "1+1"') 
                break
            await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букви пробелов примерно так: "1+1"')
            break   
        elif i == '-':
            if string.split('-')[0].isdigit():
                if string.split('-')[1].isdigit():
                    num_1 = int(string.split('-')[0])
                    num_2 = int(string.split('-')[1])
                    sum = num_1 - num_2
                    print(sum)
                    await message.answer(f'Бип-пип, у меня получилось ! ! ! )\nРазность чисел {num_1} и {num_2} равняется {sum}')
                    break
                await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "2-1"') 
                break
            await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "2-1"')
            break
        elif i == '*':
            if string.split('*')[0].isdigit():
                if string.split('*')[1].isdigit():
                    num_1 = int(string.split('*')[0])
                    num_2 = int(string.split('*')[1])
                    sum = num_1 * num_2
                    print(sum)
                    await message.answer(f'Буп-пуп, у меня получилось ! ! ! )\n{num_1} умножить на {num_2} равняется {sum}')
                    break
                await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "2*2"') 
                break
            await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "2*2"')
            break
        elif i == '/':
            if string.split('/')[0].isdigit():
                if string.split('/')[1].isdigit():
                    num_1 = int(string.split('/')[0])
                    num_2 = int(string.split('/')[1])
                    sum = num_1 / num_2
                    sum = round(sum, 3)
                    print(sum)
                    await message.answer(f'Бип-Пуп, у меня получилось ! ! ! )\n{num_1} разделить на {num_2} равняется {sum}')
                    break
                await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "2/2"') 
                break
            await message.reply(f'Буп-Бип, {name} у вас {message.text}, а должно быть без букв и пробелов примерно так: "2/2"')
            break
    if i == string[-1]:
        await message.reply('Бип-Буп, моя не знать что с этим делать.\n'
                            'Поробуй ввести вот так:\n"1+1" или "2-1" или "2*2" или "2/2"')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)


