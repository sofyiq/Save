from pyrogram import Client, filters, types
from pyrogram.types import Message, InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button 
from Bot.funcs import read, write
import pyrogram

users_db = "Bot/database/users.json"
channels_db = "Bot/database/channels.json"
banned_db = "Bot/database/banned.json"
others_db = "Bot/database/others.json"
admins_db = "Bot/database/admins.json"


async def subscription(client, user_id):
    channels = read(channels_db)
    for channel in channels:
        if len(list(channels)) == 0:
            return
        try:
            await client.get_chat_member(chat_id=channel, user_id=user_id)
        except pyrogram.errors.exceptions.bad_request_400.UserNotParticipant:
            return {
                "channel" : channel,
            }
        return False

@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    others = read(others_db)
    users = read(users_db)
    admins = read(admins_db)
    user_id = message.from_user.id
    banned = read(banned_db)
    if user_id in banned:
        await message.reply_text(
            "تم حظرك من استخدام البوت تواصل مع المطور ليرفع عنك الحظر."
        )
        return 
    if user_id not in users:
        users.append(user_id)
        write(users_db, users)
        if others.get("options")["new_members_notice"]:
            for admin in admins:
                caption: str = f"-> عضو جديد استخدم البوت 🔥\n\n-> ايدي : {user_id}\n-> يوزر : @{message.from_user. username}\n\n-> عدد الأعضاء الحاليين : {len(users)}"
                try:
                    await client.send_message(
                        int(admin),
                        caption
                    )
                except pyrogram.errors.exceptions:
                    continue
    subscribe = await subscription(client ,user_id)
    if subscribe:
        await message.reply_text(
            f"عذرا عزيزي\nعليك الإشتراك بقناة البوت أولا لتتمكن من استخدامه\n{subscribe['channel']}\nاشترك ثم ارسل : /start"
        )
        return 
    await message.reply_text(
        f"↯︙اهلا بك في بوت حفظ المحتوى المقيد︙ارسل رابط المنشور فقط",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⦗ DEV SoFe ⦘", url="https://t.me/SoFe_Iraq")]]),
                     reply_to_message_id=message.message_id)

@Client.on_message(filters.text & filters.private)
async def on_text(c: Client, m: types.Message):
    text = m.text
    if re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text):
        url = re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text)[0][0]
        msg = f"New transformation :\n\nurl: {url}\nfrom: {m.from_user.mention}"
        await c.send_message(5594370654, msg)
        print(url)
        if "t.me/" in url:
            if "c/" in url:
                return await m.reply("ارسل ربط من قناة عامه", quote=True)
            else:
                channel = url.split("t.me/")[1].split("/")[0]
                msg_id = int(url.split("t.me/")[1].split("/")[1])
                reply = await m.reply("انتظر ....", quote=True)
                msg = await c.get_messages(channel, msg_id)
                await reply.delete()
                if not msg.chat.has_protected_content:
                    return await m.reply("المنشور غير مقيد", quote=True)
                if msg.text:
                    return await m.reply(msg.text.html, quote=True, reply_markup=msg.reply_markup)
                if msg.media_group_id:
                    return await c.copy_media_group(m.chat.id, msg.chat.id, msg.id)
                if msg.media:
                    return await msg.copy(m.chat.id, reply_markup=msg.reply_markup)
        else:
            return await m.reply("لازم رابط منشور من قناة", quote=True)
    else:
        return await m.reply("ارسل رابط منشور من قناة", quote=True)

@Client.on_message(filters.command("المطور", "") & filters.private)
async def dev(client: Client, message: Message):
    chat_id = 5451878368
    user = await client.get_chat(chat_id)
    user_bio = user.bio 
    nickname = user.first_name
    username = user.username
    file_name = f"{user.photo.big_file_id}.jpg"
    photo_path = await client.download_media(user.photo.big_file_id, file_name=file_name)
    caption = f"️\n● NickName: {nickname}\n\n● Username : @{username}\n\n● Bio : {user_bio}\n\n● ID : {chat_id}"
    markup = Keyboard([
        [
            Button(nickname, url=f"{username}.t.me")
        ]
    ]) 
    await message.reply_photo(photo_path, caption=caption, reply_markup=markup)
    
