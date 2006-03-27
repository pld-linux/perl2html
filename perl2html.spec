# $Revision: 1.1 $
#
# Conditional build:
#
Summary:	perl2html - converts perl files to HTML
Summary(pl):	perl2html - konwerter ¼róde³ perl na HTML
Name:		perl2html
Version:	0.9.2
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Text
Source0:	http://user.cs.tu-berlin.de/~schintke/x2html/%{name}-%{version}.tar.gz
# Source0-md5:	4b17cd3336227a788b53c080df314890
URL:		http://user.cs.tu-berlin.de/~schintke/x2html/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	flex
Provides:	perl2html
Conflicts:	perl-Pod-Tree
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl2html highlights perl-language sources like emacs does. Output is in
HTML format. Also works as CGI to convert files on the fly.

%description -l pl
perl2html pod¶wietla sk³adniê ¼róde³ perl podobnie jak emacs. Wyj¶cie jest
w formacie HTML. Dzia³a tak¿e jako CGI konwertuj±c pliki w locie.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -d $RPM_BUILD_ROOT/usr/share/man/man1/
install -c -m 644 perl2html.1 $RPM_BUILD_ROOT/usr/share/man/man1/perl2html.1
install -c -m 644 AUTHORS $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -c -m 644 COPYING $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -c -m 644 NEWS $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -c -m 644 README $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -c -m 755 perl2html $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/perl2html.*
%attr(755,root,root) %{_bindir}/*
