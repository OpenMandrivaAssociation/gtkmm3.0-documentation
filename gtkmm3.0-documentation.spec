%define version 3.2.1
%define release %mkrel 1

%define pkgname	gtkmm-documentation
%define api_version 3.0

Name:		gtkmm%{api_version}-documentation
Summary:	GTKmm reference manual and examples
Version:	%{version}
Release:	%{release}
License:	GPLv2+ and GFDL
Group:		Books/Other
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
BuildRequires: gtkmm3.0-devel >= 3.2
BuildRequires: glibmm2.4-devel >= 2.24.0
BuildRequires: gnome-doc-utils
BuildArch: noarch
Requires: gtkmm3.0-doc

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm3 wraps GTK+ 3.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for gtkmm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q -n %{pkgname}-%{version}

%build
./configure --prefix=%_prefix
make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang gtkmm-tutorial --with-gnome

%clean
rm -rf %{buildroot}

%files -f gtkmm-tutorial.lang
%defattr(-, root, root)
%doc %{_datadir}/doc/gtkmm-%{api_version}


