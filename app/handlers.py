from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatMemberUpdated
from phrases import PHRASES
import random

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hey, {message.from_user.first_name}\nI'm here to motivate you\nJust type /motivation and that's all")


@router.message(Command('help'))
async def get_help(message: Message):
    await message.reply("All you can do just type /motivation. I'll send one of my motivational phrases.")


@router.message(Command('motivation'))
async def get_help(message: Message):
    await message.reply(random.choice(PHRASES))


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer("Cool photo bro!")

active_chats = set()

@router.my_chat_member()
async def my_chat_member_handler(my_chat_member: ChatMemberUpdated):
    if (
            my_chat_member.new_chat_member.status in {"member", "administrator"} and
            my_chat_member.old_chat_member.status not in {"member", "administrator"}
    ):
        chat_id = my_chat_member.chat.id
        print(my_chat_member.chat.id)
        active_chats.add(chat_id)

        await my_chat_member.bot.send_message(
            chat_id=chat_id,
            text="Hey there! I'm here just to make your day a bit better and motivate you!"
        )

    elif (
            my_chat_member.new_chat_member.status not in {"member", "administrator"} and
            my_chat_member.old_chat_member.status in {"member", "administrator"}
    ):
        chat_id = my_chat_member.chat.id
        active_chats.discard(chat_id)
