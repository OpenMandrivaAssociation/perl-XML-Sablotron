%define module	XML-Sablotron
%define	name	perl-%{module}
%define version 1.01
%define release %mkrel 8

Summary:	Sablotron XSLT processor encapsulation
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
Requires:	libsablotron >= 0.95
BuildRequires:	libexpat-devel
BuildRequires:	libsablotron-devel >= 0.95
BuildRequires:	perl-devel 
BuildRequires:	libjs-devel
Requires:	perl 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The %{module} perl module encapsulates the Sablotron XSLT processor.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%check
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall_std}

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML
%{_mandir}/*/*
