"""from Opus import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [
    "🦋🦋🦋🦋🦋",
    "🧚🌸🧋🍬🫖",
    "🥀🌷🌹🌺💐",
    "🌸🌿💮🌱🌵",
    "❤️💚💙💜🖤",
    "💓💕💞💗💖",
    "🌸💐🌺🌹🦋",
    "🍔🦪🍛🍲🥗",
    "🍎🍓🍒🍑🌶",
    "🧋🥤🧋🥛🍷",
    "🍬🍭🧁🎂🍡",
    "🍨🧉🍺☕️🍻",
    "🥪🥧🍦🍥🍚",
    "🫖☕️🍹🍷🥛",
    "☕️🧃🍩🍦🍙",
    "🍁🌾💮🍂🌿",
    "🌨🌥⛈🌩🌧",
    "🌷🏵🌸🌺💐",
    "💮🌼🌻🍀🍁",
    "🧟🦸🦹🧙👸",
    "🧅🍠🥕🌽🥦",
    "🐷🐹🐭🐨🐻‍❄️",
    "🦋🐇🐀🐈🐈‍⬛",
    "🌼🌳🌲🌴🌵",
    "🥩🍋🍐🍈🍇",
    "🍴🍽🔪🍶🥃",
    "🕌🏰🏩⛩🏩",
    "🎉🎊🎈🎂🎀",
    "🪴🌵🌴🌳🌲",
    "🎄🎋🎍🎑🎎",
    "🦅🦜🕊🦤🦢",
    "🦤🦩🦚🦃🦆",
    "🐬🦭🦈🐋🐳",
    "🐔🐟🐠🐡🦐",
    "🦩🦀🦑🐙🦪",
    "🐦🦂🕷🕸🐚",
    "🥪🍰🥧🍨🍨",
    " 🥬🍉🧁🧇",
]

@Client.on_message(filters.command(["tagall"], prefixes=["/"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ꜰᴏʀ ɢʀᴏᴜᴘꜱ.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ, ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀꜱ."
        )

    if message.reply_to_message and message.text:
        return await message.reply(
            "/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 👈 ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪꜱ / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ꜰᴏʀ ᴛᴀɢɢɪɴɢ..."
        )
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply(
                "/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 👈 ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪꜱ / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ꜰᴏʀ ᴛᴀɢɢɪɴɢ..."
            )
    else:
        return await message.reply(
            "/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 👈 ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪꜱ / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ꜰᴏʀ ᴛᴀɢɢɪɴɢ..."
        )
    if chat_id in spam_chats:
        return await message.reply(
            "ᴘʟᴇᴀꜱᴇ ᴀᴛ ꜰɪʀꜱᴛ ꜱᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ ʙʏ /tagalloff"
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(EMOJI)}\n\n|| ᴏꜰꜰ ᴛᴀɢɢɪɴɢ ʙʏ » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(
    filters.command(
        [
            "stoptagall",
            "canceltagall",
            "offtagall",
            "tagallstop",
            "tagalloff",
        ]
    )
)
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(
            message.chat.id, message.from_user.id
        )
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ, ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀꜱ."
        )
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦️ ꜱᴛᴏᴘᴘᴇᴅ..♦️")
"""
