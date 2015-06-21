from pkg.database import Node

def test_init():
	db = Node(host='127.0.0.1', user='root', password='password', dbname='mysql')