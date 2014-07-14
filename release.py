#!/usr/bin/env python

# Usage:  $ bin/release <build-dir>

import os.path, sys

manage_file = None

def visit(arg, dirname, names):
    global manage_file
    if (not manage_file) and arg in names:
        manage_file = os.path.join(dirname, arg)

os.path.walk(sys.argv[1], visit, 'manage.py')

print('\n---\nconfig_vars:\n\n')
