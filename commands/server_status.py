import evelink


def server_status(bot, update):
    """Get the status of the EVE Online Server"""
    api = evelink.api.API()
    server = evelink.server.Server(api)
    status = server.server_status().result
    server_up = "Server Up" if status['online'] else "Server Down"
    bot.sendMessage(update.message.chat_id, text="EVE Online: %s || Players - %s" % (server_up, status['players']))
