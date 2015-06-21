"""parse config files
"""
import ConfigParser
from pkg import file


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

    def load(self):
        """
        Load config file
        :return:
        """
        exists = filter(lambda x: file.can_access(x), self.config_files)
        self.config = [self.cfg.read(z) for z in exists]


