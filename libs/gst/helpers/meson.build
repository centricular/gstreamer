gst_plugin_scanner = executable('gst-plugin-scanner',
  'gst-plugin-scanner.c',
  c_args : '-DHAVE_CONFIG_H',
  include_directories : [configinc],
  dependencies : [gobject_dep, gmodule_dep, glib_dep, mathlib],
  link_with : [libgst, printf_lib],
)
