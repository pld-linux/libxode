Summary:	Library of XML, memory, and string helper functions
Summary(pl):	Biblioteka funkcji pomocniczych do XML, pamiêci i stringów
Name:		libxode
Version:	0.71
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/libxode/%{name}-%{version}.tar.gz
# Source0-md5:	2314649f82d11eec6ba22f88d2e4ca9b
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxode provides a library of XML, memory, and string helper
functions. Jabber server software uses libxode extensively.

%description -l pl
libxode to biblioteka funkcji pomocniczych do XML, pamiêci i stringów.
U¿ywana intensywnie przez oprogramowanie serwerowe Jabber.

%package devel
Summary:	Header files and development documentation for libxode
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libxode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libxode.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do libxode.

%package static
Summary:	Static version of libxode
Summary(pl):	Statyczna wersja libxode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libxode.

%description static -l pl
Statyczna wersjaa libxode.

%prep
%setup -q

%build
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
%{_includedir}/%{name}*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
