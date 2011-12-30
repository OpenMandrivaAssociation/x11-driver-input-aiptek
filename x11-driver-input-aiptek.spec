Name: x11-driver-input-aiptek
Epoch: 1
Version: 1.4.1
Release: 1
Summary: X.org input driver for Aiptek HyperPen USB-based tablet devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-aiptek-%{version}.tar.bz2
License: MIT

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.3.0
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Aiptek is an Xorg input driver for Aiptek HyperPen USB-based tablet devices.
This driver only supports the USB protocol.
The RS-232C-based HyperPens are managed by the "hyperpen" driver.

%prep
%setup -qn xf86-input-aiptek-%{version}

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/input/aiptek_drv.so
%{_mandir}/man4/aiptek.*

