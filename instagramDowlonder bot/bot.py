"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from dowlonder import instagramDowlonder
API_TOKEN = '5725756053:AAF72o1F_r3h9Vk6XbXns50dKzzjepbVmT4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!\nXush Kelibsiz!\nBu Botimiz\nInstagramdagi Video va Rasimlar yuqlab beradi.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    link=message.text
    data=instagramDowlonder(link=link)
    if data=='Bad':
        await message.answer("Bunday Malumot yoq")
    else:
        if data['Type']=='image':
            await message.answer_photo(photo=data['media'],)
            await message.reply('Bu botning Mualifi @ilxomjumayev')
        elif data['Type']=='video':
            await message.answer_video(video=data['media'])
            await message.reply('Bu botning Mualifi @ilxomjumayev')
        elif data['Type']=='carousel':
            for i in data['media']:
                await message.answer_document(document=i)
                await message.reply('Bu botning Mualifi @ilxomjumayev')
        else:
            await message.answer("Bunday Malumot yoq")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)