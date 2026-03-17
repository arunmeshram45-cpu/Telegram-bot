from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7999488506:AAFaOru59OL6j_QKBg5cvwItkitOqineHH4"

keywords = [
"pass",
"open pass",
"panel pass",
"jodii pass",
"blastttt",
"blast",
"open blast",
"jodi blast",
"running",
"congratulation",
"congratulations"
]

async def detect(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message and update.message.text:
        text = update.message.text.lower()

        for word in keywords:
            if word in text:

                await update.message.reply_text("""𝗕𝗜𝗚 𝗕𝗜𝗚 𝗕𝗜𝗚

𝗖𝗢𝗡𝗚𝗥𝗔𝗧𝗨𝗟𝗔𝗧𝗜𝗢𝗡𝗦 💐💐""")

                break


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), detect))

print("Bot Running...")

app.run_polling()
