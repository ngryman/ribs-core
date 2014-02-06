#
# ribs
# Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
# LGPL Licensed
#
# For OpenCV, here is the gyp file that inspired us:
#   https://code.google.com/p/modpagespeed/source/browse/trunk/src/third_party/opencv/opencv.gyp?r=1391

{
    'variables': {
        'root': 'src',
        'src': '<(root)/modules/core/src',
    },

    'targets': [{
        'target_name': 'libuv',
        'type': '<(library)',

        'dependencies': [
            'src/uv.gyp:libuv'
        ],

        'direct_dependent_settings': {
            'include_dirs': [
                '<(root)/include',
                '<(root)/modules/core/include',
            ],
        },
    }]
}
