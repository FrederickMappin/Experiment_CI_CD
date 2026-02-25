import click
import numpy as np
from .operations import add, subtract

@click.group()
def cli():
    """Simple Calculator CLI"""
    pass

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add_cmd(a, b):
    result = np.add(add(a, b), 0)  # Use numpy for demonstration
    click.echo(f"{a} + {b} = {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract_cmd(a, b):
    result = np.subtract(subtract(a, b), 0)  # Use numpy for demonstration
    click.echo(f"{a} - {b} = {result}")

if __name__ == '__main__':
    cli()
