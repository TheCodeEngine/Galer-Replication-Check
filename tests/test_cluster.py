from pkg import Cluster, Node
from mock import patch, Mock, MagicMock

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
	mock = Cluster
	mock._create_node = MagicMock(return_value=Node(host='127.0.0.1', user='root', password='123456', dbname='name'))
	mock = helper_create_cluster()
