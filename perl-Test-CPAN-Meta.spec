%define modname	Test-CPAN-Meta
%define modver 0.23

Summary:	Validation of META.yml specification elements
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-CPAN-Meta-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as the ExtUtils::MakeMaker manpage, the Module::Build
manpage and the Module::Install manpage.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*



