from pkg.table import Table

def test_init():
	table = Table()
	assert table is not None

def test_listEqualOK():
	table = Table()

	listOk = ['1', '1', '1']
	rv = table.listEqual(listOk)
	assert rv is True

def test_listEqualError():
	table = Table()

	listError = ['1', '2', '1']
	rv = table.listEqual(listError)
	assert rv is False

