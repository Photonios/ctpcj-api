"""Allows configuration to be stored and retrieved from a
configuration file. The configuration file class is a
a singleton that can be accessed from anywhere in the
application. It will read from an existing configuration
file if it exists, or write a new one with the default
values if it doesn't.

The singleton pattern was chosen to avoid cluttering or
increasing the complexity of the code of having to pass
on settings class instances everywhere. While maintaining
the ability to create a new instance to write or read
the configuration file from/to different locations.
"""

import os
import logging
import configparser

from .constants import Constants

LOGGER = logging.getLogger(__name__)


class Settings():
    """Represents the configuration file.

    Args:
        path (str): the file path to read from
    """

    instance = None

    def __init__(self, path):
        self.path = path

        self.config = configparser.ConfigParser()
        self.__init_default_config()

    @classmethod
    def singleton(cls):
        """Provides access to the global instance of the Settings class.

        Returns (configparser.ConfigParser):
            The configuration contained in the global instance of the Settings
            class.
        """

        path = Constants.config_file_path()

        if not cls.instance:
            cls.instance = Settings(path)

            if os.path.exists(path):
                cls.instance.read()
            else:
                cls.instance.write()

        return cls.instance.config

    def read(self):
        """Reads the configuration from the configured file path."""

        self.config.read(self.path)
        LOGGER.info("Settings read from %s", self.path)

    def write(self):
        """Writes the current configuration to the configured file."""

        with open(self.path, 'w') as sfile:
            self.config.write(sfile)

        LOGGER.info("Settings written to %s", self.path)

    def __init_default_config(self):
        """Initializes the config parser with the default configuration."""

        self.config['server'] = {
            'port': 2015
        }
