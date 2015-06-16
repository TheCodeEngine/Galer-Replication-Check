import MySQLdb


class Node:
	def __init__(self, **kwargs):
		self.host = kwargs.get("host")
		self.user = kwargs.get("user")
		self.password = kwargs.get("password")
		self.dbname = kwargs.get("dbname")

	def run(self, command):
		if self.db is None:
			self.db = MySQLdb.connect(self.host, self.user, self.password, self.dbname)
		cursor = self.db.cursor()
		cursor.execute(command)
		data = cursor.fetchone()
		return data
		#return (data or [None])[0]

	def close(self):
		if self.db is None:
			pass
		else:
			self.db.close()


class Cluster:
	def __init__(self, nodes=('127.0.0.1',), **kwargs):
		self.user = kwargs.get("user", None)
		self.password = kwargs.get("password", None)
		self.dbname = kwargs.get("dbname", "mysql")

		self.init_nodes(nodes)
		self.init_wsrep_vars()
	
	def init_nodes(self, nodes):
		self.nodes = map(lambda x: Node(host=x, user=self.user, password=self.password, dbname=self.dbname), nodes)

	def init_wsrep_vars(self):
		self.wsrep_vars = {
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
			}
		}

	def count(self):
		"""
		Return the count of the cluster nodes
		"""
		return len(self.nodes)

	def get_wsrep_vars(self):
		pass
