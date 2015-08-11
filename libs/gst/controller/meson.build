gst_controller_sources = [
  'gstargbcontrolbinding.c',
  'gstdirectcontrolbinding.c',
  'gsttimedvaluecontrolsource.c',
  'gstinterpolationcontrolsource.c',
  'gsttriggercontrolsource.c',
  'gstlfocontrolsource.c',
  gstenum_h,
]

if libtype != 'shared'
  gst_controller_static = static_library('gstcontroller-@0@'.format(apiversion),
    gst_controller_sources,
    c_args : ['-DHAVE_CONFIG_H','-DGST_PLUGIN_BUILD_STATIC'],
    include_directories : [configinc, libsinc],
    install : true,
    dependencies : glib_dep,
  )
  gst_controller = gst_controller_static
endif

if libtype != 'static'
  gst_controller_shared = shared_library('gstcontroller-@0@'.format(apiversion),
    gst_controller_sources,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    install : true,
    version : gst_version,
    soversion : soversion,
    dependencies : glib_dep,
  )
  gst_controller = gst_controller_shared
endif
