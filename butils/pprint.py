# coding=utf-8
from __future__ import print_function
from __future__ import absolute_import

'''
Module for colorfull pretty printing different data.

All functions should return first value passed to them to
allow easy inserting print function into expressions.
'''

import os
from difflib import ndiff
import xml.dom.minidom as minidom
from pygments import highlight
from pygments.lexers import XmlLexer
from pygments.formatters import TerminalFormatter
from pprint import pformat

colors = {
    'red': 91,
    'green': 92,
    '-':91, # for diffs
    '+':92,
    '?':94,
}

def xml(text):
    tree = minidom.parseString(text)
    print(highlight(tree.toprettyxml(), XmlLexer(), TerminalFormatter()))
    return text

def print_diff(a, b):
    raise NotImplementedError
    a_lines = render_json(a).splitlines(1)
    b_lines = render_json(b).splitlines(1)
    diff = ndiff(a_lines,b_lines)
 
    for line in diff:
        # TODO: may be use some DiffLexer if such exists?
        print('\033[%sm%s\033[0m'% (colors.get(line[0],0), line[:-1]))


def get_console_width():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)

def wrap(text, max_width=None):
    if max_width is None:
        max_width = get_console_width()

    lines = text.splitlines()
    res = []
    for l in lines:
        while True:
            cut = l[:max_width]
            if cut:
                res.append(cut)
            else:
                break
            l = l[max_width:]
    return '\n'.join(res)

def bordered(text, max_width=None):
    '''
┌─┐  ╔═╗
│ │  ║ ║
└─┘  ╚═╝
    '''
    lines = wrap(text, max_width).splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


def pprint(*args):
    for arg in args:
        print(bordered(pformat(arg)))
    return args[0]
