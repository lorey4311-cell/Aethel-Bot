import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from telegram.ext import Application, CommandHandler, MessageHandler, filters

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

Thread(target=run_server, daemon=True).start()

async def start(update, context):
    await update.message.reply_text("¡Hola Leonel! Aethel-Bot está en línea.")

async def echo(update, context):
    await update.message.reply_text(f"Dijiste: {update.message.text}")

def main():
    token = "8887747443:AAFP-007PUsvnmDRexQF_tl4yCNmB2arR60"
    
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot started...")
    app.run_polling()

if __name__ == '__main__':
    main()
