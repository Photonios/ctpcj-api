"""Collection of of constants or constants that depend on
underlying operating system, available to the entire application."""

import os


class Constants:
    """Collection of application lifetime constants."""

    @classmethod
    def root_path(cls):
        """Gets the path to the root directory of this application.

        Returns (str):
            The path to the root directory of this application.
        """

        # join with .. because constants.py is in a sub directory
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '..'
        )

        return path

    @classmethod
    def config_file_path(cls):
        """Gets the absolute path to the configuration file.

        Returns (str):
            The absolute path to the configuration file path.
        """

        path = os.path.abspath(os.path.join(
            cls.root_path(),
            'settings.ini'
        ))

        return path
