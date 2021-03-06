/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#ifndef __RIBS_ERROR_H__
#define __RIBS_ERROR_H__

#include "common.h"

namespace ribs {

enum class ErrorType {
	Success,

	InvalidArgument,
	NoMemory,
	FileRead,
	FileWrite,
	InvalidFormat,
	NotImplemented
};

class Error {
public:
	Error(ErrorType type);
	Error(ErrorType type, const std::string& info);

    ErrorType         type()    const { return t; }
	const std::string message() const { return m; }

	static const Error Success;
	static const Error NoMemory;
	static const Error InvalidFormat;
	static const Error NotImplemented;

private:
	ErrorType   t;
	std::string m;
};

}

#endif