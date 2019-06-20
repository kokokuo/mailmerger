#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from settings import config


# mailmerge --action=[pdf|html|email] [資料來源] [信件範本]

@click.command()
@click.argument("excelpath", required=True, type=click.Path())
@click.argument("mailpath", required=True, type=click.Path())
@click.option("--action",
              "-c",
              "action",
              help="Input action after merging source and mail to do.",
              type=click.Choice(config.ACTION_OPTIONS))
def runcmds(action: str, excelpath: str, mailpath: str):
    click.echo("Your option is " + click.style(f"{action}", fg="red", bold=True))
    click.echo(f"Check your excel source path > {excelpath}")
    click.echo(f"Check your email draft path > {mailpath}")


def makepdf():
    pass


if __name__ == "__main__":
    runcmds()
