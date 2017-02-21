# -*- coding: utf-8 -*-


from calculator import command_calculator
from karma import command_karma, filter_karma
from shutdown import command_shutdown
from word_count import command_word_count, filter_word_count
from ping import call_ping


COMMANDS = {
    "=": command_calculator,
    "karma": command_karma,
    "SHUTDOWN": command_shutdown,
    "word-count": command_word_count,
    "ping": call_ping
}


FILTERS = [
    filter_karma,
    filter_word_count,
]
