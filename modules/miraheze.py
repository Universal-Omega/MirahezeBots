from __future__ import unicode_literals, absolute_import, print_function, division
import sopel
import sopel.module
import requests
import sopel.tools
from sopel.module import rule, priority, thread, commands

"""Miraheze about command

This command will tell you about Miraheze and where to learn more 
"""

@commands('miraheze')
def miraheze(bot, trigger):
	if trigger.sender == '#miraheze':
    bot.say(trigger.nick + ', Miraheze is a non-profit wikifarm running MediaWiki. If you would like more information please see, https://meta.miraheze.org/ or ask in this channel.')
	else:
	bot.say(trigger.nick + ', Miraheze is a non-profit wikifarm running MediaWiki. If you would like more information please see, https://meta.miraheze.org/ or #miraheze.)
