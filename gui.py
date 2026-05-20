import customtkinter as ctk
import json


CONFIG_PATH = "config.json"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(data):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


config = load_config()


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("520x320")
        self.title("Telegram Music RPC")

        ctk.set_appearance_mode("dark")

        self.title_label = ctk.CTkLabel(
            self,
            text="Telegram Music RPC",
            font=("Segoe UI", 28, "bold")
        )

        self.title_label.pack(pady=25)

        self.status_label = ctk.CTkLabel(
            self,
            text="RPC ENABLED"
            if config["enabled"]
            else "RPC DISABLED",
            font=("Segoe UI", 20)
        )

        self.status_label.pack(pady=10)

        self.track_label = ctk.CTkLabel(
            self,
            text="Waiting for music...",
            font=("Segoe UI", 16)
        )

        self.track_label.pack(pady=20)

        self.toggle_button = ctk.CTkButton(
            self,
            text="Disable RPC"
            if config["enabled"]
            else "Enable RPC",
            command=self.toggle_rpc,
            width=220,
            height=45
        )

        self.toggle_button.pack(pady=20)

        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

    def toggle_rpc(self):

        import asyncio

        from telegram_rpc import restore_bio

        config["enabled"] = not config["enabled"]

        save_config(config)

        if config["enabled"]:

            self.status_label.configure(
                text="RPC ENABLED"
            )

            self.toggle_button.configure(
                text="Disable RPC"
            )

        else:

            self.status_label.configure(
                text="RPC DISABLED"
            )

            self.toggle_button.configure(
                text="Enable RPC"
            )

            try:

                loop = asyncio.get_event_loop()

                loop.create_task(
                    restore_bio()
                )

            except Exception as e:

                print("[RESTORE ERROR]")
                print(e)

    def on_close(self):

        self.destroy()


def start_gui():

    app = App()

    return app