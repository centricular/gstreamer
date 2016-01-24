gst_base_sources = [
  'gstadapter.c',
  'gstbaseparse.c',
  'gstbasesink.c',
  'gstbasesrc.c',
  'gstbasetransform.c',
  'gstbitreader.c',
  'gstbytereader.c',
  'gstbytewriter.c',
  'gstcollectpads.c',
  'gstdataqueue.c',
  'gstflowcombiner.c',
  'gstpushsrc.c',
  'gstqueuearray.c',
  'gsttypefindhelper.c',
]

gst_base_headers = [
  'base.h',
  'gstadapter.h',
  'gstbaseparse.h',
  'gstbasesink.h',
  'gstbasesrc.h',
  'gstbasetransform.h',
  'gstbitreader.h',
  'gstbytereader.h',
  'gstbytewriter.h',
  'gstcollectpads.h',
  'gstdataqueue.h',
  'gstflowcombiner.h',
  'gstpushsrc.h',
  'gstqueuearray.h',
  'gsttypefindhelper.h',
]

if libtype != 'shared'
  gst_base_static = static_library('gstbase-@0@'.format(apiversion),
    gst_base_sources,
    # This header needs to be generated before building this
    # target can begin
    gstenum_h,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    link_with : libgst_static,
    install : true,
    dependencies : [gobject_dep, glib_dep],
  )
  gst_base = gst_base_static
endif

if libtype != 'static'
  gst_base_shared = shared_library('gstbase-@0@'.format(apiversion),
    gst_base_sources,
    # This header needs to be generated before building this
    # target can begin
    gstenum_h,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    link_with : libgst_shared,
    version : libversion,
    soversion : soversion,
    install : true,
    dependencies : [gobject_dep, glib_dep],
  )
  gst_base = gst_base_shared
  if build_gir
    gnome.generate_gir(gst_base_shared,
      sources : gst_base_sources + gst_base_headers,
      namespace : 'GstBase',
      nsversion : apiversion,
      identifier_prefix : 'Gst',
      symbol_prefix : 'gst',
      export_packages : 'gstreamer-base-1.0',
      link_with : libgst_shared,
      include_directories : [configinc, libsinc, privinc],
      includes : ['GLib-2.0', 'GObject-2.0', 'GModule-2.0', 'Gst-1.0'],
      install : true,
      extra_args : gir_init_section,
    )
  endif
endif

install_headers('base.h',
  'gstadapter.h',
  'gstbaseparse.h',
  'gstbasesink.h',
  'gstbasesrc.h',
  'gstbasetransform.h',
  'gstbitreader.h',
  'gstbytereader.h',
  'gstbytewriter.h',
  'gstcollectpads.h',
  'gstdataqueue.h',
  'gstflowcombiner.h',
  'gstpushsrc.h',
  'gstqueuearray.h',
  'gsttypefindhelper.h',
  subdir : 'gstreamer-1.0/gst/base',
)
