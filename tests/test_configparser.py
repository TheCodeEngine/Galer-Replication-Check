from pkg.config import ConfigParser

def test_init():
    c = ConfigParser(files=('/etc/mysql/debian.cnf', '/etc/mysql/my.cnf'))
