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

printf_args = [
#  '-UHAVE_LONG_DOUBLE',
#  '-UHAVE_LONG_LONG_FORMAT',
#  ' -UHAVE_WCHAR_T',
#  '-UHAVE_WCSLEN',
#  '-UHAVE_WINT_T',
  '-DSTATIC=G_GNUC_INTERNAL',
  '-DHAVE_CONFIG_H=1',
]

if libtype != 'shared'
  printf_lib_static = static_library('gstprintf',
    printf_sources,
    include_directories : [configinc],
    c_args : printf_args,
    install : true,
    dependencies : [glib_dep],
  )
  printf_lib = printf_lib_static
endif

if libtype != 'static'
  printf_lib_shared = shared_library('gstprintf',
    printf_sources,
    include_directories : [configinc],
    c_args : printf_args,
    install : true,
    dependencies : [glib_dep],
  )
  printf_lib = printf_lib_shared
endif
