from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 25116728
api_hash = "8fef459b63e30e0d4c7febd57d036648"
phone = "+994707909293"

# The channels/groups that you want to get messages from
source_channel_names = ['FRI® VIP', 'Binance Killers® VIP Signals', 'Bitcoin Bullets® Premium Free']

# The channel/group where you want to forward messages
destination_channel_link = -1002138412651

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code:'))

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title in source_channel_names:
            await client.forward_messages(entity=destination_channel_link, messages=event.message)
    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit

client.start()
client.run_until_disconnected()
