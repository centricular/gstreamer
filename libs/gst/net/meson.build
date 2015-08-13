gst_net_sources = [
  'gstnetaddressmeta.c',
  'gstnetclientclock.c',
  'gstnettimepacket.c',
  'gstnettimeprovider.c',
]

gst_net_headers = [
 'gstnet.h',
 'gstnetaddressmeta.h',
 'gstnetclientclock.h',
 'gstnettimepacket.h',
 'gstnettimeprovider.h',
]

if libtype != 'shared'
  gst_net_static = static_library('gstnet-@0@'.format(apiversion),
    gst_net_sources, gstenum_h,
    c_args : ['-DHAVE_CONFIG_H', '-DGST_PLUGIN_BUILD_STATIC'],
    include_directories : [configinc, libsinc],
    install : true,
    dependencies : glib_dep,
  )
  gst_net = gst_net_static
endif

if libtype != 'static'
  gst_net_shared = shared_library('gstnet-@0@'.format(apiversion),
    gst_net_sources, gstenum_h,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    version : gst_version,
    soversion : soversion,
    install : true,
    dependencies : glib_dep,
  )
  gst_net = gst_net_shared
  if gir.found()
    gnome.generate_gir(gst_net_shared,
      sources : gst_net_sources + gst_net_headers,
      namespace : 'GstNet',
      nsversion : gst_version,
      link_with : libgst_shared,
      include_directories : [configinc, libsinc, privinc],
      includes : ['GLib-2.0', 'GObject-2.0', 'GModule-2.0'],
      install : true,
      extra_args : ['--strip-prefix=Gst', '--add-init-section=gst_init(NULL,NULL);'],
    )
  endif
endif
