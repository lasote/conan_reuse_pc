AC_PREREQ([2.69])
AC_INIT([zlib_autoconftest], [1.0.0], [kent.rosenkoetter@multiscalehn.com])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_CONFIG_MACRO_DIRS([m4])
AC_CONFIG_FILES([Makefile src/Makefile])

# Checks for programs.
AC_PROG_CC
AC_PROG_CC_STDC
AC_PROG_CXX

# Checks for libraries.
PKG_CHECK_MODULES([ZLIB], [zlib = 1.2.11])
PKG_CHECK_MODULES([PNG], [libpng = 1.6.23])

# Checks for library functions.
AC_OUTPUT
