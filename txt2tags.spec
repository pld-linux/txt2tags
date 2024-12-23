Summary:	Tool to convert and to format texts
Summary(pl.UTF-8):	Narzędzie do konwertowania i formatowania tekstu
Summary(pt_BR.UTF-8):	Ferramenta para converter e formatar textos
Name:		txt2tags
Version:	3.9
Release:	1
License:	GPL v2
Group:		Applications/Text
#Source0Download: https://github.com/txt2tags/txt2tags/releases
Source0:	https://github.com/txt2tags/txt2tags/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f0479f60e64708af9ea09a381bc8d6f8
Patch0:		local-docs.patch
URL:		https://txt2tags.org/
Requires:	python3
Requires:	python3-modules
Obsoletes:	vim-syntax-txt2tags < 3.9
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

%prep
%setup -q
%patch -P 0 -p1

./docs/build-docs.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__sed} -e '1s,/usr/bin/env python,%{__python3},' txt2tags.py > $RPM_BUILD_ROOT%{_bindir}/txt2tags

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md extras
%doc docs/markup/markup.html
%doc docs/rules/rules.{css,html}
%doc docs/userguide/userguide.{css,html}
%attr(755,root,root) %{_bindir}/txt2tags
