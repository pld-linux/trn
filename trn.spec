Summary:	A news reader that displays postings in threaded format
Summary(pl):	Czytnik newsów wy¶wietlaj±cy posty w postaci w±tków
Name:		trn
Version:	3.6
Release:	17
License:	distributable
Group:		Applications/News
Group(de):	Applikationen/News
Group(pl):	Aplikacje/News
Source0:	ftp://ftp.uu.net:/networking/news/readers/trn/%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig
Patch0:		%{name}-3.6-linux.patch
Patch1:		%{name}-3.6-sigtstp.patch
Patch2:		%{name}-3.6-bool.patch
Patch3:		%{name}-time-include.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trn is a basic news reader that supports threading. This version is
configured to read news from an NNTP news server.

Install trn if you need a basic news reader that shows you newsgroup
postings in threaded format.

%description -l pl
Trn to prosty czytnik news obs³uguj±cy w±tkowanie. Ta wersja jest
skonfigurowana do pobierania artyku³ów z serwera NNTP.

Zainstaluj ten pakiet, je¶li potrzebujesz prostego czytnika news,
który poka¿e ci listê artyku³ów w postaci w±tków.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/trn}

chmod 755 filexp makedir

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/trn

gzip -9nf README MANIFEST HINTS.TRN HACKERSGUIDE NEW

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,MANIFEST,HINTS.TRN,HACKERSGUIDE,NEW}.gz
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
%config %{_sysconfdir}/X11/wmconfig/trn
