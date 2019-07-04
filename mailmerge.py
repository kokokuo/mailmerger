#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from settings import config
from apps.dto.source import PreMergeSourceDTO
from apps.services.datasource import parsing_service
from apps.services.draftmerge import merge_service

# mailmerge --action=[pdf|html|email] [資料來源] [信件範本]


def makepdf(excelpath: str, mailpath: str):
    source: PreMergeSourceDTO = parsing_service.parsing_excel(excelpath)
    mail_content = merge_service.read_draft(mailpath)
    merge_service.merge2pdf(mail_content, source)


def makehtml(excelpath: str, mailpath: str):
    raise NotImplementedError()


def sendemail(excelpath: str, mailpath: str):
    raise NotImplementedError()


cmds = {
    config.ACTION_OPTION_EMAIL: sendemail,
    config.ACTION_OPTION_PDF: makepdf,
    config.ACTION_OPTION_HTML: makehtml,
}


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
    cmds[action](excelpath, mailpath)


if __name__ == "__main__":
    runcmds()
