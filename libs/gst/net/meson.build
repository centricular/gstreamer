gst_net_sources = [
  'gstnetaddressmeta.c',
  'gstnetclientclock.c',
  'gstnettimepacket.c',
  'gstnettimeprovider.c',
  gstenum_h,
]

gstnet = shared_library('gstnet-@0@'.format(apiversion),
  gst_net_sources,
  c_args : ['-DHAVE_CONFIG_H', '-Wno-pedantic'],
  include_directories : [configinc, libsinc],
  version : gst_version,
  soversion : soversion,
  install : true,
  dependencies : glib_dep,
)
