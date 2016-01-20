gst_net_sources = [
  'gstnetaddressmeta.c',
  'gstnetclientclock.c',
  'gstnetcontrolmessagemeta.c',
  'gstnettimepacket.c',
  'gstnettimeprovider.c',
  'gstptpclock.c',
  'gstntppacket.c',
]

gst_net_headers = [
 'gstnet.h',
 'gstnetaddressmeta.h',
 'gstnetclientclock.h',
 'gstnetcontrolmessagemeta.h',
 'gstnettimepacket.h',
 'gstnettimeprovider.h',
 'gstptpclock.h',
]

if libtype != 'shared'
  gst_net_static = static_library('gstnet-@0@'.format(apiversion),
    gst_net_sources, gstenum_h,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    link_with : [ gst_base_static, libgst_static ],
    install : true,
    dependencies : [gobject_dep, gio_dep, glib_dep],
  )
  gst_net = gst_net_static
endif

if libtype != 'static'
  gst_net_shared = shared_library('gstnet-@0@'.format(apiversion),
    gst_net_sources, gstenum_h,
    c_args : ['-DHAVE_CONFIG_H'],
    include_directories : [configinc, libsinc],
    link_with : [ gst_base_shared, libgst_shared ],
    version : gst_version,
    soversion : soversion,
    install : true,
    dependencies : [gobject_dep, gio_dep, glib_dep],
  )
  gst_net = gst_net_shared
  if build_gir
    gnome.generate_gir(gst_net_shared,
      sources : gst_net_sources + gst_net_headers,
      namespace : 'GstNet',
      nsversion : apiversion,
      identifier_prefix : 'Gst',
      symbol_prefix : 'gst',
      export_packages : 'gstreamer-net-1.0',
      link_with : libgst_shared,
      include_directories : [configinc, libsinc, privinc],
      includes : ['GLib-2.0', 'GObject-2.0', 'GModule-2.0', 'Gio-2.0', 'Gst-1.0'],
      install : true,
      extra_args : gir_init_section,
    )
  endif
endif
