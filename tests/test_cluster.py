from pkg import Cluster
from mock import patch

def test_init():
	cluster = Cluster()
	assert cluster is not None

def test_init_with_nodes():
	cluster = Cluster(('127.0.0.1', '127.0.0.2', '127.0.0.3'), user='root', password='123456')
	assert cluster is not None
	assert cluster.count() is 3