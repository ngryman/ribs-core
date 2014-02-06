{
    'variables': {
        'target_arch%': 'ia32',
        'library%': 'static_library',
        'src': 'src'
    },

    'targets': [{
        'target_name': 'ribs',
        'product_prefix': 'lib',
        'type': '<(library)',

        'sources': [
            '<(src)/error.cc',
            '<(src)/image.cc',
            '<(src)/io.cc',
            '<(src)/math.cc'
        ],

        'dependencies': [
            'deps/libuv/uv.gyp:libuv',
            'deps/libcv/cv.gyp:libcv'
        ],

        'conditions': [
            ['OS=="linux"', {
#                'libraries': [
#                    '-luv'
#                ],
                'cflags': [
                    '-Wall -std=c++11'
                ]
            }]
        ]
    }]
}
