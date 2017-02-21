# -*- coding: utf-8 -*-

import state

WORDCOUNT = 0

def filter_word_count(msg):
    """
    Counts all words received on input.
    @rtype: state.next
    """
    global WORDCOUNT

    for word in msg.split():
        WORDCOUNT +=1

    return state.next()

def command_word_count(msg):
    """
    Returns the number of words written on the chat. 
    @rtype: state.done
    """

    global WORDCOUNT

    return state.done("Actual word count is %s words" % WORDCOUNT)

