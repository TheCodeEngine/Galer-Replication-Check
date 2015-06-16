import click
from pkg import Cluster

class Parameter(object):
    def __init__(self, **kwargs):
        self.user = kwargs.get("user")
        self.password = kwargs.get("password")
        self.hosts = kwargs.get("hosts")


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0.0 Copyright TheCodeEngine\nUnder MIT License http://opensource.org/licenses/MIT')
    ctx.exit()

@click.group()
@click.option('--verbose', '-v', is_flag=True, default=True, help='Don`t show output.')
@click.option('--user', '-i' ,prompt='MySQL User:', default='debian-sys-maint', help='The MySQL User.')
@click.option('--password', '-p', prompt='MySQL password', hide_input=True, help='The Password for the MySQL User.')
@click.option('--hosts', '-h', multiple=True, help="A MySQL host, can multiple", default=('127.0.0.1',))
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='Show Version and Licens Information.')
@click.pass_context
def main(ctx, verbose, user, password, hosts):
    ctx.obj = Parameter(user=user, password=password, hosts=hosts)


@main.command()
@click.option('--hosts', '-h', multiple=True, help="A MySQL host, can multiple", default=('127.0.0.1',))
@click.pass_obj
def check(ctx, hosts):
    click.echo('\n+--- Checking Cluster Intigrity:')
    cluster = Cluster(nodes=hosts, user=ctx.user, password=ctx.password)
    with click.progressbar(length=cluster.count(), label='Unzipping archive') as bar:
        cluster.fetch(bar.update)


@main.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
@click.pass_obj
def do_y(ctx, hash_type):
    print("This method has these arguments: " + str(ctx.username) + ", " + str(ctx.password))


if __name__ == '__main__':
	main()
