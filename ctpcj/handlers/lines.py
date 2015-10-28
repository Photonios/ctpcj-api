"""Simple handler without any parameters that gets all
available public transportation lines in JSON."""

from .base import BaseHandler
from ctpcj import Ctpcj

class LinesHandler(BaseHandler):
    """Handles incoming requests on /lines, returning the
    available public transportation lines."""

    def get(self):
        lines = Ctpcj.all_lines()
        self.write({
            'lines': lines
        })

        self.set_header('Access-Control-Allow-Origin', '*')
