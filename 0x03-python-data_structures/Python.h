/* Python.h -- global declarations for the Python interpreter. */

#ifndef Py_PYTHON_H
#define Py_PYTHON_H
#ifdef __cplusplus
extern "C" {
#endif

/* Include the generated pyconfig.h */
#include <pyconfig.h>

/* Define to 1 if you want to include deprecated interfaces in the core */
#ifndef Py_LIMITED_API
#define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
#else
#define Py_DEPRECATED(VERSION_UNUSED)
#endif

/* Define to 1 if you want to include limited API interfaces in the core */
#ifdef Py_LIMITED_API
#define Py_LIMITED_API 0
#endif

/* Define Py_LIMITED_API_VERSION to the highest version of Python you want to
 * support with the limited API. For example, to support Python 3.6 and above,
 * you would set this to 0x03060000. */
#ifndef Py_LIMITED_API_VERSION
#define Py_LIMITED_API_VERSION 0x03090000
#endif

/* Define Py_NO_ENABLE_SHARED to disable the use of shared libraries entirely.
 * This is useful in environments where the dynamic linker is broken, or where
 * the use of shared libraries is simply not desired. */
#ifndef Py_NO_ENABLE_SHARED
#define Py_NO_ENABLE_SHARED 0
#endif

/* Define Py_ENABLE_SHARED to enable the use of shared libraries. */
#ifndef Py_ENABLE_SHARED
#define Py_ENABLE_SHARED 1
#endif

/* Define Py_NO_PYTHON_FILESYSTEM to disable the use of the Python filesystem
 * encoding and error handler. This is useful in environments where the
 * filesystem encoding is not properly set up, or where the use of the Python
 * filesystem encoding is simply not desired. */
#ifndef Py_NO_PYTHON_FILESYSTEM
#define Py_NO_PYTHON_FILESYSTEM 0
#endif

/* Define Py_ENABLE_PYTHON_FILESYSTEM to enable the use of the Python filesystem
 * encoding and error handler. */
#ifndef Py_ENABLE_PYTHON_FILESYSTEM
#define Py_ENABLE_PYTHON_FILESYSTEM 1
#endif

/* Define Py_NO_SHORT_FLOAT_REPR to disable the use of short float repr. */
#ifndef Py_NO_SHORT_FLOAT_REPR
#define Py_NO_SHORT_FLOAT_REPR 0
#endif

/* Define Py_ENABLE_SHORT_FLOAT_REPR to enable the use of short float repr. */
#ifndef Py_ENABLE_SHORT_FLOAT_REPR
#define Py_ENABLE_SHORT_FLOAT_REPR 1
#endif

/* Define Py_NO_UNICODE_COMPRESSION to disable the use of Unicode compression. */
#ifndef Py_NO_UNICODE_COMPRESSION
#define Py_NO_UNICODE_COMPRESSION 0
#endif

/* Define Py_ENABLE_UNICODE_COMPRESSION to enable the use of Unicode compression. */
#ifndef Py_ENABLE_UNICODE_COMPRESSION
#define Py_ENABLE_UNICODE_COMPRESSION 1
#endif

/* Define Py_NO_ENABLE_SHARED_MODULE to disable the use of shared modules. */
#ifndef Py_NO_ENABLE_SHARED_MODULE
#define Py_NO_ENABLE_SHARED_MODULE 0
#endif

/* Define Py_ENABLE_SHARED_MODULE to enable the use of shared modules. */
#ifndef Py_ENABLE_SHARED_MODULE
#define Py_ENABLE_SHARED_MODULE 1
#endif

/* Define Py_NO_DEPRECATION_WARNINGS to disable DeprecationWarning. */
#ifndef Py_NO_DEPRECATION_WARNINGS
#define Py_NO_DEPRECATION_WARNINGS 0
#endif

/* Define Py_ENABLE_DEPRECATION_WARNINGS to enable DeprecationWarning. */
#ifndef Py_ENABLE_DEPRECATION_WARNINGS
#define Py_ENABLE_DEPRECATION_WARNINGS 1
#endif

/* Define Py_NO_PYTHON_WARNINGS to disable Python warnings. */
#ifndef Py_NO_PYTHON_WARNINGS
#define Py_NO_PYTHON_WARNINGS 0
#endif

/* Define Py_ENABLE_PYTHON_WARNINGS to enable Python warnings. */
#ifndef Py_ENABLE_PYTHON_WARNINGS
#define Py_ENABLE_PYTHON_WARNINGS 1
#endif

/* Define Py_NO_SHORT_ENUMS to disable short enums. */
#ifndef Py_NO_SHORT_ENUMS
#define Py_NO_SHORT_ENUMS 0
#endif

/* Define Py_ENABLE_SHORT_ENUMS to enable short enums. */
#ifndef Py_ENABLE_SHORT_ENUMS
#define Py_ENABLE_SHORT_ENUMS 1
#endif

/* Define Py_NO_LONG_LONG to disable long long. */
#ifndef Py_NO_LONG_LONG
#define Py_NO_LONG_LONG 0
#endif

/* Define Py_ENABLE_LONG_LONG to enable long long. */
#ifndef Py_ENABLE_LONG_LONG
#define Py_ENABLE_LONG_LONG 1
#endif

/* Define Py_NO_FORMAT_LONG_LONG to disable the 'll' format character. */
#ifndef Py_NO_FORMAT_LONG_LONG
#define Py_NO_FORMAT_LONG_LONG 0
#endif

/* Define Py_ENABLE_FORMAT_LONG_LONG to enable the 'll' format character. */
#ifndef Py_ENABLE_FORMAT_LONG_LONG
#define Py_ENABLE_FORMAT_LONG_LONG 1
#endif

/* Define Py_NO_FORMAT_OFF_T to disable the 'z' format character. */
#ifndef Py_NO_FORMAT_OFF_T
#define Py_NO_FORMAT_OFF_T 0
#endif

/* Define Py_ENABLE_FORMAT_OFF_T to enable the 'z' format character. */
#ifndef Py_ENABLE_FORMAT_OFF_T
#define Py_ENABLE_FORMAT_OFF_T 1
#endif

/* Define Py_NO_FORMAT_SIZE_T to disable the 'n' format character. */
#ifndef Py_NO_FORMAT_SIZE_T
#define Py_NO_FORMAT_SIZE_T 0
#endif

/* Define Py_ENABLE_FORMAT_SIZE_T to enable the 'n' format character. */
#ifndef Py_ENABLE_FORMAT_SIZE_T
#define Py_ENABLE_FORMAT_SIZE_T 1
#endif

/* Define Py_NO_FORMAT_PY_SIZE_T to disable the 'n' format character for Py_ssize_t. */
#ifndef Py_NO_FORMAT_PY_SIZE_T
#define Py_NO_FORMAT_PY_SIZE_T 0
#endif

/* Define Py_ENABLE_FORMAT_PY_SIZE_T to enable the 'n' format character for Py_ssize_t. */
#ifndef Py_ENABLE_FORMAT_PY_SIZE_T
#define Py_ENABLE_FORMAT_PY_SIZE_T 1
#endif

/* Define Py_NO_FORMAT_UINT64 to disable the 'I64' format character. */
#ifndef Py_NO_FORMAT_UINT64
#define Py_NO_FORMAT_UINT64 0
#endif

/* Define Py_ENABLE_FORMAT_UINT64 to enable the 'I64' format character. */
#ifndef Py_ENABLE_FORMAT_UINT64
#define Py_ENABLE_FORMAT_UINT64 1
#endif

/* Define Py_NO_FORMAT_OFF64 to disable the 'I' format character. */
#ifndef Py_NO_FORMAT_OFF64
#define Py_NO_FORMAT_OFF64 0
#endif

/* Define Py_ENABLE_FORMAT_OFF64 to enable the 'I' format character. */
#ifndef Py_ENABLE_FORMAT_OFF64
#define Py_ENABLE_FORMAT_OFF64 1
#endif

/* Define Py_NO_FORMAT_SPEC_WIDTHS to disable the '{' and '}' format characters. */
#ifndef Py_NO_FORMAT_SPEC_WIDTHS
#define Py_NO_FORMAT_SPEC_WIDTHS 0
#endif

/* Define Py_ENABLE_FORMAT_SPEC_WIDTHS to enable the '{' and '}' format characters. */
#ifndef Py_ENABLE_FORMAT_SPEC_WIDTHS
#define Py_ENABLE_FORMAT_SPEC_WIDTHS 1
#endif

/* Define Py_NO_FORMAT_UNICODE to disable the 'u' format character. */
#ifndef Py_NO_FORMAT_UNICODE
#define Py_NO_FORMAT_UNICODE 0
#endif

/* Define Py_ENABLE_FORMAT_UNICODE to enable the 'u' format character. */
#ifndef Py_ENABLE_FORMAT_UNICODE
#define Py_ENABLE_FORMAT_UNICODE 1
#endif

/* Define Py_NO_FORMAT_PY_UNICODE to disable the 'u' format character for Py_UNICODE. */
#ifndef Py_NO_FORMAT_PY_UNICODE
#define Py_NO_FORMAT_PY_UNICODE 0
