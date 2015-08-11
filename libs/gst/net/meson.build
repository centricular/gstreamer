gst_net_sources = [
  'gstnetaddressmeta.c',
  'gstnetclientclock.c',
  'gstnettimepacket.c',
  'gstnettimeprovider.c',
  gstenum_h,
]

if libtype != 'shared'
  gst_net_static = static_library('gstnet-@0@'.format(apiversion),
    gst_net_sources,
    c_args : ['-DHAVE_CONFIG_H', '-DGST_PLUGIN_BUILD_STATIC'],
    include_directories : [configinc, libsinc],
    install : true,
    dependencies : glib_dep,
  )
  gst_net = gst_net_static
endif

if libtype != 'static'
  gst_net_shared = shared_library('gstnet-@0@'.format(apiversion),
    gst_net_sources,
    c_args : ['-DHAVE_CONFIG_H', '-Wno-pedantic'],
    include_directories : [configinc, libsinc],
    version : gst_version,
    soversion : soversion,
    install : true,
    dependencies : glib_dep,
  )
  gst_net = gst_net_shared
endif
