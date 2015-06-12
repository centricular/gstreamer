gst_c_args = ['-DHAVE_CONFIG_H',
]

executable('gst-inspect-1.0',
'gst-inspect.c', gstenum_h,
install: true,
dependencies : [glib_dep, gobject_dep, gmodule_dep, mathlib],
include_directories: configinc,
link_with: [libgst, printf_lib],
c_args: gst_c_args,
)

executable('gst-launch-1.0',
'gst-launch.c', gstenum_h,
install: true,
dependencies : [glib_dep, gobject_dep, gmodule_dep, mathlib],
include_directories: configinc,
link_with: [libgst, printf_lib],
c_args: gst_c_args,
)

executable('gst-typefind-1.0',
'gst-typefind.c', gstenum_h,
install: true,
dependencies : [glib_dep, gobject_dep, gmodule_dep, mathlib],
include_directories: configinc,
link_with: [libgst, printf_lib],
c_args: gst_c_args,
)
