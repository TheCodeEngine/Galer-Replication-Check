from pkg.table import ClusterTable

def test_init():
	table = ClusterTable(None)
	assert table is not None


def test_render():
	table = ClusterTable(None)

	class Node(object):
		def __init__(self, var):
			self.var = var

		def getvar(self, var):
			return "{0}({1})".format(self.var, var)

		def getName(self):
			return self.var

	x = [Node('n1'), Node('n2'), Node('n3')]
	y = {
			'cluster-integrity': {
				'wsrep_cluster_state_uuid': "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_state_uuid';",
				'wsrep_cluster_conf_id': "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_conf_id';",
				'wsrep_cluster_size': "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';",
				'wsrep_cluster_status': "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';"
			},
			'node-status': {
				'wsrep_ready': "SHOW GLOBAL STATUS LIKE 'wsrep_ready';",
				'wsrep_connected': "SHOW GLOBAL STATUS LIKE 'wsrep_connected';",
				'wsrep_local_state_comment': "SHOW GLOBAL STATUS LIKE 'wsrep_local_state_comment';"
			},
			'replication-health': {
				'wsrep_flow_control_paused': "SHOW STATUS LIKE 'wsrep_flow_control_paused';",
				'wsrep_cert_deps_distance': "SHOW STATUS LIKE 'wsrep_cert_deps_distance';"
			},
			'var': {
				'var': ""
			}}

	t = str(table.render(x, y))
	assert isinstance(t, str) is True
	print(t)