from pkg import Cluster
from mock import patch, Mock

def test_init():
	cluster = Cluster()
	assert cluster is not None

def helper_create_cluster():
	cluster = Cluster(('127.0.0.1', '127.0.0.2', '127.0.0.3'), user='root', password='123456')
	return cluster

def test_init_with_node():
	cluster = Cluster()
	assert cluster is not None
	assert cluster.count() is 1

def test_init_with_nodes():
	cluster = helper_create_cluster()
	assert cluster is not None
	assert cluster.count() is 3

def test_get_vars_from_nodes():
	cluster = helper_create_cluster()

	mockFoo = Mock(name = "run")
	mockFoo.mym.return_value = 'l'
	assert mockFoo.mym() == 'l'


