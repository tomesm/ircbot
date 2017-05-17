# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:00:10 2012

@author: tomesh
"""
import threading
import queuelib
import time

class Ping(threading.Thread):
    qfactory = lambda priority: queuelib.FifoDiskQueue('queue-dir-%s' % priority)
    q = queuelib.PriorityQueue(qfactory)
    def __init__(self, interface):
        threading.Thread.__init__(self)
        self._running = True
        self._if = interface
    #q = Queue.PriorityQueue()

    def run(self):
        # the routine to be run in the thread
        # should end when self._running is False
        while self._running:
            self.q.pop()
            time.sleep(5)
            self._if.write("pong")

    def stop(self):
        # pass a signal by setting the running variable to False
        self._running = False

    @classmethod
    def run_ping(cls):  #clas = class
        cls.q.put(1)
        #print mes


def call_ping(mess):
    Ping.run_ping()
