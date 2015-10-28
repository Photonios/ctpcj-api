"""Base Tornado web handler that all handlers inherit from. There's
nothing special about this yet, but this will make it easier in
the future to implement functionality that all handlers can benefit from."""

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """Handler that all handlers must inherit from."""

    # Only here because marked abstract and PyLint
    # is complaining about it not being overriden..
    def data_received(self, chunk):
        """Implement this method to handle streamed request data.

        Requires the `.stream_request_body` decorator.
        """

        pass
