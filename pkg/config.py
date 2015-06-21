"""parse config files
"""
import ConfigParser
from pkg import file
from itertools import ifilter


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
        self.cfg = None
        self.config = []
        self.load()

    def load(self):
        """
        Load config file
        :return: list of files thats loaded
        """
        exists = filter(lambda x: file.can_access(x), self.config_files)
        self.config = [z for z in exists]
        return self.config

    def search(self, section, varname):
        """
        search a variable in the config files and return the value
        :param section: string of a section
        :param varname: string of a variable
        :return: list of variables that founds
        """
        self.cfg = ConfigParser.ConfigParser()
        return [self.__exists_in_config(z, section, varname) for z in self.config]

    def search_first(self, section, varname):
        """
        search a variable in the config files and return the value
        :param section: string of a section
        :param varname: string of a variable
        :return: return the first element when something found or None
        """
        list = self.search(section, varname)
        return list[0] if len(list) > 0 else None

    def __exists_in_config(self, file, section, var_name):
        """
        search in config file in section to varname and return this
        :param file: string file path
        :param section: string of INI Section name
        :param var_name: string of Varname in a Section
        :return: list of variables that found in config
        """
        try:
            self.cfg.read(file)
        except:
            raise Exception("Can not read file:{0}".format(file))

        sections = filter(lambda x: x == section, self.cfg.sections())
        var_list = [self.__get_config_section_var(self.cfg, section, var_name) for z in sections]
        var_list = reduce(lambda x: x, var_list)

        return var_list

    def __get_config_section_var(self, cfg, section, var):
        """
        look to the section if there is the variable and return if exists
        :param cfg: ConfigParser
        :param section: string of section
        :param var: string of variable
        :return: variable value or None
        """
        try:
            return cfg.get(section, var)
        except:
            return None
