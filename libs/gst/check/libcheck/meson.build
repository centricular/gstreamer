libcheck_files = [
  'check.c',
  'check_error.c',
  'check_list.c',
  'check_log.c',
  'check_msg.c',
  'check_pack.c',
  'check_print.c',
  'check_run.c',
  'check_str.c',
]

configure_file(input : 'check.h.in',
  output : 'check.h',
  configuration : check_cdata)

libcheck = shared_library('check',
  libcheck_files,
  include_directories : configinc)
