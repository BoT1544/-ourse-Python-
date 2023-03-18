from Create_bot import dp
from aiogram.types import Message
import random
import config 

@dp.message_handler(commands=['start', 'начать'])
async def mes_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, привет !\n'
                        f'Сегодня мы с тобой поиграем в интересную игру\n'
                        'Для начала выбери сложность бота:\n'
                        'Что бы выбрать нажми на кнопки'
                        'Нормальная сложность "/normal"\n'
                        'Высокая сложность "/hard"')


@dp.message_handler(commands=['new'])
async def mes_new_game(message: Message,):
    if ' ' in message.text:
        if message.text.split(' ')[1].isdigit():
            candy = int(message.text.split(' ')[1])
            name = message.from_user.first_name
            for game in config.games:
                if message.from_user.id == game:
                    await message.answer(f'{name} ты уже есть в игре, иди играй')
                    break
            else:
                config.total = candy
                await message.answer(text=f'И так, на столе {config.total} конфет. Кидаем жребий кто берёт первым')
                config.games[message.from_user.id] = candy
                coin = random.randint(0, 1)
                if coin:
                    await message.answer(text=f'{message.from_user.first_name}, поздравляю выпал орёл. Ты ходишь первым'
                                            f'бери от 1 до 28 конфет')
                else:
                    await message.answer(text=f'{message.from_user.first_name}, не растраивайся первый ход делает бот')
                    await bot_turn(message)
        else:
            await message.reply(f'Вы ввели {message.text}, а нужно правильно команду "/new"\n'
                                'После ввести количество конфет через пробел\n'
                                'Пример ввода: "/new 100"')            
    else:
        await message.reply(f'Вы ввели {message.text}, нужно были разделить команду и цифры пробелом\n'
                                'Пример ввода: "/new 100"')
            

@dp.message_handler(commands=['normal'])
async def normal(message: Message,):
    config.dif = 0
    await message.answer(f'Вы выбрали нормальную сложность\n')
    await message.answer(f'Давай теперь  установим количество конфет\n'
                        'Для этого введи команду и через пробел укажи количество конфет\n'
                        'Пример ввода "/new 100"\n')

@dp.message_handler(commands=['hard'])
async def hard(message: Message,):
    config.dif = 1
    await message.answer(f'Вы выбрали высокую сложность\n')
    await message.answer(f'Давай теперь  установим количество конфет\n'
                        'Для этого введи команду и через пробел укажи количество конфет\n'
                        'Пример ввода "/new 100"\n')



@dp.message_handler()
async def all_catch(message: Message):
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            await player_turn(message)
        else:
            await message.answer(text=f'Ах ты, хитрый {message.from_user.first_name} !'
                                 f'Конфет надо взять хотябы 1, но не больше 28. Попробуй ещё раз ')
    else:
        if '/new' in message.text:
            await message.reply(f'У вас введено {message.text}, а нужно вводить вот так: "/new 100"\n'
                                'цифру можно любую больше 100, а то будет не интересно ! )')
        else:
            await message.answer(text='введи цифрами количество конфет от 1 до 28')

async def player_turn(message: Message):
    take_amount = int(message.text)
    config.games[message.from_user.id] = config.games.get(message.from_user.id) - take_amount
    name = message.from_user.first_name
    await message.answer(text=f'{name} взял {take_amount} конфет и на столе осталось'
                            f'{config.games.get(message.from_user.id)}\n')
    if await check_victory(message, name):
        return
    await message.answer(text=f'Торжественно передаём ход боту !') 
    await bot_turn(message)


async def bot_turn(message: Message):
        current_total = config.games.get(message.from_user.id)
        if config.dif == 1:
            take_amount = 0
            if current_total <= 28:
                take_amount = current_total
            else:
                take_amount = current_total % 29 if current_total % 29 != 0 else 1
        else:
            if current_total <= 28:
                take_amount = current_total
            else:
                take_amount = random.randint(1, 28)
        config.games[message.from_user.id] = config.games.get(message.from_user.id) - take_amount
        name = message.from_user.first_name
        await message.answer(text=f'бот взял {take_amount} конфет и на столе осталось'
                             f'{config.games.get(message.from_user.id)}\n')
        if await check_victory(message, 'бот'):
            return
        await message.answer(text=f'{name} теперь твоё черёд ! Бери конфеты') 


async def check_victory(message: Message, name: str):
    if config.games.get(message.from_user.id) <= 0:
        await message.answer(text=f'Победил {name} ! "Это была славная игра ! )')
        await message.answer('Можно начинать новую игру\n'
                            'Для этого введи команду и через пробел укажи количество конфет\n'
                            'Пример ввода "/new 100"\n'
                            'Так же можно изменить сложность бота, если не менять она останеть прежней\n'
                            'Что бы выбрать нажми на кнопки'
                            'Нормальная сложность "/normal"\n'
                            'Высокая сложность "/hard"')
        config.games.pop(message.from_user.id)
        return True
    else:
        return False

