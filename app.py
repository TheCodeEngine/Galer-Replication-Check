from __future__ import print_function
import click
import MySQLdb
from prettytable import PrettyTable
import time

class MySQLConnection:
	def __init__(self, host, user, password, dbname):
		self.host = host
		self.user = user
		self.password = password
		self.dbname = dbname

		self.db = MySQLdb.connect(self.host, self.user, self.password, self.dbname)

	def run(self, command):
		cursor = self.db.cursor()
		cursor.execute(command)
		data = cursor.fetchone()
		return data
		#return (data or [None])[0]

	def close(self):
		self.db.close()


class MariaDBHost:
	def __init__(self, host, user, password, dbname):
		self.host = host
		self.user = user
		self.password = password
		self.dbname = dbname

		self.wsrep_cluster_state_uuid = ''
		self.wsrep_cluster_conf_id = ''
		self.wsrep_cluster_size = ''
		self.wsrep_cluster_status = ''

	def __str__(self):
		return self.host

	def check_cluster_intigrity(self):
		my = MySQLConnection(self.host, self.user, self.password, self.dbname)
		_, self.wsrep_cluster_state_uuid = my.run("SHOW GLOBAL STATUS LIKE 'wsrep_cluster_state_uuid';")
		_, self.wsrep_cluster_conf_id = my.run("SHOW GLOBAL STATUS LIKE 'wsrep_cluster_conf_id';")
		_, self.wsrep_cluster_size = my.run("SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';")
		_, self.wsrep_cluster_status = my.run("SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';")
		my.close()

def checking_cluster_integrity(databases, print_human_resulsts):
	if print_human_resulsts is False:
		for database in databases:
			database.check_cluster_intigrity()
	else: 
		click.echo('\n+--- Checking Cluster Intigrity:')
		with click.progressbar(databases,label='Fetching Data', length=len(databases)) as bar:
			for database in bar:
				database.check_cluster_intigrity()
		if print_human_resulsts is True:
			table = PrettyTable(['Cluster Intigrity Var']+list(databases)+['Check'])
			table.align['Cluster Intigrity Var'] = "l"

			uuid_list = map(lambda x: x.wsrep_cluster_state_uuid, databases)
			uuid_list_check = click.style('OK', fg='green') if all(x == uuid_list[0] for x in uuid_list) else click.style('Error', bold=True, fg='red')
			table.add_row(["wsrep_cluster_state_uuid"]+uuid_list+[uuid_list_check])

			conf_id_list = map(lambda x: x.wsrep_cluster_conf_id, databases)
			conf_id_list_check = click.style('OK', fg='green') if all(x == conf_id_list[0] for x in conf_id_list) else click.style('Error', bold=True, fg='red')
			table.add_row(["wsrep_cluster_conf_id"]+conf_id_list+[conf_id_list_check])

			cluster_size = map(lambda x: x.wsrep_cluster_size, databases)
			cluster_size_check = click.style('OK', fg='green') if all(x == cluster_size[0] for x in cluster_size) else click.style('Error', bold=True, fg='red')
			table.add_row(["wsrep_cluster_size"]+cluster_size+[cluster_size_check])

			cluster_status = map(lambda x: x.wsrep_cluster_status, databases)
			cluster_status_check = click.style('OK', fg='green') if all(x == cluster_status[0] for x in cluster_status) else click.style('Error', bold=True, fg='red')
			table.add_row(["wsrep_cluster_status"]+cluster_status+[cluster_status_check])

			click.echo(table)


@click.command()
@click.option('--human', '-h' ,default=True, help='Show Human readable output.')
@click.option('--user', '-i' ,prompt='MySQL User:', default='debian-sys-maint', help='The MySQL User.')
@click.option('--password', '-p', prompt='MySQL password', hide_input=True, help='The Password for the MySQL User.')
@click.option('--hosts', '-h', multiple=True, help="A MySQL host, can multiple")
def test_cluster(human, user, password, hosts):
	"""Testing the Galera Cluster"""
	if len(hosts) is 0:
		hosts = ('127.0.0.1',)
	databases = []
	for value in hosts:
		databases.append(MariaDBHost(value, user, password, 'mysql'))

	checking_cluster_integrity(databases, human)


if __name__ == '__main__':
	test_cluster()
    


