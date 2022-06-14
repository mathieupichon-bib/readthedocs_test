import click

from .thecode import *


@click.command()
@click.option("--arg", multiple=True, default=["param"])
def main(arg):
    the_class = AClass(*arg)
    click.echo(str(the_class))


if __name__ == "__main__":
    main()
