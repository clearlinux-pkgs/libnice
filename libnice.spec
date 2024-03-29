#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: 1ab68ca
#
# Source0 file verified with key 0x1D388E5A4ED9A2BB (tester@tester.ca)
#
Name     : libnice
Version  : 0.1.22
Release  : 12
URL      : https://libnice.freedesktop.org/releases/libnice-0.1.22.tar.gz
Source0  : https://libnice.freedesktop.org/releases/libnice-0.1.22.tar.gz
Source1  : https://libnice.freedesktop.org/releases/libnice-0.1.22.tar.gz.asc
Summary  : ICE library
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
Requires: libnice-bin = %{version}-%{release}
Requires: libnice-data = %{version}-%{release}
Requires: libnice-lib = %{version}-%{release}
Requires: libnice-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection
BuildRequires : openssl-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Nice: GLib ICE library
======================
---------
(C) 2006-2020 Collabora Ltd.
(C) 2006-2011 Nokia Corporation

%package bin
Summary: bin components for the libnice package.
Group: Binaries
Requires: libnice-data = %{version}-%{release}
Requires: libnice-license = %{version}-%{release}

%description bin
bin components for the libnice package.


%package data
Summary: data components for the libnice package.
Group: Data

%description data
data components for the libnice package.


%package dev
Summary: dev components for the libnice package.
Group: Development
Requires: libnice-lib = %{version}-%{release}
Requires: libnice-bin = %{version}-%{release}
Requires: libnice-data = %{version}-%{release}
Provides: libnice-devel = %{version}-%{release}
Requires: libnice = %{version}-%{release}

%description dev
dev components for the libnice package.


%package lib
Summary: lib components for the libnice package.
Group: Libraries
Requires: libnice-data = %{version}-%{release}
Requires: libnice-license = %{version}-%{release}

%description lib
lib components for the libnice package.


%package license
Summary: license components for the libnice package.
Group: Default

%description license
license components for the libnice package.


%prep
%setup -q -n libnice-0.1.22
cd %{_builddir}/libnice-0.1.22
pushd ..
cp -a libnice-0.1.22 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709741867
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libnice
cp %{_builddir}/libnice-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libnice/f28fffc35dc811f921fd3f6e4bb72e1904254e12 || :
cp %{_builddir}/libnice-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libnice/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/libnice-%{version}/COPYING.MPL %{buildroot}/usr/share/package-licenses/libnice/8c4580d7288e21a3006db26c0fe556d00545768a || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/stunbdc
/V3/usr/bin/stund
/usr/bin/stunbdc
/usr/bin/stund

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Nice-0.1.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/nice/address.h
/usr/include/nice/agent.h
/usr/include/nice/candidate.h
/usr/include/nice/debug.h
/usr/include/nice/interfaces.h
/usr/include/nice/nice-version.h
/usr/include/nice/nice.h
/usr/include/nice/pseudotcp.h
/usr/include/stun/constants.h
/usr/include/stun/debug.h
/usr/include/stun/stunagent.h
/usr/include/stun/stunmessage.h
/usr/include/stun/usages/bind.h
/usr/include/stun/usages/ice.h
/usr/include/stun/usages/timer.h
/usr/include/stun/usages/turn.h
/usr/include/stun/win32_common.h
/usr/lib64/libnice.so
/usr/lib64/pkgconfig/nice.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gstreamer-1.0/libgstnice.so
/V3/usr/lib64/libnice.so.10.14.0
/usr/lib64/gstreamer-1.0/libgstnice.so
/usr/lib64/libnice.so.10
/usr/lib64/libnice.so.10.14.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnice/8c4580d7288e21a3006db26c0fe556d00545768a
/usr/share/package-licenses/libnice/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/libnice/f28fffc35dc811f921fd3f6e4bb72e1904254e12
