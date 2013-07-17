__author__ = 'vukasin'

import tornado.ioloop as io
import tornadoshell

ioloop = io.IOLoop.instance()

shell = tornadoshell.Shell(context={'ioloop': ioloop})
shell.start()

ioloop.start()
