"""parse config files
"""
import os
import ConfigParser


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
        self.cfg = ConfigParser.ConfigParser()
        self.config = []
        self.load()

    def __can_access(self, path):
        """
        Check is the file exists and readable
        :param path: string to file
        :return: None or config
        """
        return True if os.path.isfile(path) and os.access(path, os.R_OK) else False

    def load(self):
        """
        Load config file
        :return:
        """
        exists = filter(lambda x: self.__can_access(x), self.config_files)

