Summary:	OpenSync Python plugin
Summary(pl.UTF-8):	Wtyczka Pythona do OpenSync
Name:		libopensync-plugin-python
Version:	0.36
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/download/releases/0.36/%{name}-%{version}.tar.gz
# Source0-md5:	b8a2d4632c88af3633453c668d2a7b11
URL:		http://www.opensync.org/
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	python-devel
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

%build
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync-1.0/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/opensync-1.0/python-plugins/sample.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS src/sample.py
%attr(755,root,root) %{_libdir}/opensync-1.0/plugins/python-module.so
%dir %{_libdir}/opensync-1.0/python-plugins
