import sys

def bpython_once(was_here=[]):
    ''' First call starts bpython interactive session. Second - stops program '''
    if was_here:
        sys.exit()
    was_here = [True]
    import bpython
    bpython.embed(sys._getframe(1).f_locals)
