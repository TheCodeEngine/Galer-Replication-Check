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
	def check(hosts, user=None, password=None, config_files=('/etc/mysql/debian.cfg',)):
		print(user, password)
		c = Config(files=config_files)
		if user is None:
			user = c.search_first('client', 'user')
			user = user if user is not None else 'debian-sys-main'
		if password is None:
			password = c.search_first('client', 'password')
			print password
			password = password if password is not None else ''

		print(user, password)

		click.echo('\n+--- Checking Cluster Intigrity:')
		cluster = Cluster(nodes=hosts, user=user, password=password)
		with click.progressbar(length=cluster.count(), label='Fetching Data') as bar:
			cluster.fetch(bar.update)
		table = ClusterTable(cluster)
		print(table.render())