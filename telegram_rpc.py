import json

from telethon import TelegramClient

from telethon.tl.functions.account import (
    UpdateProfileRequest
)

from telethon.tl.functions.users import (
    GetFullUserRequest
)


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]

PREFIX = config["rpc"]["prefix"]

client = TelegramClient(
    "rpc_session",
    api_id,
    api_hash
)

started = False
original_bio = ""


async def ensure_client():

    global started
    global original_bio

    if not started:

        await client.connect()

        me = await client.get_me()

        full = await client(
            GetFullUserRequest(me.id)
        )

        original_bio = (
            full.full_user.about
            or ""
        )

        print(f"[TG] CONNECTED: {me.username}")
        print(f"[TG] ORIGINAL BIO: {original_bio}")

        started = True


async def update_rpc_async(track):

    await ensure_client()

    text = f"{PREFIX} Играет: {track}"

    if len(text) > 70:
        text = text[:67] + "..."

    try:

        await client(
            UpdateProfileRequest(
                about=text
            )
        )

        print(f"[TG] UPDATED BIO: {text}")

    except Exception as e:

        print("[TG ERROR]")
        print(e)


async def restore_bio():

    global original_bio

    await ensure_client()

    try:

        await client(
            UpdateProfileRequest(
                about=original_bio
            )
        )

        print("[TG] BIO RESTORED")

    except Exception as e:

        print("[TG RESTORE ERROR]")
        print(e)