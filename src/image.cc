/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#include "ribs/image.h"
#include "ribs/error.h"
#include <opencv/highgui.h>

using namespace ribs;
using namespace std;
using namespace cv;

Image::Image(vector<uchar>& buffer) {
	mat = imdecode(buffer, CV_LOAD_IMAGE_COLOR);
}

Image::Image(const string& filename) {
	if (filename.empty()) {
		throw Error(ErrorType::InvalidArgument, "filename");
	}

	mat = imread(filename.c_str(), CV_LOAD_IMAGE_COLOR);
	if (!mat.data) {
		throw Error(ErrorType::FileRead, filename);
	}
}

Image& Image::resize(int width, int height, int x, int y) {
	throw Error::NotImplemented;
	return *this;
}

Image& Image::crop(int width, int height, int x, int y) {
	throw Error::NotImplemented;
	return *this;
}

Image& Image::artDirection(int width, int height, int bw, int bh, int bx, int by) {
	throw Error::NotImplemented;
	return *this;
}