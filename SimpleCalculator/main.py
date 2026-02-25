
"""
Calculator CLI Application

USAGE:
    python main.py [COMMAND] [ARGS]

COMMANDS:
    add a b         Add two numbers
    subtract a b    Subtract two numbers
    multiply a b    Multiply two numbers
    divide a b      Divide two numbers
    negate value    Print the negative of a value

EXAMPLES:
    python main.py add 2 2
    python main.py divide 10 2
    python main.py negate 5
    python main.py --help
    python main.py add --help
"""

import click
from calculator.add import add as add_func
from calculator.sub import sub as sub_func
from calculator.multiplication import multiply as multiply_func
from calculator.division import divide as divide_func
from calculator.negate import negate as negate_func

@click.group()
def cli():
    """Simple Calculator CLI"""
    pass

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add(a, b):
    """Add two numbers."""
    result = add_func(a, b)
    negated = negate_func(result)
    click.echo(f"{a} + {b} = {result}")
    click.echo(f"Negated result: {negated}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract(a, b):
    """Subtract two numbers."""
    result = sub_func(a, b)
    negated = negate_func(result)
    click.echo(f"{a} - {b} = {result}")
    click.echo(f"Negated result: {negated}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def multiply(a, b):
    """Multiply two numbers."""
    result = multiply_func(a, b)
    negated = negate_func(result)
    click.echo(f"{a} * {b} = {result}")
    click.echo(f"Negated result: {negated}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def divide(a, b):
    """Divide two numbers."""
    try:
        result = divide_func(a, b)
        negated = negate_func(result)
        click.echo(f"{a} / {b} = {result}")
        click.echo(f"Negated result: {negated}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument('value', type=float)
def negate(value):
    """Print the negative of the input value."""
    result = negate_func(value)
    click.echo(f"Negate({value}) = {result}")

if __name__ == '__main__':
    cli()
