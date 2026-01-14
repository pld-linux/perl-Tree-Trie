#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Tree
%define		pnam	Trie
Summary:	Tree::Trie - an implementation of the Trie data structure in Perl
Summary(pl.UTF-8):	Tree::Trie - implementacja perlowa struktury danych Trie
Name:		perl-Tree-Trie
Version:	1.9
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tree/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b823d1896e43279227d65e6ff947d98
URL:		http://search.cpan.org/dist/Tree-Trie/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a trie data structure. The term "trie" comes
from the word re*trie*val, but is generally pronounced like "try". A
trie is a tree structure (or directed acyclic graph), the nodes of
which represent letters in a word. For example, the final lookup for
the word 'bob' would look something like
$ref->{'b'}{'o'}{'b'}{HASH(0x80c6bbc)} (the HASH being an end
marker). Only nodes which would represent words in the trie exist,
making the structure slightly smaller than a hash of the same data
set.

%description -l pl.UTF-8
Ten moduł jest implementacją struktury danych Trie. Termin "trie"
pochodzi od słowa "re*trie*val" (odtwarzanie, odzyskiwanie), ale
jest wymawiany jak angielskie słowo "try". Trie to struktura
drzewiasta (lub skierowany graf acykliczny), której węzły reprezentują
litery w słowie. Na przykład, końcowe wyszukiwanie słowa "bob" będzie
wyglądać podobnie do $ref->{'b'}{'o'}{'b'}{HASH(0x80c6bbc)} (gdzie
HASH jest znacznikiem końca). W strukturze istnieją tylko węzły
reprezentujące słowa, co czyni strukturę mniejszą niż hasz z tego
samego zbioru danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tree/Trie.pm
%{_mandir}/man3/*
