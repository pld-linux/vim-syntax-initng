Summary:	Vim syntax: initng
Summary(pl):	Sk³adnia dla Vima: initng
Name:		vim-syntax-initng
Version:	0.4.6
%define		_snap 20051129
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	http://glen.alkohol.ee/pld/initng/vim/initng-vim-%{version}-%{_snap}.tar.bz2
# Source0-md5:	8d1c81928810aae4674d9be76264670f
URL:		http://glen.alkohol.ee/pld/initng/vim/
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles
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
%doc README
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
