# TODO:
# - create more plugin packages from extras instead of packaging whole extras as doc
# - more internationalized docs?
Summary:	Tool to convert and to format texts
Summary(pl.UTF-8):	Narzędzie do konwertowania i formatowania tekstu
Summary(pt_BR.UTF-8):	Ferramenta para converter e formatar textos
Name:		txt2tags
Version:	2.6
Release:	1
License:	GPL v2
Group:		Applications/Text
#Source0Download: https://github.com/txt2tags/txt2tags/releases
Source0:	https://github.com/txt2tags/txt2tags/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	531e4ab3f0fb0a4dac5abb0605472109
URL:		https://txt2tags.org/
Requires:	python >= 2.3
Requires:	python-modules >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

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

%package -n vim-syntax-txt2tags
Summary:	Vim plugin with txt2tags syntax support
Summary(pl.UTF-8):	Wtyczka do Vima z obsługą składni txt2tags
Group:		Applications/Editors/Vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:6.3.058-3
Provides:	txt2tags-vim = %{version}-%{release}
Obsoletes:	txt2tags-vim < 2.3-3

%description -n vim-syntax-txt2tags
Vim syntax file and menu for gvim.

Also includes vim script to ':make' and build txt2tags target inside
vim. The hotkeys are <F5> for make, <F4> for displaying output and
<F3> for discarding output.

%description -n vim-syntax-txt2tags -l pl.UTF-8
Plik składni dla Vima oraz menu dla gvima.

Pakiet zawiera także skrypt Vima do wykonywania ':make' oraz budowania
txt2tags z poziomu edytora. Skróty klawiszowe to <F5> dla make'a, <F4>
do pokazywania wyjścia oraz <F3> do porzucania wyjścia.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_mandir}/{ca,de,es,eu,fr,it,pt,zh_CN}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -p doc/Basque/manpage-eu.man $RPM_BUILD_ROOT%{_mandir}/eu/man1/%{name}.1
cp -p doc/Catalan/manpage-ca.man $RPM_BUILD_ROOT%{_mandir}/ca/man1/%{name}.1
cp -p doc/Chinese/manpage-zh.man $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1/%{name}.1
cp -p doc/English/manpage.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
cp -p doc/French/manpage-fr.man $RPM_BUILD_ROOT%{_mandir}/fr/man1/%{name}.1
cp -p doc/German/manpage-de.man $RPM_BUILD_ROOT%{_mandir}/de/man1/%{name}.1
cp -p doc/Italian/manpage-it.man $RPM_BUILD_ROOT%{_mandir}/it/man1/%{name}.1
cp -p doc/Portuguese/manpage-pt.man $RPM_BUILD_ROOT%{_mandir}/pt/man1/%{name}.1
cp -p doc/Spanish/manpage-es.man $RPM_BUILD_ROOT%{_mandir}/es/man1/%{name}.1

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,plugin,ftplugin}
cp -p extras/{pagemaker,txt2tags}.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/plugin/%{name}.vim <<-EOF
" txt2tags file
au BufNewFile,BufRead *.t2t                 setf txt2tags
EOF
#" - for vim

cp -p extras/txt2tags-compiler.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin/%{name}.vim
cp -p extras/gvim-menu.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin/%{name}-menu.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README extras samples doc/English/userguide.pdf
%attr(755,root,root) %{_bindir}/txt2tags
%{_mandir}/man1/txt2tags.1*
%lang(ca) %{_mandir}/ca/man1/txt2tags.1*
%lang(de) %{_mandir}/de/man1/txt2tags.1*
%lang(es) %{_mandir}/es/man1/txt2tags.1*
%lang(eu) %{_mandir}/eu/man1/txt2tags.1*
%lang(fr) %{_mandir}/fr/man1/txt2tags.1*
%lang(it) %{_mandir}/it/man1/txt2tags.1*
%lang(pt) %{_mandir}/pt/man1/txt2tags.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/txt2tags.1*

%files -n vim-syntax-txt2tags
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/pagemaker.vim
%{_vimdatadir}/syntax/txt2tags.vim
%{_vimdatadir}/plugin/txt2tags.vim
%{_vimdatadir}/plugin/txt2tags-menu.vim
%{_vimdatadir}/ftplugin/txt2tags.vim
