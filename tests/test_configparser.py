from pkg.config import Config

def test_init():
    c = Config(files=('/etc/mysql/debian.cnf', '/etc/mysql/my.cnf'))
