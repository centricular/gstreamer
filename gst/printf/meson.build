# This behaves differently to the original. It builds
# as a standalone library for simplicity.

printf_sources = [
  'asnprintf.c',
  'printf-args.c',
  'printf-parse.c',
  'vasnprintf.c',
  'printf.c',
  'printf-extension.c',
]

printf_lib = shared_library('gstprintf',
  printf_sources,
  include_directories : [configinc],
  install : true,
  dependencies : [glib_dep],
)
