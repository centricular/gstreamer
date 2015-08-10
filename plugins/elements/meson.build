gst_elements_sources = [
  'gstcapsfilter.c',
  'gstdownloadbuffer.c',
  'gstelements.c',
  'gstelements_private.c',
  'gstfakesrc.c',
  'gstfakesink.c',
  'gstfdsrc.c',
  'gstfdsink.c',
  'gstfilesink.c',
  'gstfilesrc.c',
  'gstfunnel.c',
  'gstidentity.c',
  'gstinputselector.c',
  'gstoutputselector.c',
  'gstmultiqueue.c',
  'gstqueue.c',
  'gstqueue2.c',
  'gstsparsefile.c',
  'gsttee.c',
  'gsttypefindelement.c',
  'gstvalve.c',
  gstenum_h,
]

if libtype != 'shared'
  gst_elements_static = static_library('gstcoreelements',
    gst_elements_sources,
    c_args : ['-DHAVE_CONFIG_H', '-Wno-pedantic'],
    include_directories : [configinc, libsinc],
    link_with : libgst,
    dependencies : glib_dep,
    install : true,
    install_dir : '@0@/gstreamer-1.0'.format(get_option('libdir')),
  )
  gst_elements = gst_elements_static
endif

if libtype != 'static'
  gst_elements_shared = shared_library('gstcoreelements',
    gst_elements_sources,
    c_args : ['-DHAVE_CONFIG_H', '-Wno-pedantic'],
    include_directories : [configinc, libsinc],
    link_with : libgst,
    dependencies : glib_dep,
    install : true,
    install_dir : '@0@/gstreamer-1.0'.format(get_option('libdir')),
  )
  gst_elements = gst_elements_shared
endif
