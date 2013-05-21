%define upstream_name    Test-CPAN-Meta
%define upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Validation of META.yml specification elements
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as the ExtUtils::MakeMaker manpage, the Module::Build
manpage and the Module::Install manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-5mdv2012.0
+ Revision: 765675
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-4
+ Revision: 764186
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-3
+ Revision: 676639
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2
+ Revision: 657470
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.180.0-1
+ Revision: 638961
- update to new version 0.18

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 536213
- update to 0.17

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 480737
- update to 0.16

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 478058
- update to 0.15

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 474749
- update to 0.14

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 408937
- import perl-Test-CPAN-Meta


* Tue Aug 04 2009 cpan2dist 0.13-1mdv
- initial mdv release, generated with cpan2dist
