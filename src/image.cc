/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#include "image.h"
#include "io.h"
#include "operation.h"
#include "math.h"

using namespace std;
using namespace cv;
using namespace ribs;

Image::Image(const Mat& pixels) :
    p(pixels),
	w(0),
	h(0) {
}

Image::~Image() {
//	if (p) delete[] p;
}

void Image::Open(const string& filename, ImageCallback callback) {
	if (!callback) return;

	if (filename.empty()) {
		callback(Error(ErrorType::InvalidArgument), NULL);

	}

	IO::Read(filename, [callback](const Error& error, Mat* pixels) {
	    if (ErrorType::Success == error.type()) {
	        callback(error, new Image(*pixels));
	    }
	    else {
	        callback(error, NULL);
	    }
	});
}

void Image::Resize(uint32_t width, uint32_t height, ImageCallback callback) {
	Resize(width, height, Origin::Center, callback);
}

void Image::Resize(uint32_t width, uint32_t height, Origin origin, ImageCallback callback) {
	uint32_t x, y;
	Math::coordinates(origin, w, h, &x, &y);

	Resize(width, height, x, y, callback);
}

void Image::Resize(uint32_t width, uint32_t height, uint32_t x, uint32_t y, ImageCallback callback) {
	Operation::Resize(this, width, height, x, y, callback);
}

void Image::Crop(uint32_t width, uint32_t height, ImageCallback callback) {
	Crop(width, height, Origin::Center, callback);
}

void Image::Crop(uint32_t width, uint32_t height, Origin origin, ImageCallback callback) {
	uint32_t x, y;
	Math::coordinates(origin, w, h, &x, &y);

	Crop(width, height, x, y, callback);
}

void Image::Crop(uint32_t width, uint32_t height, uint32_t x, uint32_t y, ImageCallback callback) {
	Operation::Crop(this, width, height, x, y, callback);
}