%include	/usr/lib/rpm/macros.perl
%define	pdir	Tree
%define	pnam	Trie
Summary:	Tree::Trie - An implementation of the Trie data structure in Perl
Name:		perl-Tree-Trie
Version:	0.4
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a trie data structure.  The term "trie" comes from
the word reB<trie>val, but is generally pronounced like "try".  A trie is
a tree structure (or directed acyclic graph), the nodes of which represent
letters in a word.  For example, the final lookup for the word 'bob'
would look something like C<$ref-E<gt>{'b'}{'o'}{'b'}{HASH(0x80c6bbc)}>
(the HASH being an end marker).  Only nodes which would represent words
in the trie exist, making the structure slightly smaller than a hash of
the same data set.

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
