from __future__ import print_function
import pymysql
from functools import reduce

class Node:
	def __init__(self, **kwargs):
		self.host = kwargs.get("host")
		self.user = kwargs.get("user")
		self.password = kwargs.get("password")
		self.dbname = kwargs.get("dbname")
		self.wsrep_vars = {}
		self.db = None

	def run_sql(self, command):
		if self.db is None:
			self.db = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.dbname)
		cursor = self.db.cursor()
		cursor.execute(command)
		data = cursor.fetchone()
		return data

	def __str__(self):
		return self.host

	def run(self, var_name, sql_stament):
		try:
			_, rv = self.run_sql(sql_stament)
			self.wsrep_vars[var_name] = rv
		except:
			self.wsrep_vars[var_name] = None

	def getvar(self, variable):
		return self.wsrep_vars[variable]

	def getName(self):
		return self.host

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
		self.nodes = map(self._create_node, nodes)

	def _create_node(self, node):
		return Node(host=node, user=self.user, password=self.password, dbname=self.dbname)

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
			},
			'var': {
				'var': "SHOW STATUS LIKE 'wsrep_flow_control_paused';"
			}
		}

	def count(self):
		"""
		Return the count of the cluster nodes
		"""
		return len(list(self.nodes))

	def nodes(self):
		return self.nodes

	def wsrep_vars(self):
		return self.wsrep_vars

	def wsrep_vars_values(self):
		return reduce(lambda x,y: list(x)+list(y), [self.wsrep_vars[z].keys() for z in self.wsrep_vars])

	def fetch(self, update_call=None):
		count = 0
		for node in self.nodes:
			for var_status, vars_dict in self.wsrep_vars.items():
				for variable,sql_statement in vars_dict.items():
					node.run(variable, sql_statement)
					count = count + 1
					if update_call is not None:
						update_call(count)

	def check(self, ok_style=True, error_style=False):
		list_keys = [
			'wsrep_cluster_status',
			'wsrep_cluster_size',
			'wsrep_cluster_conf_id',
			'wsrep_cluster_state_uuid'
		]
		list_vars = self.__check_generate_values(list_keys)
		f = lambda l: True if all(x == l[0] for x in l) else False
		list_vars_reduce = [f(z) for z in list_vars]

		error = reduce(lambda x,y: x and y, list_vars_reduce)

		self.__print_check(list_keys, list_vars_reduce, ok_style, error_style)

		return error

	def __check_generate_values(self, list_keys):
		return [[n.getvar(v) for n in self.nodes] for v in list_keys]

	def __print_check(self, list_keys, list_vars, ok_style, error_style):
		l = zip(list_keys, list_vars)

		print('\nCluster-Status:')
		fnpoe = lambda x: ok_style if x == True else error_style
		f = lambda xy: print("{1} \t {0}".format(xy[0],fnpoe(xy[1])))
		[f(z) for z in l]

