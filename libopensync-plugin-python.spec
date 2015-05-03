Summary:	OpenSync Python plugin
Summary(pl.UTF-8):	Wtyczka Pythona do OpenSync
Name:		libopensync-plugin-python
Version:	0.36
Release:	8
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/0.36/%{name}-%{version}.tar.gz
# Source0-md5:	b8a2d4632c88af3633453c668d2a7b11
Patch0:		cmake.patch
Patch1:		branch.diff
URL:		http://www.opensync.org/
BuildRequires:	cmake >= 2.8
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= 1:0.39-7
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	sed >= 4.0
Requires:	python-opensync >= 1:0.39
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync is a synchronization framework that is platform and
distribution independent.

It consists of several plugins that can be used to connect to devices,
a powerful sync-engine and the framework itself.

This package contains Python plugin for OpenSync framework.

%description -l pl.UTF-8
OpenSync to niezależny od platformy i dystrybucji szkielet do
synchronizacji danych.

Składa się z różnych wtyczek, których można używać do łączenia z
urządzeniami, potężnego silnika synchronizacji oraz samego szkieletu.

Ten pakiet zawiera wtyczkę Pythona dla szkieletu OpenSync.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# use system version
%{__rm} cmake/modules/FindPythonLibs.cmake

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/libopensync1/python-plugins/sample.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS src/sample.py
%attr(755,root,root) %{_libdir}/libopensync1/plugins/python-module.so
%dir %{_datadir}/libopensync1/python-plugins
