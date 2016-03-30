# telegram-eurobot
Github suggested I call this repo "sturdy-eureka"...

### Running the bot
Create your bot with BotFather according to the [Telegram Documentation](https://core.telegram.org/bots#botfather).

Once you have your token, run the bot with `python eurobot.py your-token-here`- replacing your-token-here with your token from BotFather.

### Contributing
Adding new commands - make a new module in `/commands`, and define your command in said module. Ensure the method for your command has the signature `my_command(bot, update)`, which is what `python-telegram-bot` will pass into command handlers. Also, please ensure your command's main function has a docstring, these are used to generate the help text shown as a response to `/help` or `/start`.
