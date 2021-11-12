#!/usr/bin/env python3
# Starter program with click cli examples

from functools import reduce

import click


# Shared args
@click.group()
@click.option("--debug", "-d", is_flag=True, help="Use debug mode")
@click.option("--verbose", "-v", is_flag=True, help="Use verbose mode")
@click.pass_context
def cli(ctx, debug, verbose):
    """Pass general probram settings such as 'debug'

    Example, to call 'sum' with 'debug' use:
        'python ./src/main.py --debug sum'
    """
    ctx.ensure_object(dict)

    ctx.obj["DEBUG"] = debug
    ctx.obj["VERBOSE"] = verbose

    if verbose:
        click.echo(f"Verbose is on")
        click.echo(f"Debug is {'on' if ctx.obj['DEBUG'] else 'off'}")
    elif debug:
        click.echo(f"Debug is 'on'")
    else:
        pass


@cli.command()
@click.argument("items", nargs=-1, type=int)
@click.pass_context
def sum(ctx, items):
    """Sum any number of objects passed in via 'items'.

    Params:
        number items: numbers to sum
            Note: use "--" before negatives
                example: "sum -- 2 3 -1"
        bool debug: debug mode via ctx
        bool verbose: verbose mode via ctx"""
    debug = ctx.obj["DEBUG"]
    verbose = ctx.obj["VERBOSE"]

    if verbose:
        click.echo(f"items={items}")

    sum = reduce(lambda x, y: x + y, items)
    click.echo(f"sum={sum}")
    return sum


if __name__ == "__main__":
    cli(obj={})
