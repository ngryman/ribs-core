/*!
 * ribs
 * Copyright (c) 2014 Nicolas Gryman <ngryman@gmail.com>
 * LGPL Licensed
 */

#include "ribs/error.h"

using namespace std;
using namespace ribs;

static const string ERROR_MESSAGES[] = {
    "Success",
    "Invalid argument",
    "Out of memory",
    "Can't read file",
    "Can't write file",
    "Invalid image format",
    "Not implemented"
};

const Error Error::Success(ErrorType::Success);
const Error Error::NoMemory(ErrorType::NoMemory);
const Error Error::InvalidFormat(ErrorType::InvalidFormat);
const Error Error::NotImplemented(ErrorType::NotImplemented);

Error::Error(ErrorType type) {
	m = ERROR_MESSAGES[static_cast<int>(type)];
}

Error::Error(ErrorType type, const string& info) {
	m = ERROR_MESSAGES[static_cast<int>(type)] + ": " + info;
}