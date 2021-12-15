from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyromod import listen

api_id = 7309528
api_hash = "889011dbc11c7f87a50af540b2745354"
api_key = "5087985942:AAGwR4uuLrGjGcnBtCrzJuOFI0Cds-_C8O8"

with Client("my_account", api_id, api_hash, api_key) as app:
    pass



#START
@app.on_message(filters.command("start"))
async def start(client, message):
    await app.send_message(message.chat.id, f"""
👋 **Benvenuto** {message.from_user.mention} nel bot ufficiale di @Mangapertutti 🎌

❔__Cosa posso fare qui?__
Tramite il comando /manga puoi consigliare un manga che vorresti che pubblicassimo. 
⚠ **ATTENZIONE**! Solamente i migliori verranno pubblicati, eventuali scherzi verranno puniti con un ban!

**SEGUICI SUI NOSTRI SOCIAL** ⬇️
""", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                            "📫 Canale News",
                            url="https://t.me/mangapertutti")
            ],

            [
                InlineKeyboardButton(
                    "🌐 Sito Web",
                    url="https://www.mangapertutti.ga")

            ]

        ]
    ))

#FUNZIONE SUGGERIMENTO MANGA TRAMITE COMANDO
@app.on_message(filters.command("manga"))
async def start(client,message):
    answer = await client.ask(message.chat.id, f'''
    
📖 **NUOVO SUGGERIMENTO MANGA**

Hey {message.from_user.mention}, invia il nome del manga che vuoi suggerire!! 

__I migliori verranno selezionati e poi pubblicati.__
    
    ''')
    await client.send_message("konoiiii", f'Hai un nuovo suggerimento da parte di {message.from_user.mention} » {answer.text}')
    await client.send_message(message.chat.id, "**Suggerimento inoltrato allo staff, grazie! **😊")


@app.on_message(filters.command("test"))
async def test(client, message):
    await message.reply(f"la tua mention è {message.from_user.mention}")





app.run()
