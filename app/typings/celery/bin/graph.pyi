"""
This type stub file was generated by pyright.
"""

import click
from celery.bin.base import CeleryCommand, handle_preload_options
from celery.utils.graph import GraphFormatter

"""The ``celery graph`` command."""

@click.group()
@click.pass_context
@handle_preload_options
def graph(ctx):  # -> None:
    """The ``celery graph`` command."""
    ...

@graph.command(cls=CeleryCommand, context_settings={"allow_extra_args": True})
@click.pass_context
def bootsteps(ctx):  # -> None:
    """Display bootsteps graph."""
    ...

@graph.command(cls=CeleryCommand, context_settings={"allow_extra_args": True})
@click.pass_context
def workers(ctx):  # -> None:
    """Display workers graph."""

    class Node: ...
    class Thread(Node): ...
    class Formatter(GraphFormatter): ...
    class Worker(Node): ...
    class Backend(Node): ...
    class Broker(Node): ...