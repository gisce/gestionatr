## -*- encoding: utf-8 -*-

import sys
import click
from suds.client import Client as SudsClient


def request_p0(url, user, password, xml_file):
    client = SudsClient(url=url, cache=None)
    if isinstance(xml_file, str):
        xml_str = xml_file
    else:
        f = open(xml_file, "r")
        xml_str = f.read()
    return client.service.sync(xml_str)


@click.group()
def cli():
    pass


@cli.command()
@click.option('-u', '--url', default='http://localhost', help=u'URL del webservice', show_default=True)
@click.option('-s', '--user', help=u'User del webservice', show_default=True)
@click.option('-p', '--password', help=u'Password del webservice', show_default=True)
@click.option('-f', '--file', help=u'Fitxer P0 pas 01 per enviar', show_default=True)
def sollicitar_p0(url, user, password, file):
    res = request_p0(url, user, password, file)
    print res


if __name__ == '__main__':
    cli()
