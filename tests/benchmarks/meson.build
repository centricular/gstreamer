benchmarks = [
  'caps',
  'capsnego',
  'complexity',
  'controller',
  'init',
  'mass-elements',
  'gstpollstress',
  'gstpoolstress',
  'gstclockstress',
  'gstbufferstress',
]

foreach b : benchmarks
  executable(b, '@0@.c'.format(b),
    include_directories : [configinc, libsinc],
    link_with : [gst_controller, printf_lib, libgst],
    dependencies : [gobject_dep, gmodule_dep, glib_dep, ],
    )
endforeach
