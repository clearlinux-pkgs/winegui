#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : winegui
Version  : 2.8.1
Release  : 8
URL      : https://winegui.melroy.org/downloads/WineGUI-Source-v2.8.1.tar.gz
Source0  : https://winegui.melroy.org/downloads/WineGUI-Source-v2.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0
Requires: winegui-bin = %{version}-%{release}
Requires: winegui-data = %{version}-%{release}
Requires: winegui-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gtkmm-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# WineGUI
At last, a user-interface friendly [Wine](https://www.winehq.org/) (A compatibility layer capable of running Windows applications under Linux) Manager.

%package bin
Summary: bin components for the winegui package.
Group: Binaries
Requires: winegui-data = %{version}-%{release}
Requires: winegui-license = %{version}-%{release}

%description bin
bin components for the winegui package.


%package data
Summary: data components for the winegui package.
Group: Data

%description data
data components for the winegui package.


%package license
Summary: license components for the winegui package.
Group: Default

%description license
license components for the winegui package.


%prep
%setup -q -c -n WineGUI-Source-v2.8.1.tar
cd %{_builddir}/WineGUI-Source-v2.8.1.tar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1741963885
mkdir -p clr-build
pushd clr-build
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

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
export SOURCE_DATE_EPOCH=1741963885
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/winegui
cp %{_builddir}/WineGUI-Source-v%{version}.tar/LICENSE %{buildroot}/usr/share/package-licenses/winegui/f75ccad99ecd76c1f0858cbc59e64f430ffff079 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/winegui

%files data
%defattr(-,root,root,-)
/usr/share/applications/winegui.desktop
/usr/share/glib-2.0/schemas/org.melroy.winegui.gschema.xml
/usr/share/icons/hicolor/48x48/apps/winegui.png
/usr/share/icons/hicolor/scalable/apps/winegui.svg
/usr/share/winegui/images/apps/command_prompt.png
/usr/share/winegui/images/apps/default_app_file.png
/usr/share/winegui/images/apps/excel_document.png
/usr/share/winegui/images/apps/file_explorer.png
/usr/share/winegui/images/apps/help_file.png
/usr/share/winegui/images/apps/html_document.png
/usr/share/winegui/images/apps/image_file.png
/usr/share/winegui/images/apps/installer_file.png
/usr/share/winegui/images/apps/internet_explorer.png
/usr/share/winegui/images/apps/link_file.png
/usr/share/winegui/images/apps/minesweeper.png
/usr/share/winegui/images/apps/multimedia_file.png
/usr/share/winegui/images/apps/notepad.png
/usr/share/winegui/images/apps/oleview.png
/usr/share/winegui/images/apps/other_file.png
/usr/share/winegui/images/apps/pdf_file.png
/usr/share/winegui/images/apps/powerpoint_document.png
/usr/share/winegui/images/apps/regedit.png
/usr/share/winegui/images/apps/task_manager.png
/usr/share/winegui/images/apps/text_file.png
/usr/share/winegui/images/apps/uninstaller.png
/usr/share/winegui/images/apps/unknown_file.png
/usr/share/winegui/images/apps/url.png
/usr/share/winegui/images/apps/wine.png
/usr/share/winegui/images/apps/winecfg.png
/usr/share/winegui/images/apps/winecontrol.png
/usr/share/winegui/images/apps/winefile.png
/usr/share/winegui/images/apps/winetricks.png
/usr/share/winegui/images/apps/word_document.png
/usr/share/winegui/images/apps/wordpad.png
/usr/share/winegui/images/logo.png
/usr/share/winegui/images/logo_big.png
/usr/share/winegui/images/not_ready.png
/usr/share/winegui/images/not_ready_org.png
/usr/share/winegui/images/ready.png
/usr/share/winegui/images/ready_org.png
/usr/share/winegui/images/windows/windows10_32-bit.png
/usr/share/winegui/images/windows/windows10_64-bit.png
/usr/share/winegui/images/windows/windows11_32-bit.png
/usr/share/winegui/images/windows/windows11_64-bit.png
/usr/share/winegui/images/windows/windows2.0_32-bit.png
/usr/share/winegui/images/windows/windows2000_32-bit.png
/usr/share/winegui/images/windows/windows2003_32-bit.png
/usr/share/winegui/images/windows/windows2003_64-bit.png
/usr/share/winegui/images/windows/windows2008_32-bit.png
/usr/share/winegui/images/windows/windows2008_64-bit.png
/usr/share/winegui/images/windows/windows2008r2_32-bit.png
/usr/share/winegui/images/windows/windows2008r2_64-bit.png
/usr/share/winegui/images/windows/windows3.0_32-bit.png
/usr/share/winegui/images/windows/windows3.1_32-bit.png
/usr/share/winegui/images/windows/windows7_32-bit.png
/usr/share/winegui/images/windows/windows7_64-bit.png
/usr/share/winegui/images/windows/windows8.1_32-bit.png
/usr/share/winegui/images/windows/windows8.1_64-bit.png
/usr/share/winegui/images/windows/windows8_32-bit.png
/usr/share/winegui/images/windows/windows8_64-bit.png
/usr/share/winegui/images/windows/windows95_32-bit.png
/usr/share/winegui/images/windows/windows98_32-bit.png
/usr/share/winegui/images/windows/windowsme_32-bit.png
/usr/share/winegui/images/windows/windowsnt3.51_32-bit.png
/usr/share/winegui/images/windows/windowsnt4.0_32-bit.png
/usr/share/winegui/images/windows/windowsvista_32-bit.png
/usr/share/winegui/images/windows/windowsvista_64-bit.png
/usr/share/winegui/images/windows/windowsxp_32-bit.png
/usr/share/winegui/images/windows/windowsxp_64-bit.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/winegui/f75ccad99ecd76c1f0858cbc59e64f430ffff079
