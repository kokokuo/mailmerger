#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from settings import config


# mailmerge --pdf [資料來源] [信件範本]
# mailmerge --html [資料來源] [信件範本]
# mailmerge --email [資料來源] [信件範本]


@click.command()
@click.option("--action",
              "-c",
              help="Input action after merging source and mail to do.",
              type=click.Choice(config.ACTION_OPTIONS))
def mailmerge(action: str):
    pass


if __name__ == "__main__":
    mailmerge()
