#!/usr/bin/env python

import hexchat

__module_name__ = "warn-away"
__module_version__ = "1.0"
__module_description__ = (
    "Hexchat plugin that displays a msg saying the user is away"
)


def warn_user_if_away(word, word_eol, userdata):
    away_reason = hexchat.get_info("away")
    if away_reason is not None:
        print("\002 >>> You are away (reason: %s)" % away_reason)


hexchat.hook_print("Focus Tab", warn_user_if_away)

print("Module %s loaded (version: %s)" % (__module_name__, __module_version__))
