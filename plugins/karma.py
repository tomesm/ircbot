# -*- coding: utf-8 -*-

from . import state

KARMA = {}

def command_karma(name):
    """
    Returns the actual karma of 'name'
    @param name: key to search karma for
    @type name: str
    @returns: message with actual karma
    """
    global KARMA
    # ignore empty parameter
    if name == "":
        return state.next()
    if name not in KARMA:
        return state.done("%s has no karma" % name)
    return state.done("%s's karma is %s" % (name, KARMA[name]))

def filter_karma(msg):
    """
    Handles the message name++/name-- and increases/decreases numeric
    karma value accordingly.
    @param msg: received message
    @type msg: str
    @rtype: state.done|state.next
    """
    global KARMA
    msg = msg.lower()
    for word in msg.split():
        # ignore the '[cC]++' string
        if word == "c++":
            continue
        # check whether the word ends with ++/--
        if not (word.endswith("++") or word.endswith("--")):
            continue
        key = word[:-2]
        # if the string in `word` is shorter than 2 characters, then
        # `key` contains empty string
        if key == "":
            continue
        KARMA.setdefault(key, 0)
        KARMA[key] += 1 if word.endswith('++') else -1
        # ^^^ is "the right way" of selecting values, but needs Python >= 2.5
        # in older Pythons, the 'and/or' trick can be used for the same result
        #
        # KARMA[key] += word.endswith('++') and 1 or -1
        #
        # http://www.siafoo.net/article/52#selecting-values
        #
        # Also note, that those two lines could be one-lined to
        #
        # KARMA[key] = KARMA.get(key, 0) + (1 if word.endswith('++') else -1)

        # if the 'final' karma is 0, delete the key from the dictionary
        if KARMA[key] == 0:
            del KARMA[key]
    return state.next()

