#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1D388E5A4ED9A2BB (tester@tester.ca)
#
Name     : libnice
Version  : 0.1.16
Release  : 9
URL      : https://nice.freedesktop.org/releases/libnice-0.1.16.tar.gz
Source0  : https://nice.freedesktop.org/releases/libnice-0.1.16.tar.gz
Source1  : https://nice.freedesktop.org/releases/libnice-0.1.16.tar.gz.asc
Summary  : ICE library
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
Requires: libnice-bin = %{version}-%{release}
Requires: libnice-data = %{version}-%{release}
Requires: libnice-lib = %{version}-%{release}
Requires: libnice-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gnutls-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)

%description
Nice: GLib ICE library
======================
---------
(C) 2006-2018 Collabora Ltd.
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


%package doc
Summary: doc components for the libnice package.
Group: Documentation

%description doc
doc components for the libnice package.


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
%setup -q -n libnice-0.1.16
cd %{_builddir}/libnice-0.1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604616245
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-gstreamer --without-gstreamer-0.10
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604616245
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnice
cp %{_builddir}/libnice-0.1.16/COPYING %{buildroot}/usr/share/package-licenses/libnice/f28fffc35dc811f921fd3f6e4bb72e1904254e12
cp %{_builddir}/libnice-0.1.16/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libnice/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/libnice-0.1.16/COPYING.MPL %{buildroot}/usr/share/package-licenses/libnice/8c4580d7288e21a3006db26c0fe556d00545768a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libnice/NiceAgent.html
/usr/share/gtk-doc/html/libnice/NiceCandidate.html
/usr/share/gtk-doc/html/libnice/annotation-glossary.html
/usr/share/gtk-doc/html/libnice/api-index-deprecated.html
/usr/share/gtk-doc/html/libnice/api-index-full.html
/usr/share/gtk-doc/html/libnice/ch01.html
/usr/share/gtk-doc/html/libnice/ch02.html
/usr/share/gtk-doc/html/libnice/ch03.html
/usr/share/gtk-doc/html/libnice/ch04.html
/usr/share/gtk-doc/html/libnice/ch05.html
/usr/share/gtk-doc/html/libnice/home.png
/usr/share/gtk-doc/html/libnice/index.html
/usr/share/gtk-doc/html/libnice/left-insensitive.png
/usr/share/gtk-doc/html/libnice/left.png
/usr/share/gtk-doc/html/libnice/libnice-Bind.html
/usr/share/gtk-doc/html/libnice/libnice-Debug-messages.html
/usr/share/gtk-doc/html/libnice/libnice-ICE.html
/usr/share/gtk-doc/html/libnice/libnice-Network-interfaces-discovery.html
/usr/share/gtk-doc/html/libnice/libnice-NiceAddress.html
/usr/share/gtk-doc/html/libnice/libnice-Pseudo-TCP-Socket.html
/usr/share/gtk-doc/html/libnice/libnice-STUN-Constants.html
/usr/share/gtk-doc/html/libnice/libnice-StunAgent.html
/usr/share/gtk-doc/html/libnice/libnice-StunMessage.html
/usr/share/gtk-doc/html/libnice/libnice-TURN.html
/usr/share/gtk-doc/html/libnice/libnice-Timer.html
/usr/share/gtk-doc/html/libnice/libnice.devhelp2
/usr/share/gtk-doc/html/libnice/pt01.html
/usr/share/gtk-doc/html/libnice/pt02.html
/usr/share/gtk-doc/html/libnice/pt03.html
/usr/share/gtk-doc/html/libnice/pt04.html
/usr/share/gtk-doc/html/libnice/right-insensitive.png
/usr/share/gtk-doc/html/libnice/right.png
/usr/share/gtk-doc/html/libnice/states.png
/usr/share/gtk-doc/html/libnice/style.css
/usr/share/gtk-doc/html/libnice/up-insensitive.png
/usr/share/gtk-doc/html/libnice/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstnice.so
/usr/lib64/libnice.so.10
/usr/lib64/libnice.so.10.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnice/8c4580d7288e21a3006db26c0fe556d00545768a
/usr/share/package-licenses/libnice/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/libnice/f28fffc35dc811f921fd3f6e4bb72e1904254e12
