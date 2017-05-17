# -*- coding: utf-8 -*-
"""

@author: Martin Tomes
"""

#!/usr/bin/python

#http://www.networksorcery.com/enp/protocol/irc.htm
import re
import socket
import getpass
import time


class IRCBotInterface(object):
    """Generic interface for working with IRC messages."""

    def read(self):
        raise NotImplemented

    def write(self, msg):
        raise NotImplemented

    def open(self):
        raise NotImplemented

    def close(self):
        raise NotImplemented


class IRCBotShellInterface(IRCBotInterface):

    def __init__(self):
        pass

    def read(self):
        return input("> ")

    def write(self, msg):
        print(msg)

    def open(self):
        pass

    def close(self):
        pass

class IRCBotTelnetInterface(IRCBotInterface):
    def __init__(self, address = None, port = 8080):
        self._timeout = 60 * 10
        self._listen = None
        self._sfile = None
        self._socket = None

        self._addr = address
        self._port = port

    def client(self):
        if not self._socket:
            # wait for incoming connection
            conn, addr = self._listen.accept()

            # prepare python File object
            self._sfile = conn.makefile()
            self._socket = conn

        return self._sfile

    def disconnected(self):
        self._socket = None
        self._sfile = None

    def read(self):
        while True:
            try:
                data = self.client().readline()
                if data == "":
                    self.disconnected()
                else:
                    return data.rstrip()
            except (socket.error, socket.timeout, IOError) as ex:
                self.disconnected()

    def write(self, msg):
        self._sfile.write(msg+"\n")
        self._sfile.flush()

    def open(self):
        """Make a socket connection."""
        for (family, socktype, proto, canonname, sockaddr) in socket.getaddrinfo(self._addr, self._port):
            try:
                if socktype != socket.SOCK_STREAM:
                    continue
                if family != socket.AF_INET:
                    continue
                sock = socket.socket(family, socktype, proto)
                sock.settimeout(self._timeout)

                # listen on the selected address
                sock.bind(sockaddr)
                sock.listen(0)
                self._listen = sock

            except (socket.error, socket.timeout, IOError) as ex:
                print(str(ex))

        if self._listen == None:
            raise Exception("No valid address found")

    def close(self):
        if self._socket:
            self._socket.close()

        if self._listen:
            self._listen.close()


if __name__ == "__main__":
    x = IRCBotTelnetInterface("localhost", 8082)
    x.open()

    while True:
        data = x.read()
        if data == "":
            break

        print("Received:", data)
        x.write(data)
