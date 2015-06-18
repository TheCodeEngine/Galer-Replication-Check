import click
from pkg.database import Cluster
from pkg.table import ClusterTable


class AppInfo:
	@staticmethod
	def version_info():
		return 'Version 1.2.1 Copyright TheCodeEngine\nUnder MIT License http://opensource.org/licenses/MIT'


class GaleraCLI:
	@staticmethod
	def check(user, password, hosts):
		click.echo('\n+--- Checking Cluster Intigrity:')
		cluster = Cluster(nodes=hosts, user=user, password=password)
		with click.progressbar(length=cluster.count(), label='Fetching Data') as bar:
			cluster.fetch(bar.update)
		table = ClusterTable(cluster)
		table.render()