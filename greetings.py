#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click

@click.command()
@click.option('--greeting', default='Hello', help='The greeting to use')
@click.option('--name', default='Leander', help='The name to greet')
def greetings(greeting, name):
    print(f"{greeting} {name}!")

if __name__ == '__main__':
    greetings()