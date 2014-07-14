#!/usr/bin/env python

# Usage:  $ bin/release <build-dir>

import os.path, sys

build_dir = sys.argv[1]

if (os.path.isfile(os.path.join(build_dir, 'requirements.txt'))
 or os.path.isfile(os.path.join(build_dir, 'setup.py'))):
    print('Python')
else:
    sys.exit(1)
