gst_controller_sources = [
  'gstargbcontrolbinding.c',
  'gstdirectcontrolbinding.c',
  'gsttimedvaluecontrolsource.c',
  'gstinterpolationcontrolsource.c',
  'gsttriggercontrolsource.c',
  'gstlfocontrolsource.c',
  gstenum_h,
]

gstcontroller = shared_library('gstcontroller-@0@'.format(apiversion),
  gst_controller_sources,
  c_args : '-DHAVE_CONFIG_H',
  include_directories : [configinc, libsinc],
  install : true,
  version : gst_version,
  soversion : soversion,
  dependencies : glib_dep,
)
