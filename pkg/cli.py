from prettytable import PrettyTable
import click

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
				status = self._get_list_status(attr_list) if status_key == 'cluster-integrity' else ''
				table.add_row([key]+attr_list+[status])
			table.add_row(self._create_list_with_empty(self.cluster.count()+2))
		print table

	def _get_list_with_vars(self, wsrep_var, nodes):
		attr_list = map(lambda x: x.get_var(wsrep_var), nodes)
		return attr_list

	def _get_list_status(self, attr_list): # @todo TESTING
		status = click.style('OK', fg='green') if all(x == attr_list[0] for x in attr_list) else click.style('Error', bold=True, fg='red')
		return status

	def _create_list_with_empty(self, count):
		l = []
		for i in range(count):
			l.append('')
		return l

