/* bool.c - Jon McCormack, April 2004  */

/*
 * add boolean type to C
 */

#ifndef _BOOL_H_
#define _BOOL_H_

#if defined(true) | defined(false)
#error Boolean types seem to have been defined somewhere else
#else

typedef unsigned short bool;
#define FALSE		0
#define TRUE		1

#endif

#endif
