import click

class DBHost:
	def __init__(self, **kwargs):
		self.host = kwargs.get("host")
		self.user = kwargs.get("user")
		self.password = kwargs.get("password")
		self.dbname = kwargs.get("dbname")

		self.db = MySQLdb.connect(self.host, self.user, self.password, self.dbname)

	def run(self, command):
		cursor = self.db.cursor()
		cursor.execute(command)
		data = cursor.fetchone()
		return data
		#return (data or [None])[0]

	def close(self):
		self.db.close()
	

class GaleraCheck:
	def __init__(self, **kwargs):
		self.host = kwargs.get("host", None)
		self.user = kwargs.get("user", None)
		self.password = kwargs.get("password", None)
		self.dbname = kwargs.get("dbname", "mysql")

		init_db_host()
		init_wsrep_vars()
	
	def init_db_host(self):
		self.db = DBHost(host=self.host, user=self.user, password=self.password, dbname=self.dbname)

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

	def get_wsrep_vars(self):




class Parameter(object):
    def __init__(self, **kwargs):
        self.user = kwargs.get("user")
        self.password = kwargs.get("password")


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0.0 Copyright TheCodeEngine\nUnder MIT License http://opensource.org/licenses/MIT')
    ctx.exit()

@click.group()
@click.option('--verbose', '-v', is_flag=True, default=True, help='Don`t show output.')
@click.option('--user', '-i' ,prompt='MySQL User:', default='debian-sys-maint', help='The MySQL User.')
@click.option('--password', '-p', prompt='MySQL password', hide_input=True, help='The Password for the MySQL User.')
@click.option('--hosts', '-h', multiple=True, help="A MySQL host, can multiple")
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='Show Version and Licens Information.')
@click.pass_context
def main(ctx, verbose, user, password, hosts):
    ctx.obj = Parameter(user=user, password=password)


@main.command()
@click.pass_obj
def check(ctx):
	click.echo('\n+--- Checking Cluster Intigrity:')


@main.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
@click.pass_obj
def do_y(ctx, hash_type):
    print("This method has these arguments: " + str(ctx.username) + ", " + str(ctx.password))


if __name__ == '__main__':
	main()
