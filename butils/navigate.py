import inspect

class Location(object):
    filename = None
    line_no = None

    def __str__(self):
        return 'At %s:%s' % (
            self.filename or 'unknown',
            self.line_no or 'unknown'
        )

def whereis(ob):
    l = Location()
    try:
        l.filename = inspect.getsourcefile(ob)
    except TypeError:
        pass
    try:
        l.line_no = inspect.getsourcelines(ob)[1]
    except IOError:
        pass
    return l
