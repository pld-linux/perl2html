Summary:	perl2html - converts perl files to HTML
Summary(pl.UTF-8):   perl2html - konwerter źródeł perlowych do HTML-a
Name:		perl2html
Version:	0.9.2
Release:	0.1
Epoch:		0
License:	GPL v2+
Group:		Applications/Text
Source0:	http://user.cs.tu-berlin.de/~schintke/x2html/%{name}-%{version}.tar.gz
# Source0-md5:	4b17cd3336227a788b53c080df314890
URL:		http://user.cs.tu-berlin.de/~schintke/x2html/index.html
BuildRequires:	autoconf
BuildRequires:	flex
Conflicts:	perl-Pod-Tree
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl2html highlights perl-language sources like emacs does. Output is
in HTML format. Also works as CGI to convert files on the fly.

%description -l pl.UTF-8
perl2html podświetla składnię źródeł w Perlu podobnie jak emacs.
Wyjście jest w formacie HTML. Działa także jako CGI konwertując pliki
w locie.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install perl2html $RPM_BUILD_ROOT%{_bindir}
install perl2html.1 $RPM_BUILD_ROOT%{_mandir}/man1/perl2html.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/perl2html.1*
