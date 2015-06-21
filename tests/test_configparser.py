from pkg.config import Config

def test_init():
    c = Config(files=('/etc/mysql/debian.cnf', '/etc/mysql/my.cnf'))
    assert c is not None

def test_load():
    c = Config(files=('/etc/mysql/debian.cnf', '/etc/mysql/my.cnf'))
    cfgs = c.load()
    assert cfgs is not None