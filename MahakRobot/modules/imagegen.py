import request 
from MahakRobot import dispatcher
from MahakRobot.modules.disable import DisableAbleCommandHandler

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hello! I can help you find images from Pinterest. Use the /image command followed by a keyword to search for images. Example: /image cats"
    )

def pinterest_image_downloader(update: Update, context: CallbackContext) -> None:
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text("Please provide a keyword to search for images. Example: /image cats")
        return

    bot = context.bot
    bot.send_chat_action(chat_id=update.message.chat_id, action="upload_photo")

    api_url = f"https://pinteresimage.nepcoderdevs.workers.dev/?query={query}&limit=9"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if 'results' in data:
            for result in data["results"]:
                bot.send_photo(
                    chat_id=update.message.chat_id,
                    photo=result["imageUrl"],
                    caption=f"📷 <b>{result['title']}</b>",
                    parse_mode=ParseMode.HTML
                )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="❌ <b>No results found.</b>",
                parse_mode=ParseMode.HTML
            )
    except requests.RequestException as e:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=f"❌ <b>Error:</b> <i>{str(e)}</i>",
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=f"❌ <b>Unexpected error:</b> <i>{str(e)}</i>",
            parse_mode=ParseMode.HTML
        )

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("image", pinterest_image_downloader))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()