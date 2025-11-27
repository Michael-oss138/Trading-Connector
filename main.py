from telethon import TelegramClient, events
from config import apiid, apihash, CHANNELS
from trader import sendtotradingbot
from parser import parsesignal

client = TelegramClient("session", apiid, apihash)

async def process_message(message: str):
    print("New Message:", message)

    signal = parsesignal(message)

    if signal:
        print("Signal Detected", signal)
        sendtotradingbot(signal)
    else:
        print("Not a trading signal")

@client.on(events.NewMessage(chats=CHANNELS))
async def channellistener(event):
    message = event.message.message
    await process_message(message)

def main():
    print("bot starting....3,2,1  Listening to Channels", CHANNELS)
    client.start()
    client.run_until_disconnected()

if __name__ == "main":
    main()