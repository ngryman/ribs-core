{
    'variables': {
        'target_arch%': 'ia32',
        'library%': 'static_library',
        'with_test%': 0
    },

    'target_defaults': {
        'conditions': [
            ['OS=="linux"', {
                'cflags': [
                    '-Wall -std=c++11'
                ]
            }]
        ]
    },

    'targets': [{
        'target_name': 'ribs',
        'product_prefix': 'lib',
        'type': '<(library)',

        'sources': [
            'src/error.cc',
            'src/image.cc'
        ],

        'include_dirs': [
            'include'
        ],

        'dependencies': [
            'deps/libcv/cv.gyp:libcv'
        ]
    }],

    'conditions': [
        ['with_test==1', {
            'targets': [{
                'target_name': 'run-tests',
                'type': 'executable',

                'sources': [
                    'test/run-tests.cc'
                ],

                'dependencies': [
                    'ribs'
                ],

                'include_dirs': [
                    'include',
                    'deps/catch/include'
                ]
            }],
        }],
    ]
}
