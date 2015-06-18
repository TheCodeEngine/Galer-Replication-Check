from pkg.table import ClusterTable

def test_init():
	table = ClusterTable(None)
	assert table is not None


def test_render():
	table = ClusterTable(None)

	class Node(object):
		def __init__(self, var):
			self.var = var

		def getvar(self):
			return self.var

	x = [Node('n1'), Node('n2'), Node('n3')]
	y = ['var1', 'var2', 'var3']

	t = table.render(x, y)