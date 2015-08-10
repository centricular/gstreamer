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
  gstenum_h,
]

if libtype != 'shared'
  gst_base_static = static_library('gstbase-@0@'.format(apiversion),
    gst_base_sources,
    # This header needs to be generated before building this
    # target can begin
    gstenum_h,
    c_args : ['-DHAVE_CONFIG_H', '-Wno-pedantic'],
    include_directories : [configinc, libsinc],
    install : true,
    dependencies : glib_dep,
  )
  gst_base = gst_base_static
endif

if libtype != 'static'
  gst_base_shared = shared_library('gstbase-@0@'.format(apiversion),
    gst_base_sources,
    # This header needs to be generated before building this
    # target can begin
    gstenum_h,
    c_args : ['-DHAVE_CONFIG_H', '-Wno-pedantic'],
    include_directories : [configinc, libsinc],
    version : gst_version,
    soversion : soversion,
    install : true,
    dependencies : glib_dep,
  )
  gst_base = gst_base_shared
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
