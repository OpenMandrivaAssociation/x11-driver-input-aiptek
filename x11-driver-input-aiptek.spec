# There is no version 1.1.0 tarball
Epoch: 1

Name: x11-driver-input-aiptek
Version: 1.1.1
Release: %mkrel 2
Summary: X.org input driver for Aiptek HyperPen USB-based tablet devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-aiptek-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
Aiptek is an Xorg input driver for Aiptek HyperPen USB-based tablet devices.
This driver only supports the USB protocol.
The RS-232C-based HyperPens are managed by the "hyperpen" driver.

%prep
%setup -q -n xf86-input-aiptek-%{version}

%build
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
