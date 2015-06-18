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

def test_tableArray():
	table = Table()
	x = ['node 1', 'node 2', 'node 3', 'node 4']
	y = ['var 1', 'var 2', 'var 3']

	array = table.tableArray(x, y, (lambda x: x), (lambda x: x))
	assert table is not None
	assert len(array) is 3
	assert len(array[0]) is 5
	assert array[0][0] is 'var 1'
	assert array[0][1] is 'node 1'

def test_tableArrayWithObject():
	table = Table()
	class MyObject(object):
		def __init__(self, para):
			self.para = para

		def getPara(self):
			return self.para

	x = [MyObject('node 1'), MyObject('node 2'), MyObject('node 3'), MyObject('node 4')]
	y = ['var 1', 'var 2', 'var 3']

	# Test if rendered Table
	array = table.tableArray(x, y, (lambda x: x), (lambda x: x))
	assert table is not None
	assert len(array) is 3
	assert len(array[0]) is 5

	# Test with function
	fx = lambda x: x.getPara()
	array = table.tableArray(x, y, (lambda x: x), (lambda x: x))
	assert table is not None
	assert len(array) is 3
	assert len(array[0]) is 5

def test_renderTable():
	table = Table()

	x = ['node 1', 'node 2', 'node 3', 'node 4', 'node 5']
	y = ['variables', 'var 1', 'var 2', 'var 3']

	t = table.renderTable(x, y)
	t = str(t)

	assert t is not None
	assert isinstance(t, str) is True

