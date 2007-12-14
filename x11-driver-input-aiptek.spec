Name: x11-driver-input-aiptek
Version: 1.1.0
Release: %mkrel 5
Summary: X.org input driver for Aiptek HyperPen USB-based tablet devices
Group: Development/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-aiptek  xorg/drivers/xf86-input-aiptek
# cd xorg/drivers/xf86-input-aiptek
# git-archive --format=tar --prefix=xf86-input-aiptek-1.1.0/ master | bzip2 -9 > xf86-input-aiptek-1.1.0.tar.bz2
########################################################################
Source0: xf86-input-aiptek-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
Iptek is an Xorg input driver for Aiptek HyperPen USB-based tablet devices.
This driver only supports the USB protocol.
The RS-232C-based HyperPens are managed by the "hyperpen" driver.
THIS DRIVER IS BROKEN:
Missing symbol xf86IsCorePointer no longer present due to X Input Hotplug
rework. (Also links with libm; not really a problem).

%prep
%setup -q -n xf86-input-aiptek-%{version}

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/aiptek_drv.la
%{_libdir}/xorg/modules/input/aiptek_drv.so
%{_mandir}/man4/aiptek.*
