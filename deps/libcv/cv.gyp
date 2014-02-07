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
	},

	'targets': [{
		'variables': {
			'module_root': '<(root)/3rdparty/libjpeg',
			'src': '<(module_root)'
		},

		'target_name': 'libjpeg',
		'type': '<(library)',

		'sources': [
			'<(src)/jcapimin.c',
            '<(src)/jcapistd.c',
            '<(src)/jccoefct.c',
            '<(src)/jccolor.c',
            '<(src)/jcdctmgr.c',
            '<(src)/jchuff.c',
            '<(src)/jcinit.c',
            '<(src)/jcmainct.c',
            '<(src)/jcmarker.c',
            '<(src)/jcmaster.c',
            '<(src)/jcomapi.c',
            '<(src)/jcparam.c',
            '<(src)/jcphuff.c',
            '<(src)/jcprepct.c',
            '<(src)/jcsample.c',
            '<(src)/jctrans.c',
            '<(src)/jdapimin.c',
            '<(src)/jdapistd.c',
            '<(src)/jdatadst.c',
            '<(src)/jdatasrc.c',
            '<(src)/jdcoefct.c',
            '<(src)/jdcolor.c',
            '<(src)/jddctmgr.c',
            '<(src)/jdhuff.c',
            '<(src)/jdinput.c',
            '<(src)/jdmainct.c',
            '<(src)/jdmarker.c',
            '<(src)/jdmaster.c',
            '<(src)/jdmerge.c',
            '<(src)/jdphuff.c',
            '<(src)/jdpostct.c',
            '<(src)/jdsample.c',
            '<(src)/jdtrans.c',
            '<(src)/jerror.c',
            '<(src)/jfdctflt.c',
            '<(src)/jfdctfst.c',
            '<(src)/jfdctint.c',
            '<(src)/jidctflt.c',
            '<(src)/jidctfst.c',
            '<(src)/jidctint.c',
            '<(src)/jidctred.c',
            '<(src)/jmemansi.c',
            '<(src)/jmemmgr.c',
            '<(src)/jquant1.c',
            '<(src)/jquant2.c',
            '<(src)/jutils.c',
            '<(src)/transupp.c'
		]
	}, {
		'variables': {
			'module_root': '<(root)/3rdparty/libpng',
			'src': '<(module_root)'
		},

		'target_name': 'libpng',
		'type': '<(library)',

		'sources': [
			'<(src)/png.c',
            '<(src)/pngerror.c',
            '<(src)/pngget.c',
            '<(src)/pngmem.c',
            '<(src)/pngpread.c',
            '<(src)/pngread.c',
            '<(src)/pngrio.c',
            '<(src)/pngrtran.c',
            '<(src)/pngrutil.c',
            '<(src)/pngset.c',
            '<(src)/pngtrans.c',
            '<(src)/pngwio.c',
            '<(src)/pngwrite.c',
            '<(src)/pngwtran.c',
            '<(src)/pngwutil.c'
		]
	}, {
		'variables': {
			'module_root': '<(root)/3rdparty/zlib',
			'src': '<(module_root)'
		},

		'target_name': 'zlib',
		'type': '<(library)',

		'sources': [
			'<(src)/compress.c',
            '<(src)/crc32.c',
            '<(src)/deflate.c',
            '<(src)/gzclose.c',
            '<(src)/gzlib.c',
            '<(src)/gzread.c',
            '<(src)/gzwrite.c',
            '<(src)/infback.c',
            '<(src)/inffast.c',
            '<(src)/inflate.c',
            '<(src)/inftrees.c',
            '<(src)/trees.c',
            '<(src)/uncompr.c',
#            zconf.h.cmakein
            '<(src)/zutil.c'
		]
	}, {
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
			'<(src)/persistence.cpp',
#			'<(src)/precomp.cpp',
			'<(src)/rand.cpp',
			'<(src)/stat.cpp',
			'<(src)/system.cpp',
			'<(src)/tables.cpp'
		],

		'include_dirs': [
			'<(root)/include',
			'<(module_root)/include',
			'<(gen)/include'
		],

		'direct_dependent_settings': {
			'include_dirs': [
				'<(gen)/include'
			]
		},

		'defines': [
			'__OPENCV_BUILD=1'
		],

		'cflags': [
			'-pthread'
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
			'<(module_root)/include',
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
			'libjpeg',
			'libpng',
			'zlib'
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
				'<(module_root)/include'
			],
		},

		'defines': [
			'__OPENCV_BUILD=1'
		]
	}]
}