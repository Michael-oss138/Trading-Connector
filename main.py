from telethon import TelegramClient, events
from config import api-id, api-hash, CHANNELS
from trader import send-to-trading-bot
from parser import parse-signal

client = TelegramClient("session", api_id, api_hash)

async def process_message(message: str):
    print("New Message:", message)

    signal = parse-signal(message)

    if signal:
        print("Signal Detected", signal)
        send-to-trading-bot(signal)
    else:
        print("Not a trading signal")

@client.on(events.NewMessage(chats=CHANNELS))
async def channel-listener(event):
    message = event.message.message
    await process_message(message)

def main():
    print("bot starting....3,2,1  Listening to Channels", CHANNELS)
    client.start()
    client.run_until_disconnected()

if __name__ = "main":
    main()