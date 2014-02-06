#!/usr/bin/env python

#
# dependencies
#

import fnmatch
import optparse
import os
import subprocess
import shutil
import sys

#
# constants
#

root_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

#
# options handling
#

parser = optparse.OptionParser()

parser.add_option('--library',
	action='store_true',
	dest='library',
	help='build a static or shared library. Valid value are: '
		'static, shared. (default: static_library)')

parser.add_option('--target-cpu',
	action='store',
	dest='target_cpu',
	help='CPU archivecture to build for. Valid values are: arm, ia32, x64')

parser.add_option('--target-os',
	action='store',
	dest='target_os',
	help='operating system to build for. Valid values are:'
		'win, mac, solaris, freebsd, openbsd, linux, android')

(options, args) = parser.parse_args()

#
# configure: gather options and call gyp accordingly.
#

def configure():
	# assemble gyp arguments
	gyp_args = ['gyp', '--depth=' + root_dir]
	gyp_args.append('-Dlibrary={0}_library'.format(options.library or 'static'))
	gyp_args.append('-Dtarget_arch={0}'.format(options.target_cpu or 'ia32'))

	# invoke gyp
	subprocess.call(gyp_args)

#
# build: depending of os, calls the correct command to compile.
#

def build():
	# invoke make
	subprocess.call(['make'])

#
# clean: removes all compiled files.
#

def clean():
	shutil.rmtree(os.path.join(root_dir, 'out'))

#
# distclean: removes all compiled and gyp generated files.
#

def distclean():
	clean()
	for filename in find_files('*.mk'):
		os.remove(filename)
	for filename in find_files('*.Makefile'):
		os.remove(filename)

#
# rebuild: clean and build.
#

def rebuild():
	clean()
	build()

#
# misc.
#

def find_files(pattern):
	for root, dirs, files in os.walk(root_dir):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename

#
# entry point
#

# call the given opeartion
if args[0] in globals():
	globals()[args[0]]()
else:
	parser.print_help()
