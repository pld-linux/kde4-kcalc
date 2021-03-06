#
%define		_state		stable
%define		orgname		kcalc
%define		qtver		4.8.3

Summary:	K Desktop Environment - KDE calculator
Name:		kde4-kcalc
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7ea755bb177ce5c4121492147a3e7eb9
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gmp-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
Requires:	kde4-kdebase-workspace >= 4.11.4
Obsoletes:	kcalc
Obsoletes:	kde4-kdeutils-kcalc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calculator for KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/libkdeinit4_kcalc.so
%{_datadir}/apps/kcalc
%{_datadir}/apps/kconf_update/kcalcrc.upd
%{_datadir}/config.kcfg/kcalc.kcfg
%{_desktopdir}/kde4/kcalc.desktop
