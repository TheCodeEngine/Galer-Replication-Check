import click
from prettytable import PrettyTable


class Table(object):
	def __init__(self):
		super(Table, self).__init__()

	def listEqual(self, list):
		return True if all(x == list[0] for x in list) else False

	def tableArray(self, x, y, fx, fy):
		return [fy(y)+[fx(z,y) for z in x] for y in y]

	def renderTable(self, x, y,fx=None, fy=None, fi=None):
		fx = (lambda x,y: x) if fx is None else fx
		fy = (lambda y: [y]) if fy is None else fy
		lt = self.tableArray(x, y, fx, fy)
		lf, lr = lt[0], lt[1:]

		table = PrettyTable(lf)

		fi = (lambda l: table.add_row(l)) if fi is None else fi
		map(fi, lr)

		return table


class ClusterTable(Table):
	def __init__(self, cluster):
		super(ClusterTable, self).__init__()
		self.cluster = cluster

	def render(self, x=None, y=None):
		x = self.cluster.nodes if x is None else x
		y = self.cluster.wsrep_vars_values() if y is None else y ## @todo move to Cluster and test
		table = self.__rendertable(x, y)
		return table

	def __rendertable(self, nodes, wsrep_vars):
		fx = (lambda x,y: x.getvar(y) if (y is not 'var') else x.getName())
		fy=(lambda x: [x])
		table = self.renderTable(nodes, wsrep_vars, fx=fx, fy=fy)
		table.align["var"] = "l"



		#table = PrettyTable(['Cluster Intigrity Var'] + nodes + ['Check'])
		#table.align['Cluster Intigrity Var'] = "l"
#
		#for status_key, status_value in wsrep_vars.items():
		#	for key, value in status_value.items():
		#		attr_list = self.__get_list_with_vars(key, nodes)
		#		status = self.__statusStringListEqual(attr_list) if status_key == 'cluster-integrity' else ''
		#		table.add_row([key] + attr_list + [status])
		#	table.add_row([''] * (self.cluster.count() + 2))

		return table

	def __statusStringListEqual(self, attr_list):						# @todo deprecated
		ok_style = click.style('OK', fg='green')
		error_style = click.style('Error', bold=True, fg='red')

		return ok_style if self.listEqual(attr_list) else error_style

	def __get_list_with_vars(self, wsrep_var, nodes):					# todo @deprecated
		attr_list = map(lambda x: x.getvar(wsrep_var), nodes)
		return attr_list
