Summary:	IBM PKCS#11 engine for OpenSSL
Summary(pl.UTF-8):	Silnik IBM PKCS#11 dla OpenSSL-a
Name:		openssl-engine-ibmpkcs11
Version:	1.0.0
Release:	1
License:	OpenSSL (Apache-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencryptoki/openssl-ibmpkcs11-%{version}.tar.gz
# Source0-md5:	3ebb42c427a492a06c146bb9211243b8
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6.3
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.8
Requires:	openssl >= 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBM PKCS#11 engine for OpenSSL.

%description -l pl.UTF-8
Silnik IBM PKCS#11 dla OpenSSL-a.

%prep
%setup -q -n openssl-ibmpkcs11-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{_libdir}/engines
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/engines/libibmpkcs11.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README openssl.cnf.sample
%attr(755,root,root) %{_libdir}/engines/libibmpkcs11.so*
