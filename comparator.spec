Summary:	Tools for fast comparasion of large source-code trees
Summary(pl.UTF-8):	Narzędzia do szybkiego porównania drzew kodu źródłowego
Name:		comparator
Version:	2.8
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.catb.org/~esr/comparator/%{name}-%{version}.tar.gz
# Source0-md5:	4523dfe8f14e5356df258ecd3f51499f
URL:		http://www.catb.org/~esr/comparator/
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comparator and filterator are a pair of tools for rapidly finding
common code segments in large source trees. They can be useful as
tools for detecting copyright infringement.

%description -l pl.UTF-8
Comparator i filterator są parą narzędzi do szybkiego znajdywania
wspólnych segmentów kodu w dużych drzewach kodu źródłowego. Mogą one
być użytecznymi narzędziami do wykrywania naruszeń praw autorskich.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{py_sitedir}}

install comparator filterator $RPM_BUILD_ROOT%{_bindir}
install comparator.1 $RPM_BUILD_ROOT%{_mandir}/man1
install comparator.py $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/comparator.1*
%{py_sitedir}/*
