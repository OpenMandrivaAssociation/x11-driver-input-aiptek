Name: x11-driver-input-aiptek
Epoch: 1
Version: 1.4.1
Release: 3
Summary: X.org input driver for Aiptek HyperPen USB-based tablet devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-aiptek-%{version}.tar.bz2
License: MIT

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
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
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/aiptek_drv.so
%{_mandir}/man4/aiptek.*



%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:1.4.1-2
+ Revision: 787169
- Rebuild for x11-server 1.12

* Fri Dec 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:1.4.1-1
+ Revision: 748288
- new version 1.4.1
- cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.4.0-2
+ Revision: 703622
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:1.4.0-1
+ Revision: 683596
- New version 1.4.0.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.1-4
+ Revision: 671120
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1:1.3.1-3mdv2011.0
+ Revision: 595751
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1:1.3.1-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Wed Aug 18 2010 Thierry Vignaud <tv@mandriva.org> 1:1.3.1-1mdv2011.0
+ Revision: 571251
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:1.3.0-1mdv2010.1
+ Revision: 464246
- New version: 1.3.0

* Fri Feb 27 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:1.2.0-1mdv2009.1
+ Revision: 345693
- Fix build with newer libtool

  + Thierry Vignaud <tv@mandriva.org>
    - new release
    - fix group

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1:1.1.1-2mdv2009.0
+ Revision: 265779
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Thierry Vignaud <tv@mandriva.org> 1:1.1.1-1mdv2009.0
+ Revision: 212574
- new release (remove GIT patches)

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:1.0.1-7mdv2008.1
+ Revision: 160473
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-6mdv2008.1
+ Revision: 156567
- re-enable rpm debug packages support

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 155784
- Updated BuildRequires and resubmit package.
- Remove build of debug package.
  Update BuildRequires.
  Pull upstream fixes to packages so that package is expected to work
  correctly now (no hardware to test).
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
  Upstream tarball is at 1.0.1 but diff from tag aiptek-1_0_1 to
  xf86-input-aiptek-1.1.0@mandriva shows only minimal "cosmetic" changes, i.e.
  version bump, adition of .gitignore file and use of macros instead of
  static values to specify version in source files.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Build fix, as previous commit did not properly reflect the changes when
  appling/listing patches.
- This implements one possible alternative I suggest @cooker to still use
  git-archive for repositories that don't have a version tag or stable branch.
  In this case, at commit afedccae164668128c6228542585cc27d241b7e6, that
  is just after some .gitignore/.cvsignore changes after the version bump
  and update of configure.ac, the tag xf86-input-aiptek-1.1.0@mandriva
  was added. There is no common pattern in tag names, but since some of them
  use the format "<repository-name>-version", I will try to use this format
  and choose a sensible commit to generate a mandriva tag, that is suggested
  to also exist upstream (without the '@mandriva' substring).
- Missing URL removed in previous commit.
- Update to generate tarball from tag aiptek-1_0_1. Please note that there is
  no 1.1.0 tag, and the upstream diff from 1.1.0 to 1_0_1 is just the version
  in configure.ac.
  The new patches are harmless and basically cosmetic changes, but upgrade
  to local branch mandriva+gpl.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.1-4mdv2008.1
+ Revision: 98624
- minor spec cleanup
- build against xserver 1.4

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2008.0
+ Revision: 75597
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:03:02 (31708)
- fill in summary & descriptions for all input drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

