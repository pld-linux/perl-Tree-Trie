%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	Trie
Summary:	Tree::Trie - an implementation of the Trie data structure in Perl
Summary(pl):	Tree::Trie - implementacja perlowa struktury danych Trie
Name:		perl-Tree-Trie
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82eb063ab6dd00e78b1aeee52ea553ea
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
Ten modu� jest implementacj� struktury danych Trie. Termin "trie"
pochodzi od s�owa "re*trie*val" (odtwarzanie, odzyskiwanie), ale
jest wymawiany jak angielskie s�owo "try". Trie to struktura
drzewiasta (lub skierowany graf acykliczny), kt�rej w�z�y reprezentuj�
litery w s�owie. Na przyk�ad, ko�cowe wyszukiwanie s�owa "bob" b�dzie
wygl�da� podobnie do $ref->{'b'}{'o'}{'b'}{HASH(0x80c6bbc)} (gdzie
HASH jest znacznikiem ko�ca). W strukturze istniej� tylko w�z�y
reprezentuj�ce s�owa, co czyni struktur� mniejsz� ni� hasz z tego
samego zbioru danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tree/Trie.pm
%{_mandir}/man3/*
