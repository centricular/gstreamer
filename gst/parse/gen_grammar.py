#!/usr/bin/env python3

import subprocess, sys

cfile = sys.argv[1]
hfile = sys.argv[2]
yfile = sys.argv[3]

subprocess.check_call(['bison', '-d', '-v', '-ppriv_gst_parse_yy', yfile, '-o', cfile])

prefix = '''
#ifdef HAVE_CONFIG_H
#include<config.h>
#endif
'''

contents = open(cfile).read()
content = prefix + contents
open(cfile, 'w').write(contents)
