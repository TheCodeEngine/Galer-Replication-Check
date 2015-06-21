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
        self.config = [z for z in exists]
        return self.config

    def search(self, section, varname):
        """
        search a variable in the config files and return the value
        :param varname:
        :return:
        """
        return [self.__exists_in_config(z, section, varname) for z in self.config]

    def __exists_in_config(self, file, section, var_name):
        """
        search in config file in section to varname and return this
        :param cfg:
        :param section:
        :param var_name:
        :return:
        """
        try:
            self.cfg.read(file)
        except:
            raise Exception("Can not read file:{0}".format(file))

        sections = filter(lambda x: x == section, self.cfg.sections())
        var_list = [self.__get_config_section_var(self.cfg, section, var_name) for z in sections]
        return reduce(lambda x: x, var_list)

    def __get_config_section_var(self, cfg, section, var):
        try:
            return cfg.get(section, var)
        except:
            return None
