from pyrogram import Client, filters



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
