from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8540907111:AAHSC62-lhTEfCcDssBn4TM8WX4TSSFzZOM"
CHANNEL = "@kinobotda"

async def start(update: AAFj-OwgSP6qfQJp7sGLcg3qL9HhuWGrsR8, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Kino botga xush kelibsiz!\n\n"
        "Kino kodini yuboring.\n"
        f"Avval kanalga obuna bo‘ling 👉 {CHANNEL}"
    )

async def kino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text
    await update.message.reply_text(
        f"🎥 Siz so‘ragan kino kodi: {code}\n\n"
        "Bu test bot. Keyin to‘liq qilamiz."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, kino))
app.run_polling()
