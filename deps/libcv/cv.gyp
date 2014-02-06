#
# ribs
# Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
# LGPL Licensed
#
# For OpenCV, here is the gyp file that inspired us:
#   https://code.google.com/p/modpagespeed/source/browse/trunk/src/third_party/opencv/opencv.gyp?r=1391

{
    'variables': {
        'target_arch%': 'ia32',
        'library%': 'static_library',
        'gen': 'gen/arch/<(OS)/<(target_arch)',
        'root': 'src',
        'root_core': '<(root)/modules/core',
        'root_imgproc': '<(root)/modules/imgproc',
        'root_highgui': '<(root)/modules/highgui',
    },

    'targets': [{
        'variables': {
            'module_root': '<(root)/modules/core',
            'src': '<(module_root)/src'
        },

        'target_name': 'opencv_core',
        'type': '<(library)',

        'sources': [
            '<(src)/alloc.cpp',
            '<(src)/arithm.cpp',
            '<(src)/array.cpp',
            '<(src)/cmdparser.cpp',
            '<(src)/convert.cpp',
            '<(src)/copy.cpp',
            '<(src)/datastructs.cpp',
            '<(src)/drawing.cpp',
            '<(src)/dxt.cpp',
            '<(src)/lapack.cpp',
            '<(src)/mathfuncs.cpp',
            '<(src)/matmul.cpp',
            '<(src)/matop.cpp',
            '<(src)/matrix.cpp',
            '<(src)/out.cpp',
            # Since persistence.cpp would pull in the gzip I/O layer for zlib,
            # we simply stub out the one symbol that's referenced to it
            # and not actually called.
#            '<(DEPTH)/third_party/opencv/persistence_stub.cpp',
#            '<(src)/precomp.cpp',
            '<(src)/rand.cpp',
            '<(src)/stat.cpp',
            '<(src)/system.cpp',
            '<(src)/tables.cpp'
        ],

        'include_dirs': [
            '<(root)/include',
            '<(root_core)/include',
            '<(gen)/include'
        ],

        'direct_dependent_settings': {
            'include_dirs': [
#                '<(root)/include',
#                '<(module_root)/include'
                '<(gen)/include'
            ],
        },

        'defines': [
            '__OPENCV_BUILD=1'
        ]
    }, {
        'variables': {
            'module_root': '<(root)/modules/imgproc',
            'src': '<(module_root)/src'
        },

        'target_name': 'opencv_imgproc',
        'type': '<(library)',

        'dependencies': [
            'opencv_core',
        ],

        'sources': [
            '<(src)/accum.cpp',
            '<(src)/approx.cpp',
            '<(src)/canny.cpp',
            '<(src)/color.cpp',
            '<(src)/contours.cpp',
            '<(src)/convhull.cpp',
            '<(src)/corner.cpp',
            '<(src)/cornersubpix.cpp',
            '<(src)/deriv.cpp',
            '<(src)/distransform.cpp',
            '<(src)/emd.cpp',
            '<(src)/featureselect.cpp',
#            '<(src)/featuretree.cpp',
            '<(src)/filter.cpp',
            '<(src)/floodfill.cpp',
            '<(src)/geometry.cpp',
            '<(src)/grabcut.cpp',
            '<(src)/histogram.cpp',
            '<(src)/hough.cpp',
            '<(src)/imgwarp.cpp',
#            '<(src)/inpaint.cpp',
#            '<(src)/kdtree.cpp',
            '<(src)/linefit.cpp',
#            '<(src)/lsh.cpp',
            '<(src)/matchcontours.cpp',
            '<(src)/moments.cpp',
            '<(src)/morph.cpp',
#            '<(src)/precomp.cpp',
            '<(src)/pyramids.cpp',
#            '<(src)/pyrsegmentation.cpp',
            '<(src)/rotcalipers.cpp',
            '<(src)/samplers.cpp',
            '<(src)/segmentation.cpp',
            '<(src)/shapedescr.cpp',
            '<(src)/smooth.cpp',
#            '<(src)/spilltree.cpp',
            '<(src)/subdivision2d.cpp',
            '<(src)/sumpixels.cpp',
            '<(src)/tables.cpp',
            '<(src)/templmatch.cpp',
            '<(src)/thresh.cpp',
            '<(src)/undistort.cpp',
            '<(src)/utils.cpp',
        ],

        'include_dirs': [
            '<(root_imgproc)/include',
        ],

        'direct_dependent_settings': {
            'include_dirs': [
                '<(module_root)/include'
            ],
        },
    }, {
        'variables': {
            'module_root': '<(root)/modules/highgui',
            'src': '<(module_root)/src'
        },

        'target_name': 'libcv',
        'type': '<(library)',

        'dependencies': [
            'opencv_imgproc',
        ],

        'sources': [
            '<(src)/bitstrm.cpp',
            '<(src)/cap.cpp',
            '<(src)/grfmt_base.cpp',
            '<(src)/grfmt_bmp.cpp',
            '<(src)/grfmt_jpeg.cpp',
            '<(src)/grfmt_png.cpp',
            '<(src)/grfmt_pxm.cpp',
            '<(src)/grfmt_sunras.cpp',
            '<(src)/grfmt_tiff.cpp',
            '<(src)/loadsave.cpp',
#            '<(src)/precomp.cpp',
            '<(src)/utils.cpp'
        ],

        'include_dirs': [
            '<(module_root)/include',
            '<(root)/modules/core/include',
            '<(gen)/include'
        ],

        'direct_dependent_settings': {
            'include_dirs': [
                '<(root)/include',
                '<(root_highgui)/include'
            ],
        },

        'defines': [
            '__OPENCV_BUILD=1'
        ]
    }]
}