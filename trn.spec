Summary:	A news reader that displays postings in threaded format
Summary(es.UTF-8):   Lector de News con Threads
Summary(pl.UTF-8):   Czytnik newsów wyświetlający posty w postaci wątków
Summary(pt_BR.UTF-8):   Leitor de News com Threads
Name:		trn
Version:	3.6
Release:	18
License:	distributable
Group:		Applications/News
Source0:	ftp://ftp.uu.net:/networking/news/readers/trn/%{name}-%{version}.tar.gz
# Source0-md5:	0337ebc89f64825bc4ce2fb12e5b96a7
Source1:	%{name}.desktop
Patch0:		%{name}-linux.patch
Patch1:		%{name}-sigtstp.patch
Patch2:		%{name}-bool.patch
Patch3:		%{name}-time-include.patch
Patch4:		%{name}-bison.patch
BuildRequires:	bison
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trn is a basic news reader that supports threading. This version is
configured to read news from an NNTP news server.

%description -l es.UTF-8
'trn' es uno de los lectores originales de threaded news. Esta versión
está configurada para leer news de un servidor NNTP.

%description -l pl.UTF-8
Trn to prosty czytnik news obsługujący wątkowanie. Ta wersja jest
skonfigurowana do pobierania artykułów z serwera NNTP.

%description -l pt_BR.UTF-8
'trn' é um dos leitores originais de threaded news. Esta versão é
configurada para ler news de um servidor NNTP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/trn,%{_desktopdir}}

chmod 755 filexp makedir

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MANIFEST HINTS.TRN HACKERSGUIDE NEW
%attr(755,root,root) %{_bindir}/trn
%attr(755,root,root) %{_bindir}/newsetup
%attr(755,root,root) %{_bindir}/newsgroups
%attr(755,root,root) %{_bindir}/Pnews
%attr(755,root,root) %{_bindir}/Rnmail
%attr(755,root,root) %{_bindir}/trn-artchk
%attr(755,root,root) %{_bindir}/nntplist
%dir %{_libdir}/trn
%attr(755,root,root) %{_libdir}/trn/*
%{_mandir}/man1/trn.1*
%{_mandir}/man1/Pnews.1*
%{_mandir}/man1/Rnmail.1*
%{_mandir}/man1/newsetup.1*
%{_mandir}/man1/newsgroups.1*
%{_desktopdir}/*.desktop
