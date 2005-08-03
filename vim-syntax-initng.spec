
%define		_vimdatadir	%{_datadir}/vim/vimfiles

%define		_snap 20050729
Summary:	Vim syntax: initng
Summary(pl):	Sk³adnia dla Vima: initng
Name:		vim-syntax-initng
Version:	0.2
Release:	0.%{_snap}.8
License:	GPL
Group:		Applications/Editors/Vim
Source0:	http://glen.alkohol.ee/pld/initng/vim/initng-vim-%{_snap}.tar.bz2
# Source0-md5:	4b640815358793d78e367f3b9b281925
URL:		http://glen.alkohol.ee/pld/initng/vim/
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_syntax initng

%description
This plugin provides syntax highlighting for initng files.

%description -l pl
Ta wtyczka dostarcza pod¶wietlanie sk³adni dla plików initng.

%prep
%setup -q -n initng-vim-%{_snap}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install syntax.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{_syntax}.vim
install ftdetect.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{_syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
