def add_command(bot, fn):
    bot.add_command(fn)


def add_commands(bot, fns):
    for fn in fns:
        try:
            add_command(bot, fn)
        except Exception as e:
            pass
