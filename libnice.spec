#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1D388E5A4ED9A2BB (tester@tester.ca)
#
Name     : libnice
Version  : 0.1.14
Release  : 3
URL      : https://nice.freedesktop.org/releases/libnice-0.1.14.tar.gz
Source0  : https://nice.freedesktop.org/releases/libnice-0.1.14.tar.gz
Source99 : https://nice.freedesktop.org/releases/libnice-0.1.14.tar.gz.asc
Summary  : ICE library
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
Requires: libnice-bin
Requires: libnice-lib
Requires: libnice-doc
Requires: libnice-data
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)

%description
Nice: GLib ICE library
======================
---------
(C) 2006-2017 Collabora Ltd.
(C) 2006-2011 Nokia Corporation

%package bin
Summary: bin components for the libnice package.
Group: Binaries
Requires: libnice-data

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
Requires: libnice-lib
Requires: libnice-bin
Requires: libnice-data
Provides: libnice-devel

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
Requires: libnice-data

%description lib
lib components for the libnice package.


%prep
%setup -q -n libnice-0.1.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511971516
%configure --disable-static --with-gstreamer --without-gstreamer-0.10
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1511971516
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sdp-example
/usr/bin/simple-example
/usr/bin/stunbdc
/usr/bin/stund
/usr/bin/threaded-example

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
%defattr(-,root,root,-)
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
/usr/share/gtk-doc/html/libnice/ix03.html
/usr/share/gtk-doc/html/libnice/ix04.html
/usr/share/gtk-doc/html/libnice/ix05.html
/usr/share/gtk-doc/html/libnice/ix06.html
/usr/share/gtk-doc/html/libnice/ix07.html
/usr/share/gtk-doc/html/libnice/ix08.html
/usr/share/gtk-doc/html/libnice/ix09.html
/usr/share/gtk-doc/html/libnice/ix10.html
/usr/share/gtk-doc/html/libnice/ix11.html
/usr/share/gtk-doc/html/libnice/ix12.html
/usr/share/gtk-doc/html/libnice/ix13.html
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
/usr/lib64/libnice.so.10.7.0
