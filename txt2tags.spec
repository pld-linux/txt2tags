# TODO
#  - maybe the -vim subpackage isn't needed, but how then you can guarantee
#    existing parent dirs?
#  - txt2tags-vim or vim-txt2tags?
#  - package more extra/'s? (kate already has txt2tags!)
#  - lock vim version require to same vim major version detected at compile time somehow. (6.3 today)

Summary:	Tool to convert and to format texts
Summary(pl):	Narzêdzie do konwertowania i formatowania tekstu
Summary(pt_BR):	Ferramenta para converter e formatar textos
Name:		txt2tags
Version:	2.1
Release:	1.4
License:	GPL
Group:		Applications/Text
Source0:	http://txt2tags.sourceforge.net/src/%{name}-%{version}.tgz
# Source0-md5:	05a0ddcd76aaca72584a12520c764034
URL:		http://txt2tags.sourceforge.net/
BuildRequires:	bc
BuildRequires:	vim-rt
Requires:	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		vimep		%(rpm -q vim-rt --qf '%{EPOCH}')
%define		vimver		%(rpm -q vim-rt --qf '%{VERSION}' | cut -d. -f1,2)
%define		vimshv		%(echo %{vimver} | tr -d .)
%define		_vimdatadir	%{_datadir}/vim/vim%{vimshv}

%description
txt2tags is a tool to convert and to format texts. It functions thus:
you supply a text that has ones simple marquinhas for txt2tags and it
converts for any one of these formats:
- a document HTML
- a document SGML
- a document Latex
- a page of manual UNIX (manpage)
- a page of the MoinMoin
- a presentation of the Magic Point
- a PageMaker 6.0 document

%description -l pl
txt2tags jest narzêdziem s³u¿±cym do konwertowania oraz do
formatowania tekstów. Potrafi konwertowaæ ka¿dy z poni¿szych formatów:
- dokument HTML
- dokument SGML
- dokument Latex
- stronê podrêcznika UNIX (manpage)
- stronê MoinMoin
- prezentacjê Magic Point
- dokument PageMakera 6.0

%description -l pt_BR
txt2tags é uma ferramenta para converter e formatar textos. Funciona
assim: você fornece um texto com umas marquinhas simples para o
txt2tags e ele converte para qualquer um desses formatos:
- um documento HTML
- um documento SGML
- um documento LaTeX
- uma página de manual UNIX (manpage)
- uma página do MoinMoin
- uma apresentação do Magic Point
- um documento do PageMaker 6.0

%package vim
Summary:	Vim - syntax
Summary(pl):	Sk³adnia dla Vima
Group:		Applications/Editors/Vim
Requires:	vim >= %{vimep}:%{vimver}
Requires:	%{_vimdatadir}

%description vim
Vim syntax file and menu for gvim.

Also includes vim script to ':make' and build txt2tags target inside vim.
The hotkeys are <F5> for make, <F4> for displaying output and <F3> for discarding
output.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install doc/manpage.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,plugin}
install extras/txt2tags.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/plugin/%{name}.vim <<-EOF
" txt2tags file
au BufNewFile,BufRead *.t2t                 setf txt2tags
EOF
#" - for vim

install extras/txt2tags-compiler.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin
install extras/gvim-menu.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin/%{name}-menu.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc extras samples doc/userguide.pdf ChangeLog README* TEAM TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files vim
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/plugin/*
