# 🎵 Telegram Music RPC

Realtime RPC для Telegram, который автоматически показывает музыку, которую ты сейчас слушаешь.

Поддерживается:

* Spotify
* Яндекс Музыка
* VK Музыка
* YouTube Music

Пример bio:

```text
🎵 Играет: Drake — Passionfruit
```

---

# ✨ Возможности

* 🚫 Без доп. приложений
* 🎵 Автоопределение музыки
* 🔄 Автоматическое обновление био
* ♻️ Восстановление старого био после закрытия
* ⚡ Обновление треков в реальном времени

---

# 📦 Установка

## 1. Установить Python

Рекомендуется:

* Python 3.11
* Python 3.12

Скачать:

[Python Downloads](https://www.python.org/downloads/?utm_source=chatgpt.com)

При установке обязательно включить:

```text
Add Python to PATH
```

---

# 📁 Клонирование проекта

```bash
git clone https://github.com/attackdevv/TelegramMusicRPC.git
cd TelegramMusicRPC
```

---

# 🧪 Создание venv

```bash
python -m venv .venv
```

---

# ▶️ Активация venv

## Windows CMD

```bash
.venv\Scripts\activate
```

## PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

# 📚 Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# 🔑 Получение Telegram API

1. Открыть:

[my.telegram.org](https://my.telegram.org?utm_source=chatgpt.com)

2. Войти по номеру телефона

3. Перейти в:

```text
API Development Tools
```

4. Создать приложение

5. Получить:

* api_id
* api_hash

---

# ⚙️ Настройка config.json

Открыть:

```text
config.json
```

И вставить свои данные:

```json
{
    "enabled": true,

    "update_interval": 15,

    "telegram": {
        "api_id": 123456,
        "api_hash": "YOUR_API_HASH"
    },

    "rpc": {
        "prefix": "🎵"
    }
}
```

---

# 🔐 Авторизация Telegram

Запустить:

```bash
python auth.py
```

---

# 📱 Ввести:

## Номер телефона

```text
PHONE:
```

## Код из Telegram

```text
CODE:
```

## Пароль 2FA (если включен)

```text
2FA PASSWORD:
```

---

# ✅ После успешного входа

Появится:

```text
SUCCESS
```

И файл:

```text
rpc_session.session
```

---

# 🚀 Запуск

```bash
python main.py
```

---

# 🖥️ Интерфейс

Программа показывает:

* текущий трек
* статус RPC
* кнопку включения/выключения

При выключении RPC:

* био автоматически восстанавливается

При закрытии программы:

* старое био тоже возвращается

---

# 🎧 Поддерживаемые сервисы

Работает с:

* Spotify Desktop
* Spotify Web
* Яндекс Музыка
* VK Музыка
* YouTube Music
* Chrome
* Firefox
* Edge
* Opera

---

# 🛠️ Сборка в EXE

Установить:

```bash
pip install pyinstaller
```

Собрать:

```bash
pyinstaller --onefile --windowed main.py
```

Готовый exe:

```text
dist/main.exe
```
---

# ❤️ Credits

Made by Attack Dev
