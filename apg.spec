Summary:	apg - Automated Password Generator
Summary(pl):	apg - automatyczny generator hase�
Name:		apg
Version:	2.0.0a3
Release:	1
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.adel.nursat.kz/apg/download/%{name}-%{version}.tar.gz
URL:		http://www.adel.nursat.kz/apg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apg generates several random passwords. It uses several password
generation algorithms (currently two) and a built-in pseudo random
number generator.

%description -l pl
apg generuje losowe has�a. Korzysta z kilku (aktualnie dw�ch)
algorytm�w i wbudowanego generatora liczb pseudolosowych.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install apg apgbfm $RPM_BUILD_ROOT%{_bindir}
install doc/man/apg.1 doc/man/apgbfm.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README CHANGES THANKS TODO doc/{APG_TIPS,rfc0972.txt,rfc1750.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apg
%attr(755,root,root) %{_bindir}/apgbfm
%doc *.gz
%doc doc/*.gz
%{_mandir}/man1/*
