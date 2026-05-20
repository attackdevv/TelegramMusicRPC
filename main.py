import asyncio
import json

from media import get_media

from telegram_rpc import (
    update_rpc_async,
    restore_bio
)

from gui import start_gui


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

last_track = ""


async def rpc_loop(gui):

    global last_track

    while True:

        try:

            with open("config.json", "r", encoding="utf-8") as f:
                config = json.load(f)

            enabled = config["enabled"]

            if enabled:

                media = await get_media()

                if media:

                    title = media["title"]
                    artist = media["artist"]
                    playing = media["playing"]

                    track = f"{artist} — {title}"

                    gui.track_label.configure(
                        text=track
                    )

                    print(f"[MEDIA] {track}")

                    if playing and track != last_track:

                        print("[RPC] NEW TRACK")

                        await update_rpc_async(track)

                        last_track = track

                else:

                    gui.track_label.configure(
                        text="No media playing"
                    )

                    print("[MEDIA] NO MEDIA")

            else:

                gui.track_label.configure(
                    text="RPC disabled"
                )

                print("[RPC] DISABLED")

                last_track = ""

        except Exception as e:

            print("[MAIN ERROR]")
            print(e)

        await asyncio.sleep(
            config["update_interval"]
        )


async def main():

    gui = start_gui()

    asyncio.create_task(
        rpc_loop(gui)
    )

    try:

        while gui.winfo_exists():

            gui.update()

            await asyncio.sleep(0.01)

    finally:

        print("[APP] RESTORING BIO...")

        await restore_bio()


asyncio.run(main())