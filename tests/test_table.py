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

def test_renderTableArray():
	table = Table()
	array = table.renderTableArray(['node 1', 'node 2', 'node 3', 'node 4'], ['var 1', 'var 2', 'var 3'])

	assert table is not None
	assert len(array) is 3
	assert len(array[0]) is 5
	assert array[0][0] is 'var 1'
	assert array[0][1] is 'node 1'
