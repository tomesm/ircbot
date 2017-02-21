# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:49:32 2012

@author: tomesh
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import interface
import plugins
from plugins import state
from plugins import ping




#-------------- BOT ---------------#



class IrcBot(object):
    """
    Implementation of the bot as such. Commands are implemented separately.
    """
    COMMANDS = plugins.COMMANDS
    FILTERS = plugins.FILTERS

    def __init__(self, interface):
        """
        @param interface: implementation of the I/O interface
        @type interface: object5
        """
        self._if = interface

    def parse(self, msg):
        """
        Parse a message, return relevant output.

        @param msg: unparsed message
        @type msg: str
        @return: message to print or None (if there's no output to print)
        @rtype: str|None
        """

        # split msg into command & arguments
        try:
           command, args = msg.split(None, 1)
        except ValueError: # split failed
            command, args = msg.rstrip(), ""

        # try execute command
        if command in self.COMMANDS:
            rval = self.COMMANDS[command](args)

            if state.is_done(rval):
                return rval.value

        # run text HOOKS
        for f in self.FILTERS:
            rval = f(msg)
            if state.is_done(rval):
                return rval.value

            if state.is_replace(rval):
                msg = rval.value

        return msg

    def run(self):
        """
        Endless loop which 'runs' the bot.
        """
        while True:
            msg = self._if.read()
            msg = self.parse(msg)
            if msg:
                self._if.write(msg)


# Main loop
if __name__ == "__main__":
    ifc = interface.IRCBotShellInterface()
    ifc.open()

    try:

        ping = ping.Ping(ifc)
        ping.start()
        bot = IrcBot(ifc)
        bot.run()


    except (KeyboardInterrupt, EOFError, SystemExit):
        print "Shutting down the Bot!"
        ifc.close()
        sys.exit(0)
