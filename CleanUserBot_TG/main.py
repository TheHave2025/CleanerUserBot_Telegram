import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logging.basicConfig(level=logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.CRITICAL)

api_id = "Tu API ID de Telegram aqui"
api_hash = "#Tu API Hash de Telegram aqui"
OWNER_ID = "#Tu ID de Telegram aquí"

app = Client("cleaner_userbot", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command("clean", prefixes=".") & filters.group)
async def limpiar(client: Client, message: Message):

    if message.from_user.id != OWNER_ID:
        return

    msg = await message.reply("𝗜𝗻𝗶𝗰𝗶𝗮𝗻𝗱𝗼 𝗹𝗶𝗺𝗽𝗶𝗲𝘇𝗮... 🧹")

    chat_id = message.chat.id
    mensajes = []
    total = 0

    async for m in client.get_chat_history(chat_id):

        if m.id == msg.id:
            continue

        mensajes.append(m.id)

        if len(mensajes) >= 100:
            await client.delete_messages(chat_id, mensajes)
            total += len(mensajes)
            mensajes = []

            await msg.edit(f"𝗟𝗶𝗺𝗽𝗶𝗮𝗻𝗱𝗼... 🧹\n━━━━━━━━━━━━━\n{total} Mensajes eliminados")

    if mensajes:
        await client.delete_messages(chat_id, mensajes)
        total += len(mensajes)

    await msg.edit(f"𝗚𝗿𝘂𝗽𝗼 𝗹𝗶𝗺𝗽𝗶𝗼 ✅\n━━━━━━━━━━━━━\n🗑 {total} Mensajes eliminados")


app.run()