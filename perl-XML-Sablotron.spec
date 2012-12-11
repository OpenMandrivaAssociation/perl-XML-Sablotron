%define upstream_name XML-Sablotron
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Sablotron XSLT processor encapsulation
License:	MPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		XML-Sablotron-1.01-perl5.14-build-fixes.patch
BuildRequires:	expat-devel
BuildRequires:	sablotron-devel >= 0.95	
BuildRequires:	perl-devel 
BuildRequires:	pkgconfig(mozjs185)

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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML
%{_mandir}/*/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.10.0-2
+ Revision: 773576
- sanitize dependencies
- clean out spec
- fix building against perl 5.14 (P0)
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 602396
- update to new version 1.01
- normalize version
- update to new version 1.01

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.01-5mdv2008.0
+ Revision: 36946
- rebuild for expat


* Sat Jan 13 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-4mdv2007.0
+ Revision: 108395
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-XML-Sablotron

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.01-3mdk
- Rebuild

* Sat May 28 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.01-2mdk
- add BuildRequires: libjs-devel

* Sat May 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.01-1mdk
- 1.01

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.98-6mdk
- disable test

* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.98-5mdk
- rebuild for new perl

* Sun May 23 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.98-4mdk
- rebuilt against new libsablotron
- msff

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.98-3mdk
- own dir
- rebuild

