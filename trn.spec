Summary: A news reader that displays postings in threaded format.
Name: trn
Version: 3.6
Release: 16
Copyright: distributable
Group: Applications/Internet
Source0:  ftp://ftp.uu.net:/networking/news/readers/trn/trn-3.6.tar.gz
Source1: trn.wmconfig
Patch0: trn-3.6-linux.patch
Patch1: trn-3.6-sigtstp.patch
Patch2: trn-3.6-make.patch
Patch3: trn-3.6-bool.patch
Buildroot: /var/tmp/trn-root

%description
Trn is a basic news reader that supports threading.  This version is
configured to read news from an NNTP news server.

Install trn if you need a basic news reader that shows you newsgroup
postings in threaded format.

%prep
%setup -q 
%patch0 -p1 -b .linux
%patch1 -p1 -b .sigstp
%patch2 -p1 -b .make
%patch3 -p1 -b .bool

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/lib/trn
mkdir -p $RPM_BUILD_ROOT/usr/man/man1/

chmod 755 filexp
chmod 755 makedir

make install RPM_INSTALL=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT/usr/bin/*
chmod 755 $RPM_BUILD_ROOT/usr/lib/*

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
cp $RPM_SOURCE_DIR/trn.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/trn

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README INSTALL MANIFEST HINTS.TRN HACKERSGUIDE NEW
/usr/bin/trn
/usr/bin/newsetup
/usr/bin/newsgroups
/usr/bin/Pnews
/usr/bin/Rnmail
/usr/bin/trn-artchk
/usr/bin/nntplist
/usr/lib/trn
/usr/man/man1/trn.1
/usr/man/man1/Pnews.1
/usr/man/man1/Rnmail.1
/usr/man/man1/newsetup.1
/usr/man/man1/newsgroups.1
%config /etc/X11/wmconfig/trn
