
%define	snap	20011218

Summary:	Library of XML, memory, and string helper functions
Summary(pl):	Biblioteka funkcji pomocniczych do XML, pamiЙci i stringСw
Name:		libxode
Version:	1.2
Release:	1.%{snap}
License:	GPL/LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	http://download.jabber.org/cvs/%{name}.tgz
Patch0:		%{name}-cvs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxode provides a library of XML, memory, and string helper
functions. Jabber server software uses libxode extensively.

%description -l pl
libxode to biblioteka funkcji pomocniczych do XML, pamiЙci i stringСw.
U©ywana intensywnie przez oprogramowanie serwerowe Jabber.

%package devel
Summary:	Header files and development documentation for libxode
Summary(pl):	Pliki nagЁСwkowe i dokumentacja do libxode
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libxode.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja programisty do libxode.

%package static
Summary:	Static version of libxode
Summary(pl):	Statyczna wersja libxode
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static version of libxode.

%description static -l pl
Statyczna wersjaa libxode.

%prep
%setup -qn libxode
%patch0 -p1

%build
aclocal
autoheader
automake -a
autoconf 
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
