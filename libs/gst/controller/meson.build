gst_controller_sources = [
  'gstargbcontrolbinding.c',
  'gstdirectcontrolbinding.c',
  'gsttimedvaluecontrolsource.c',
  'gstinterpolationcontrolsource.c',
  'gsttriggercontrolsource.c',
  'gstlfocontrolsource.c',
]

gst_controller_headers = [
  'gstargbcontrolbinding.h',
  'gstdirectcontrolbinding.h',
  'gsttimedvaluecontrolsource.h',
  'gstinterpolationcontrolsource.h',
  'gsttriggercontrolsource.h',
  'gstlfocontrolsource.h',
]

if libtype != 'shared'
  gst_controller_static = static_library('gstcontroller-@0@'.format(apiversion),
    gst_controller_sources,
    gstenum_h,
    c_args : ['-DHAVE_CONFIG_H','-DGST_PLUGIN_BUILD_STATIC'],
    include_directories : [configinc, libsinc],
    link_with : libgst,
    install : true,
    dependencies : [gobject_dep, glib_dep],
  )
  gst_controller = gst_controller_static
endif

if libtype != 'static'
  gst_controller_shared = shared_library('gstcontroller-@0@'.format(apiversion),
    gst_controller_sources,
    gstenum_h,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    install : true,
    version : gst_version,
    link_with : libgst,
    soversion : soversion,
    dependencies : [gobject_dep, glib_dep],
  )
  gst_controller = gst_controller_shared
  if gir.found()
    gnome.generate_gir(gst_controller_shared,
      sources : gst_controller_sources + gst_controller_headers,
      namespace : 'GstController',
      nsversion : apiversion,
      link_with : libgst_shared,
      include_directories : [configinc, libsinc, privinc],
      install : true,
      extra_args : ['--strip-prefix=Gst', '--add-init-section=gst_init(NULL,NULL);'],
    )
  endif
endif
