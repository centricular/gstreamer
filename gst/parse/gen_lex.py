#!/usr/bin/env python3

import sys, subprocess

cfile = sys.argv[1]
hfile = sys.argv[2]
lfile = sys.argv[3]
tabhfile = sys.argv[4]

subprocess.check_call(['flex', '--header-file=' + hfile, '-o', cfile, '-Ppriv_gst_parse_yy', lfile])

prefix = '''#ifdef HAVE_CONFIG_H
#include<config.h>
#endif
'''
parse_snippet = '''void priv_gst_parse_yyset_column (int column_no , void * yyscanner);
void priv_gst_parse_yyset_column (int column_no , void * yyscanner)
'''

contents = open(hfile).read()
if not 'priv_gst_parse_yyget_column' in contents:
    contents = parse_snippet + contents
contents = prefix + contents

open(hfile, 'w').write(contents)
