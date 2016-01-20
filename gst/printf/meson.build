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

# FIXME: need a way to find portable c_args for -fPIC
printf_lib = static_library('gstprintf',
    printf_sources, gstenum_h,
    include_directories : [configinc],
    c_args : [printf_args, '-fPIC'],
    install : false,
    dependencies : [glib_dep])
