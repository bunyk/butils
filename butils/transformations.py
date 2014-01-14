
class func_to_dict(object):
    ''' Converts function of one hashable argument to dictionary-like
        object which "contains" all it returning values. '''
    def __init__(self, f):
        self.f = f

    def __getitem__(self, key):
        return f(key)
