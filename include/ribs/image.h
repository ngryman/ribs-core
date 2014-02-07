/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#ifndef __RIBS_IMAGE_H__
#define __RIBS_IMAGE_H__

#include "common.h"

namespace ribs {

class Image {
public:
	inline uchar* pixels() const { return mat.data; }
	inline int    width()  const { return mat.cols; }
	inline int    height() const { return mat.rows; }
	inline size_t length() const { return mat.total(); }

	Image(std::vector<uchar>& buffer);
	Image(const std::string& filename);
	virtual ~Image() {}

	Image& resize(int width, int height, int x, int y);
	Image& crop(int width, int height, int x, int y);
	Image& artDirection(int width, int height, int bw, int bh, int bx, int by);

	void save(const std::string& filename) const;

private:
	cv::Mat mat;
};

}

#endif