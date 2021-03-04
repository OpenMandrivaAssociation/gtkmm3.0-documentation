%define pkgname	gtkmm-documentation
%define api	3.0

Summary:	GTKmm reference manual and examples
Name:		gtkmm-documentation
Version:	3.24.1
Release:	1
License:	GPLv2+ and GFDL
Group:		Books/Other
URL:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
BuildArch: noarch
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	scrollkeeper
BuildRequires:	pkgconfig
BuildRequires:	intltool
BuildRequires:	perl
Requires:	gtkmm3.0-doc

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm3 wraps GTK+ 3.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for gtkmm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name --with-gnome

%files -f %{name}.lang
%doc NEWS  README AUTHORS
%{_datadir}/doc/gtkmm-3.0/

