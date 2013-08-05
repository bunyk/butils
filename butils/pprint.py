'''
Module for colorfull pretty printing different data.

All functions should return first value passed to them to
allow easy inserting print function into expressions.
'''

from difflib import ndiff
 
colors ={
    '-':91, # for diffs
    '+':92,
    '?':94,
}

import xml.dom.minidom
from pygments import highlight
from pygments.lexers import XmlLexer
from pygments.formatters import TerminalFormatter

def xml(text):
    xml = xml.dom.minidom.parseString(text)
    print highlight(xml.toprettyxml(), XmlLexer(), TerminalFormatter())
    return text

def print_diff(a,b):
    a_lines = render_json(a).splitlines(1)
    b_lines = render_json(b).splitlines(1)
    diff = ndiff(a_lines,b_lines)
 
    for line in diff:
        # TODO: may be use some DiffLexer if such exists?
        print '\033[%sm%s\033[0m'% (colors.get(line[0],0), line[:-1])
