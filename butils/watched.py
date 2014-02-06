from __future__ import print_function
import sys
import inspect

from .pprint import pprint
 
def from_where_called():
    info = inspect.getframeinfo(sys._getframe(2))
    # info about frame two frames higher than current
    # (function which called functions which called this function :) )
    code = info.code_context[0] if info.code_context else ''
    return '%s:%s %s' % (info.filename, info.lineno, code)
 
def add_watched_attribute(name, watch_get=False):  
    def attr_watch_get(self):
        value = getattr(self, '_' + name, 'unset')
        if watch_get:
            pprint(from_where_called(), name, 'is', value)
        return value
 
    def attr_watch_set(self, value):
        pprint(from_where_called(), name, 'set to', value)
        setattr(self, '_' + name, value)
 
    sys._getframe(1).f_locals[name] = property(attr_watch_get, attr_watch_set)


def watch_for_output(condition=lambda x: True, stream='stdout'):
    original_stream = getattr(sys, stream)

    class NewStream(object):
        def write(self, txt):
            original_stream.write(txt)
            if condition(txt):
                original_stream.write(from_where_called() + '\n')

    setattr(sys, stream, NewStream())


def log_lines():
    current_file = inspect.getframeinfo(sys._getframe(1)).filename
    pprint('Tracing is ON in %r' % current_file)

    def tracer(frame, event, arg):
        if event != 'line':
            return tracer

        info = inspect.getframeinfo(frame)
        code = info.code_context[0] if info.code_context else ''
        if info.filename == current_file:
            pprint('Executing %s:%s %s' % (info.filename, info.lineno, code))

        return tracer

    old_trace = sys.gettrace()
    def restore():
        sys.settrace(old_trace)

    sys.settrace(tracer)

    return restore
