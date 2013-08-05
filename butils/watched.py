import sys
import inspect
 
def from_where_called():
    info = inspect.getframeinfo(sys._getframe(2))
    # info about frame two frames higher than current
    # (function which called functions which called this function :) )
    code = info.code_context[0] if info.code_context else ''
    return '%s:%s %s' % (info.filename, info.lineno, code)
 
def add_watched_attribute(name):  
    def attr_watch_get(self):
        value = getattr(self, '_' + name, 'unset')
        print from_where_called(), name, 'is', value
        return value
 
    def attr_watch_set(self, value):
        print from_where_called(), name, 'set to', value
        setattr(self, '_' + name, value)
 
    sys._getframe(1).f_locals[name] = property(attr_watch_get, attr_watch_set)
