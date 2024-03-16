from pyrogram import Client, filters

# Zdefiniuj token bota, API ID i API HASH
API_ID = 21393840
API_HASH = "e2e6b3a785e6e6e3c35d52d71e8d8b2a"
BOT_TOKEN = "7068265790:AAFV3HdiAbgkbPZuzW6ZWyae1ZtqDj358HA"

# Inicjalizuj klienta Pyrogram
app = Client("Aura_ID_Bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Dekorator obsługi komendy
@app.on_message(filters.command("check"))
def check_user(app, message):
    # Pobierz nazwę użytkownika z wiadomości
    username = message.text.split()[1]

    # Pobierz id użytkownika
    user = app.get_users(username)

    # Wyślij wiadomość z id użytkownika
    message.reply_text(f"ID użytkownika: {user.id}")

# Uruchom klienta
app.run()
