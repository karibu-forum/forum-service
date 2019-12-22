import click

from forum_service.commands.db import db
from forum_service.commands import seed
from forum_service.commands.server import run_server
from forum_service import app


@click.group()
def cli():
    pass


cli.add_command(db)
if app.config.APP_ENV != 'production':
    cli.add_command(run_server)
