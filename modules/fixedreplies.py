from sopel import module

keywords = {
    'tdee': 'https://loseitirc.github.io/tdeecalc/',
    'ss': 'http://liamrosen.com/fitness.html',
    'docs' : 'https://github.com/loseitIRC/loseitdocs',
    'source' : 'https://github.com/loseitIRC/loseitbot'
}

@module.commands(*keywords.keys())
def linkreply(bot, trigger):
      bot.reply(keywords[trigger.group(1)])
