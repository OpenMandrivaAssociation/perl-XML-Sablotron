%define upstream_name    XML-Sablotron
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2
Summary:	Sablotron XSLT processor encapsulation
License:	MPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		XML-Sablotron-1.01-perl5.14-build-fixes.patch
Requires:	libsablotron >= 0.95
BuildRequires:	libexpat-devel
BuildRequires:	libsablotron-devel >= 0.95
BuildRequires:	perl-devel 
BuildRequires:	libjs-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package is a interface to the Sablotron API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .perl514~

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}

%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML
%{_mandir}/*/*
