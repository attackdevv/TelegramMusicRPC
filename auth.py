from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import json


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]


client = TelegramClient(
    "rpc_session",
    api_id,
    api_hash
)

print("[1] CONNECTING...")

client.connect()

print("[2] CONNECTED")


if not client.is_user_authorized():

    print("[3] NOT AUTHORIZED")

    phone = input("PHONE: ")

    client.send_code_request(phone)

    code = input("CODE: ")

    try:

        client.sign_in(phone, code)

    except SessionPasswordNeededError:

        password = input("2FA PASSWORD: ")

        client.sign_in(password=password)

else:

    print("[3] ALREADY AUTHORIZED")


me = client.get_me()

print(f"[4] LOGGED AS: {me.username}")

print("SUCCESS")

input("PRESS ENTER TO EXIT")