%include	/usr/lib/rpm/macros.python
Summary:	Tools for fast comparasion of large source-code trees
Summary(pl):	Narzêdzia do szybkiego porównania drzew kodu ¼ród³owego
Name:		comparator
Version:	2.4
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.catb.org/~esr/comparator/%{name}-%{version}.tar.gz
# Source0-md5:	e4161ae7ab845dcf47d2d8549452fc05
URL:		http://www.catb.org/~esr/comparator/
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comparator and filterator are a pair of tools for rapidly finding
common code segments in large source trees. They can be useful as
tools for detecting copyright infringement.

%description -l pl
Comparator i filterator s± par± narzêdzi do szybkiego znajdywania
wspólnych segmentów kodu w du¿ych drzewach kodu ¼ród³owego. Mog± one
byæ u¿ytecznymi narzêdziami do wykrywania naruszeñ praw autorskich.

%prep
%setup -q

%build
%{__make} \
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
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/comparator.1*
%{py_sitedir}/*
