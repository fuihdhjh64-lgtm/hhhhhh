from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot token from @BotFather
BOT_TOKEN = "8671655903:AAEmRFbP-QpVARJ3HtMTM4djEzxNmlT7WPM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "you dont have access to this p1 please contact @kuruuuuuuuuuuuuuuuuuuu for access"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
