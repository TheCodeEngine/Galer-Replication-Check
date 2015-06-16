from prettytable import PrettyTable

class ClusterTable:

	def __init__(self, cluster):
		self.cluster = cluster

	def render(self):
		self._render(self.cluster.nodes, self.cluster.wsrep_vars)

	def _render(self, nodes, wsrep_vars):

		table = PrettyTable(['Cluster Intigrity Var']+nodes+['Check'])
		table.align['Cluster Intigrity Var'] = "l"

		for status_key,status_value in wsrep_vars.items():
			for key,value in status_value.items():
				attr_list = self._get_list_with_vars(key, nodes)
				table.add_row([key]+attr_list+['OK'])
		print table

	def _get_list_with_vars(self, wsrep_var, nodes):
		attr_list = map(lambda x: x.get_var(wsrep_var), nodes)
		return attr_list

