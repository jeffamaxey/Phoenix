#!/usr/bin/env python

import wx.py as py

#----------------------------------------------------------------------

intro = f'Welcome To PyCrust {py.version.VERSION} - The Flakiest Python Shell'

def runTest(frame, nb, log):
    return py.shell.Shell(nb, -1, introText=intro)

#----------------------------------------------------------------------

overview = py.shell.__doc__


if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

