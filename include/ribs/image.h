/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#ifndef __RIBS_IMAGE_H__
#define __RIBS_IMAGE_H__

#include "common.h"

namespace ribs {

using ImageCallback = std::function<void(const Error&, Image*)>;

class Image {
public:
	inline cv::Mat  Pixels() const { return p; }
	inline uint32_t Width()  const { return w; }
	inline uint32_t Height() const { return h; }
	inline uint32_t Length() const { return Stride() * h; }
	inline uint32_t Stride() const { return w * 4; }

	void Resize(uint32_t width, uint32_t height, ImageCallback callback);
	void Resize(uint32_t width, uint32_t height, Origin origin, ImageCallback callback);
	void Resize(uint32_t width, uint32_t height, uint32_t x, uint32_t y, ImageCallback callback);

	void Crop(uint32_t width, uint32_t height, ImageCallback callback);
	void Crop(uint32_t width, uint32_t height, Origin origin, ImageCallback callback);
	void Crop(uint32_t width, uint32_t height, uint32_t x, uint32_t y, ImageCallback callback);

	void AutoArt(uint32_t width, uint32_t height, uint32_t bw, uint32_t bh, ImageCallback callback);
	void AutoArt(uint32_t width, uint32_t height, uint32_t bw, uint32_t bh, Origin origin, ImageCallback callback);
	void AutoArt(uint32_t width, uint32_t height, uint32_t bw, uint32_t bh, uint32_t bx, uint32_t by, ImageCallback callback);

	void Save(const std::string& filename, ImageCallback callback) const;

	static void Open(const std::string& filename, ImageCallback callback);

private:
	Image(const cv::Mat& pixels);
	virtual ~Image();

	cv::Mat  p;
	uint32_t w;
	uint32_t h;
};

}

#endif