/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#ifndef __RIBS_COMMON_H__
#define __RIBS_COMMON_H__

#include <functional>
#include <memory>
#include <string>
#include <vector>

#include "config.h"

#include <opencv/cv.h>

namespace ribs {

enum Origin {
	Center,
	TopLeft,
	Top,
	TopRight,
	Right,
	RightBottom,
	Bottom,
	LeftBottom,
	Left
};

class Error;
class Image;

}

#endif