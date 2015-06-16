import click


class Parameter(object):
    def __init__(self, **kwargs):
        self.user = wargs.get("user")
        self.password = wargs.get("password")

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0.0 Copyright TheCodeEngine\nUnder MIT License http://opensource.org/licenses/MIT')
    ctx.exit()

@click.group()
@click.option('--human', '-h' ,default=True, help='Show Human readable output.')
@click.option('--user', '-i' ,prompt='MySQL User:', default='debian-sys-maint', help='The MySQL User.')
@click.option('--password', '-p', prompt='MySQL password', hide_input=True, help='The Password for the MySQL User.')
@click.option('--hosts', '-h', multiple=True, help="A MySQL host, can multiple")
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.pass_context
def main(ctx, human, user, password, hosts):
    ctx.obj = Parameter(user, password)
    print("This method has these arguments: " + str(user) + ", " + str(password))


@main.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
@click.pass_obj
def check_split(ctx, hash_type):
    print("This method has these arguments: " + str(ctx.username) + ", " + str(ctx.password))


@main.command()
@click.pass_obj
def do_y(ctx):
    print("This method has these arguments: " + str(ctx.username) + ", " + str(ctx.password))


if __name__ == '__main__':
	main()