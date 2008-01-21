%define debug_package	%{nil}

Name: x11-driver-input-aiptek
Version: 1.1.0
Release: %mkrel 5
Summary: X.org input driver for Aiptek HyperPen USB-based tablet devices
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-input-aiptek-1.1.0@mandriva suggested on upstream
# Tag at git checkout afedccae164668128c6228542585cc27d241b7e6
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-aiptek  xorg/drivers/xf86-input-aiptek
# cd xorg/drivers/xf86-input-aiptek
# git-archive --format=tar --prefix=xf86-input-aiptek-1.1.0/ xf86-input-aiptek-1.1.0@mandriva | bzip2 -9 > xf86-input-aiptek-1.1.0.tar.bz2
########################################################################
Source0: xf86-input-aiptek-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-aiptek-1.1.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Patch-with-a-load-of-fixes-backported-from-aiptekta.patch
Patch3: 0003-Driver-s-don-t-have-to-worry-about-being-core-pointe.patch
Patch4: 0004-miPointerCurrentScreen-is-deprecated-miPointerGetSc.patch
Patch5: 0005-Remove-redefinition-of-NEED_XF86_TYPES.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
Aiptek is an Xorg input driver for Aiptek HyperPen USB-based tablet devices.
This driver only supports the USB protocol.
The RS-232C-based HyperPens are managed by the "hyperpen" driver.

%prep
%setup -q -n xf86-input-aiptek-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/aiptek_drv.so
%{_mandir}/man4/aiptek.*
