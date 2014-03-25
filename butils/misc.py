import sys
import pickle

def bpython_once(was_here=[]):
    ''' First call starts bpython interactive session. Second - stops program '''
    if was_here:
        sys.exit()
    was_here = [True]
    import bpython
    bpython.embed(sys._getframe(1).f_locals)


def save_object(object, filename):
    with open(filename, 'w') as f:
        pickle.dump(f, object)

def load_object(filename):
    try:
        with open(filename) as f:
            return pickle.load(f)
    except IOError:
        return None

