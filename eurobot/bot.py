#!/usr/bin/env python
from eurobot.commands import commands
from telegram.ext import Updater
import logging
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    welcome_text = """Hi, I am EuroSquad's bot - Eurobot!

I know the following commands:\n"""
    for command, method in commands.items():
        welcome_text += "/%s    %s\n" % (command, method.__doc__)

    welcome_text += "\nI am maintained by @hreeder. My source code is [available here](https://github.com/hreeder/telegram-eurobot)"
    bot.sendMessage(update.message.chat_id, text=welcome_text, parse_mode="Markdown")


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(sys.argv[1])

    dp = updater.dispatcher

    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", start)

    for command, method in commands.items():
        dp.addTelegramCommandHandler(command, method)

    dp.addErrorHandler(error)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
