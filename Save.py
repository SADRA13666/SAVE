from telethon.sync import TelegramClient, events
import os
api_id = input("Please Enter API ID : ")
api_hash = input("Please Enter API Hash : ")
bot = TelegramClient('SecretBot', api_id, api_hash).start()

@bot.on(events.NewMessage(pattern=r'(بصبر)', func=lambda e: e.is_reply))
async def show_image(event):
    userid = await bot.get_me()
    if event.sender_id == userid.id:
        try:
            message = await event.get_reply_message()
            download = await bot.download_media(message)
            await bot.send_message('me', f'➣Downloaded🤟\n➣Powered by Alireza🌹', file=download)
            os.remove(download)
        except Exception as e:
            await bot.send_message('me', f"خطایی دریافت شد:\n\n{e}")
print("Powered by Alireza")
print("Ok, Bot is running.....")
bot.run_until_disconnected()
