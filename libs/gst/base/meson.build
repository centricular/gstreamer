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
  'gsttypefindhelper.c'
]

gst_base = shared_library('gstbase-@0@'.format(apiversion),
  gst_base_sources,
  # This header needs to be generated before building this
  # target can begin
  gstenum_h,
  c_args : '-DHAVE_CONFIG_H',
  include_directories : [configinc, libsinc],
  version : gst_version,
  soversion : soversion,
  install : true,
  dependencies : glib_dep,
)
