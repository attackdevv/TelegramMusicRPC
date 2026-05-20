import threading
from flask import Flask, request
from telegram_rpc import update_rpc_async
from gui import start_gui

app = Flask(__name__)

rpc_enabled = True
last_track = ""

@app.route("/update", methods=["POST"])
async def update():
    global rpc_enabled
    global last_track

    if not rpc_enabled:
        return {"status": "disabled"}

    data = request.json

    title = data.get("title", "Unknown")
    artist = data.get("artist", "Unknown")
    playing = data.get("playing", False)

    if not playing:
        return {"status": "paused"}

    track = f"{artist} — {title}"

    if track == last_track:
        return {"status": "same"}

    last_track = track

    print(f"[RPC] {track}")

    await update_rpc_async(track)

    return {"status": "updated"}

def run_server():
    app.run(
        host="127.0.0.1",
        port=8765,
        debug=False
    )

def on_close(self):
    self.destroy()
    
if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    start_gui()