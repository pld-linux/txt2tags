Summary:	Tool to convert and to format texts
Summary(pl):	Narzêdzie do konwertowania i formatowania tekstu
Summary(pt_BR):	Ferramenta para converter e formatar textos
Name:		txt2tags
Version:	1.7
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://txt2tags.sourceforge.net/src/%{name}-%{version}.tgz
# Source0-md5:	bbee7b77dfff87e1666eb7071d7d0281
URL:		http://txt2tags.sourceforge.net/
Requires:	python
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

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc contrib extras samples userguide ChangeLog.txt README* RULES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
