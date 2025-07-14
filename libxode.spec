Summary:	Library of XML, memory, and string helper functions
Summary(pl.UTF-8):	Biblioteka funkcji pomocniczych do XML-a, pamięci i łańcuchów
Name:		libxode
Version:	0.71
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libxode/%{name}-%{version}.tar.gz
# Source0-md5:	2314649f82d11eec6ba22f88d2e4ca9b
Patch0:		%{name}-system-expat.patch
Patch1:		%{name}-ac.patch
URL:		http://libxode.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxode provides a library of XML, memory, and string helper
functions. Jabber server software uses libxode extensively.

%description -l pl.UTF-8
libxode to biblioteka funkcji pomocniczych do XML-a, pamięci i
łańcuchów. Używana intensywnie przez oprogramowanie serwerowe Jabber.

%package devel
Summary:	Header files and development documentation for libxode
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libxode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95

%description devel
Header files and development documentation for libxode.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do libxode.

%package static
Summary:	Static version of libxode
Summary(pl.UTF-8):	Statyczna wersja libxode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libxode.

%description static -l pl.UTF-8
Statyczna wersja libxode.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxode.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libxode-config
%attr(755,root,root) %{_libdir}/libxode.so
%{_libdir}/libxode.la
%{_includedir}/libxode.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxode.a
