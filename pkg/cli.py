import click
from pkg.database import Cluster
from pkg.table import ClusterTable
from pkg.config import Config


class AppInfo:
	@staticmethod
	def version_info():
		return 'Version 1.2.1 Copyright TheCodeEngine\nUnder MIT License http://opensource.org/licenses/MIT'


class GaleraCLI:
	@staticmethod
	def check(hosts, user=None, password=None, config_files=None):
		if user is None:
			c = Config(files=config_files)
			user = c.search_first('client', 'user')
			user = user if user is not None else click.prompt('MySQL User')
		if password is None:
			c2 = Config(files=config_files)
			password = c2.search_first('client', 'password')
			password = password if password is not None else click.prompt('MySQL password', hide_input=True)

		click.echo('\n+--- Checking Cluster Intigrity:')
		cluster = Cluster(nodes=hosts, user=user, password=password)
		with click.progressbar(length=cluster.count(), label='Fetching Data') as bar:
			cluster.fetch(bar.update)
		table = ClusterTable(cluster)
		print(table.render())

		cluster.check(ok=click.style('OK', fg='green'), error=click.style('Error', bold=True, fg='red'))