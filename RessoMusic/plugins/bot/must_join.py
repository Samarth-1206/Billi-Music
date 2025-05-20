from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from RessoMusic import app

#--------------------------
MUST_JOIN = "I_kaisen"
#--------------------------

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/3tfhrd.jpg",
                    caption=(
                        f"<b>๏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ <a href=\"{link}\">๏ sᴜᴘᴘᴏʀᴛ ๏</a> "
                        f"ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ғᴇᴀᴛᴜʀᴇs.</b>\n\n"
                        f"<b>ᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴛʜᴇ <a href=\"{link}\">๏ ᴄʜᴀɴɴᴇʟ ๏</a> "
                        f"ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴛʏᴘᴇ /start ᴀɢᴀɪɴ !!</b>"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("• ᴊᴏɪɴ •", url=link),
                            ]
                        ]
                    ),
                    parse_mode="html"
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
