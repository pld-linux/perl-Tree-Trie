%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	Trie
Summary:	Tree::Trie - An implementation of the Trie data structure in Perl
Summary(pl):	Tree::Trie - perlowa implementacja struktury danych Trie
Name:		perl-Tree-Trie
Version:	0.4
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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

%description -l pl
Ten modu³ jest implementacj± struktury danych Trie. Termin "trie"
pochodzi od s³owa "re*trie*val" (odtwarzanie, odzyskiwanie), ale
jest wymawiany jak angielskie s³owo "try". Trie to struktura
drzewiasta (lub skierowany graf acykliczny), której wêz³y reprezentuj±
litery w s³owie. Na przyk³ad, koñcowe wyszukiwanie s³owa "bob" bêdzie
wygl±daæ podobnie do $ref->{'b'}{'o'}{'b'}{HASH(0x80c6bbc)} (gdzie
HASH jest znacznikiem koñca). W strukturze istniej± tylko wêz³y
reprezentuj±ce s³owa, co czyni strukturê mniejsz± ni¿ hasz z tego
samego zbioru danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tree/Trie.pm
%{_mandir}/man3/*
