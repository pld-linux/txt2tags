
%define		_vimdatadir	%{_datadir}/vim/vimfiles

Summary:	Tool to convert and to format texts
Summary(pl.UTF-8):	Narzędzie do konwertowania i formatowania tekstu
Summary(pt_BR.UTF-8):	Ferramenta para converter e formatar textos
Name:		txt2tags
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://txt2tags.sourceforge.net/src/%{name}-%{version}.tgz
# Source0-md5:	0514bb01161183808dc8be105c032677
URL:		http://txt2tags.sourceforge.net/
Requires:	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
txt2tags jest narzędziem służącym do konwertowania oraz do
formatowania tekstów. Potrafi konwertować każdy z poniższych formatów:
- dokument HTML
- dokument SGML
- dokument Latex
- stronę podręcznika UNIX (manpage)
- stronę MoinMoin
- prezentację Magic Point
- dokument PageMakera 6.0

%description -l pt_BR.UTF-8
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
Summary(pl.UTF-8):	Składnia dla Vima
Group:		Applications/Editors/Vim
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{_vimdatadir}
Requires:	vim >= 4:6.3.058-3

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

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,plugin,ftplugin}
install extras/txt2tags.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/plugin/%{name}.vim <<-EOF
" txt2tags file
au BufNewFile,BufRead *.t2t                 setf txt2tags
EOF
#" - for vim

install extras/txt2tags-compiler.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin/%{name}.vim
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
%{_vimdatadir}/ftplugin/*
