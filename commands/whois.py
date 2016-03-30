from datetime import datetime
import evelink


def calculate_time(delta):
    output = []
    days = delta.days % 31
    months = delta.days / 31
    years = None
    if months > 12:
        years = months / 12
        months %= 12

    if years:
        output.append("%d years" % years)

    if months:
        output.append("%d months" % months)

    output.append("%d days" % days)
    return ", ".join(output)


def whois(bot, update):
    """Get information about an EVE Online character"""
    who = " ".join(update.message.text.split()[1:])
    eve = evelink.eve.EVE()

    charid = eve.character_id_from_name(who).result
    if not charid:
        bot.sendMessage(update.message.chat_id, text="The character %s could not be found." % who)

    info = eve.character_info_from_id(charid).result
    time_in_corp = datetime.utcnow() - datetime.utcfromtimestamp(info['corp']['timestamp'])

    message = """*%s* (%s)
Corp: %s (%s)""" % (who, round(info['sec_status'], 2),
                    info['corp']['name'], calculate_time(time_in_corp))

    if info['alliance']['name']:
        time_in_alliance = datetime.utcnow() - datetime.utcfromtimestamp(info['alliance']['timestamp'])
        message += """
Alliance: %s (%s)""" % (info['alliance']['name'], calculate_time(time_in_alliance))

    bot.sendMessage(update.message.chat_id, text=message, parse_mode="Markdown")
