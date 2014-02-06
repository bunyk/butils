# coding=utf-8
from __future__ import print_function
from __future__ import absolute_import

'''
Module for colorfull pretty printing different data.

All functions should return first value passed to them to
allow easy inserting print function into expressions.
'''

import os
import sys
from difflib import ndiff
import xml.dom.minidom as minidom
from pygments import highlight
from pygments.lexers import XmlLexer
from pygments.formatters import TerminalFormatter
from pprint import pformat

colors = {
    'white': 90,
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


def wrap(text, max_width):
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

def bordered(text):
    '''
┌─┐  ╔═╗
│ │  ║ ║
└─┘  ╚═╝
    '''
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

class Printer(object):
    pretty = True
    bordered = False
    max_width = None
    outfile = sys.stdout
    color = None

    def __call__(self, *args):
        out = []
        for arg in args:
            item = pformat(arg) if self.pretty else str(arg)
            if self.max_width: 
                item = wrap(item, self.max_width)
            if self.bordered:
                item = bordered(item)
            out.append(item)
        out = ' '.join(out)
        if self.color:
            out = self.color_code(self.color) + out + self.color_code('white')
        print(out, file=self.outfile)

    def color_code(self, name):
        if name in colors:
            return '\033[%sm' % colors[name]
        else:
            return ''

    @classmethod
    def get_console_width():
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns)

pprint = Printer()
