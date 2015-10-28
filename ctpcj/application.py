"""Represents the web server application and is used to
abstract initializing, starting and stoppig it."""

import logging
import tornado.ioloop
import tornado.web

from .settings import Settings
from .handlers import LinesHandler

LOGGER = logging.getLogger(__name__)


class Application:
    """Represents this application at a top-level."""

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.webserver = tornado.web.Application([
            (r'/lines', LinesHandler)
        ])

        self.is_running = False

    def run(self):
        """Runs this application as a web server listening
        on a specific port.

        This method blocks forever."""

        self.webserver.listen(
            Settings.singleton()['server']['port']
        )

        LOGGER.info("Starting web server on port %s",
                    Settings.singleton()['server']['port'])

        self.is_running = True
        tornado.ioloop.IOLoop.current().start()

    def stop(self):
        """Stops the web server and returns the exit code
        to return to the underlying operating system.

        Returs (int):
            The exit code to return to the underlying
            operating system.
        """

        if self.is_running:
            tornado.ioloop.IOLoop.instance().stop()

        return 0
