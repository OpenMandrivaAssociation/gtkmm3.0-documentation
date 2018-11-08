%define pkgname	gtkmm-documentation
%define api	3.0

Summary:	GTKmm reference manual and examples
Name:		gtkmm-documentation
Version:	3.22.1
Release:	1
License:	GPLv2+ and GFDL
Group:		Books/Other
URL:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
BuildArch: noarch
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtkmm-3.0)
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
%configure2_5x \
	--build=%{_build}

%make

%install
%makeinstall_std

%find_lang gtkmm-tutorial --with-gnome

%files -f gtkmm-tutorial.lang
%doc %{_datadir}/doc/gtkmm-%{api}



%changelog
* Mon Jul 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 809889
- update to new version 3.4.1

* Tue Nov 22 2011 Götz Waschk <waschk@mandriva.org> 3.2.1-1
+ Revision: 732355
- update to new version 3.2.1

* Mon Nov 21 2011 Götz Waschk <waschk@mandriva.org> 3.2.0-1
+ Revision: 732239
- new version
- bump deps

* Thu May 12 2011 Götz Waschk <waschk@mandriva.org> 3.0.3-1
+ Revision: 673858
- update to new version 3.0.3

* Fri Apr 15 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 653101
- update to new version 3.0.2

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 651082
- update to new version 3.0.0

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 2.99.4-1
+ Revision: 650195
- adapt for gtkmm 3.0

* Tue Sep 21 2010 Götz Waschk <waschk@mandriva.org> 2.21.8.1-1mdv2011.0
+ Revision: 580382
- update to new version 2.21.8.1

* Tue Apr 13 2010 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2010.1
+ Revision: 534014
- update to new version 2.20.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 529946
- new version
- bump deps

* Thu Feb 11 2010 Götz Waschk <waschk@mandriva.org> 2.19.3-1mdv2010.1
+ Revision: 504284
- update to new version 2.19.3

* Tue Jan 19 2010 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2010.1
+ Revision: 493567
- update to new version 2.19.2

* Mon Sep 28 2009 Götz Waschk <waschk@mandriva.org> 2.17.4-1mdv2010.0
+ Revision: 450608
- update to new version 2.17.4

* Tue Sep 15 2009 Götz Waschk <waschk@mandriva.org> 2.17.3-1mdv2010.0
+ Revision: 443159
- update to new version 2.17.3

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.17.1-1mdv2010.0
+ Revision: 440840
- new version
- update file list

* Mon Sep 07 2009 Götz Waschk <waschk@mandriva.org> 2.17.0-1mdv2010.0
+ Revision: 432755
- new version
- disable parallel make

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2009.1
+ Revision: 356704
- update to new version 2.16.0

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2009.0
+ Revision: 286614
- new version
- update file list
- update license
- import gtkmm2.4-doc

