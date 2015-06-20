import os
from configparser import ConfigParser
"""parse config files
"""


class Config(object):
    """
    Parse config files liki ini for values and return this values
    """
    def __init__(self, files=None):
        """
        Konstruktor
        :type files: tuple
        """
        if not isinstance(files, tuple):
            raise ValueError('The Parameter files must be a tuple')

        self.config_files = list(files)
        self.cfg = ConfigParser()
        self.config = []
        self.load()

    def load(self):
        """
        Load config file
        :return:
        """
        f = lambda x: x

        return f
