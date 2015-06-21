from pkg import file

def test_can_access():
    assert file.can_access('/etc/test/') is False
    assert file.can_access('/etc/hosts') is True
