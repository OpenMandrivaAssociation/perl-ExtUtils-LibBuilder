%define upstream_name    ExtUtils-LibBuilder
%define upstream_version 0.09
Name:       perl-%{upstream_name}
Version:	0.09
Release:	2

Summary:    A tool to build C libraries
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/ambs/ExtUtils-LibBuilder
Source0:	https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-LibBuilder-0.09.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildRequires: perl-devel
BuildArch: noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




