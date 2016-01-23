have_trace = not get_option('disable_trace')
have_registry = not get_option('disable_registry')

# tests and condition when to skip the test
core_tests = [
  [ 'gst/gst', not have_registry ],
  [ 'gst/gstatomicqueue' ],
  [ 'gst/gstbuffer' ],
  [ 'gst/gstbufferlist' ],
  [ 'gst/gstbufferpool' ],
  [ 'gst/gstchildproxy', not have_registry ],
  [ 'gst/gstclock' ],
  [ 'gst/gstcontext' ],
  [ 'gst/gstcontroller' ],
  [ 'gst/gstcaps' ],
  [ 'gst/gstcapsfeatures' ],
  [ 'gst/gstdatetime' ],
  [ 'gst/gstdevice' ],
  [ 'gst/gstelement', not have_registry ],
  [ 'gst/gstelementfactory', not have_registry ],
  [ 'gst/gstghostpad', not have_registry ],
  [ 'gst/gstinfo' ],
  [ 'gst/gstiterator' ],
  [ 'gst/gstmessage' ],
  [ 'gst/gstmemory' ],
  [ 'gst/gstmeta' ],
  [ 'gst/gstminiobject' ],
  [ 'gst/gstobject' ],
  [ 'gst/gstpad', not have_registry ],
  [ 'gst/gstparamspecs' ],
  [ 'gst/gstpipeline', not have_registry ],
  [ 'gst/gstpoll' ],
  [ 'gst/gstplugin', not have_registry ],
  [ 'gst/gstpreset' ],
  [ 'gst/gstprotection' ],
  [ 'gst/gstquery', not have_registry ],
  [ 'gst/gstregistry', not have_registry ],
  [ 'gst/gstsegment' ],
  [ 'gst/gststructure' ],
  [ 'gst/gstsystemclock' ],
  [ 'gst/gsttag' ],
  [ 'gst/gsttagsetter' ],
  [ 'gst/gsttask' ],
  [ 'gst/gsttoc' ],
  [ 'gst/gsttocsetter' ],
  [ 'gst/gsturi' ],
  [ 'gst/gstutils', not have_registry ],
  [ 'gst/gstvalue' ],
  [ 'generic/states', not have_registry ],
  [ 'libs/adapter' ],
  [ 'libs/baseparse' ],
  [ 'libs/basesrc', not have_registry ],
  [ 'libs/basesink', not have_registry ],
  [ 'libs/bitreader' ],
  [ 'libs/bytereader' ],
  [ 'libs/bytewriter' ],
  [ 'libs/bitreader-noinline' ],
  [ 'libs/bytereader-noinline' ],
  [ 'libs/bytewriter-noinline' ],
  [ 'libs/collectpads', not have_registry ],
  [ 'libs/controller' ],
  [ 'libs/flowcombiner' ],
  [ 'libs/gstnetclientclock' ],
  [ 'libs/gstnettimeprovider' ],
  [ 'libs/gsttestclock' ],
  [ 'libs/sparsefile' ],
  [ 'libs/transform1' ],
  [ 'libs/typefindhelper' ],
  [ 'libs/queuearray' ],
  [ 'elements/capsfilter', not have_registry ],
  [ 'elements/concat', not have_registry ],
  [ 'elements/fakesrc', not have_registry ],
  [ 'elements/fdsrc', not have_registry ],
  [ 'elements/filesink', not have_registry ],
  [ 'elements/filesrc', not have_registry ],
  [ 'elements/funnel', not have_registry ],
  [ 'elements/identity', not have_registry ],
  [ 'elements/multiqueue', not have_registry ],
  [ 'elements/selector', not have_registry ],
  [ 'elements/streamiddemux', not have_registry ],
  [ 'elements/tee', not have_registry ],
  [ 'elements/queue', not have_registry ],
  [ 'elements/queue2', not have_registry ],
  [ 'elements/valve', not have_registry ],
  [ 'pipelines/seek', not have_registry ],
  [ 'pipelines/queue-error', not have_registry ],
  [ 'tools/gstinspect' ],
  # These take quite long, put them at the end
  [ 'elements/fakesink', not have_registry ],
  [ 'gst/gstbin', not have_registry ],
  [ 'gst/gstbus', not have_registry ],
  [ 'gst/gstevent', not have_registry ],
  [ 'pipelines/stress', not have_registry ],
  [ 'generic/sinks', not have_registry ],
]

test_defines = [
  '-UG_DISABLE_ASSERT',
  '-UG_DISABLE_CAST_CHECKS',
  '-DGST_CHECK_TEST_ENVIRONMENT_BEACON="GST_STATE_IGNORE_ELEMENTS"',
  '-DTESTFILE="' + meson.current_source_dir() + '/meson.build"',
]

test_env = [
  'GST_SYSTEM_PLUGIN_PATH=',
  'GST_PLUGIN_PATH=' + meson.build_root() + '/plugins',
  'GST_PLUGIN_SCANNER='+ meson.build_root() + '/libs/gst/helpers/gst-plugin-scanner',
  'GST_STATE_IGNORE_ELEMENTS=',
  'CK_DEFAULT_TIMEOUT=20',
]

foreach t : core_tests
  test_name = t.get(0)
  if t.length() == 2
    skip_test = t.get(1)
  else
    skip_test = false
  endif
  if not skip_test
    exe = executable(test_name, '@0@.c'.format(test_name),
      gstenum_h,
      include_directories : [configinc, libsinc],
      c_args : ['-DHAVE_CONFIG_H=1'] + test_defines,
      link_with : [gst_check, gst_net, gst_base, gst_controller, libgst],
      dependencies : [gio_dep, gobject_dep, gmodule_dep, glib_dep],
    )
    test(test_name, exe,
      env: test_env + [ 'GST_REGISTRY=@0@/@1@.registry'.format(meson.current_build_dir(), test_name) ]
    )
  endif
endforeach

if have_registry
  test('gstcpp', executable('gstcpp', 'gst/gstcpp.cc',
    gstenum_h,
    include_directories : [configinc, libsinc],
    cpp_args : ['-DHAVE_CONFIG_H=1'] + test_defines,
    link_with : [gst_check, gst_controller, gst_net, gst_base, libgst],
    dependencies : [gio_dep, gobject_dep, gmodule_dep, glib_dep]),
    env: test_env + [ 'GST_REGISTRY=@0@/gstcpp.registry'.format(meson.current_build_dir()) ])
endif

test('gstlibscpp', executable('gstlibscpp', 'libs/gstlibscpp.cc',
    gstenum_h,
    include_directories : [configinc, libsinc],
    cpp_args : ['-DHAVE_CONFIG_H=1'],
    link_with : [gst_check, gst_controller, gst_net, gst_base, libgst],
    dependencies : [gio_dep, gobject_dep, gmodule_dep, glib_dep]),
    env: test_env + [ 'GST_REGISTRY=@0@/gstlibscpp.registry'.format(meson.current_build_dir()) ])
