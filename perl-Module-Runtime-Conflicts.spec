#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Runtime-Conflicts
Version  : 0.003
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Runtime-Conflicts-0.003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Runtime-Conflicts-0.003.tar.gz
Summary  : 'Provide information on conflicts for Module::Runtime'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Runtime-Conflicts-data = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Module::Runtime)

%description
This archive contains the distribution Module-Runtime-Conflicts,
version 0.003:
Provide information on conflicts for Module::Runtime

%package data
Summary: data components for the perl-Module-Runtime-Conflicts package.
Group: Data

%description data
data components for the perl-Module-Runtime-Conflicts package.


%package dev
Summary: dev components for the perl-Module-Runtime-Conflicts package.
Group: Development
Requires: perl-Module-Runtime-Conflicts-data = %{version}-%{release}
Provides: perl-Module-Runtime-Conflicts-devel = %{version}-%{release}

%description dev
dev components for the perl-Module-Runtime-Conflicts package.


%prep
%setup -q -n Module-Runtime-Conflicts-0.003

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-Runtime-Conflicts
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-Module-Runtime-Conflicts/LICENCE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Module/Runtime/Conflicts.pm

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-Module-Runtime-Conflicts/LICENCE

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Runtime::Conflicts.3
