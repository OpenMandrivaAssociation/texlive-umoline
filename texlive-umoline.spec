Name:		texlive-umoline
Version:	19085
Release:	1
Summary:	Underline text allowing line breaking
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umoline
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides commands \Underline, \Midline and \Overline for
underlining, striking out, and overlining their text arguments.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/umoline/umoline.sty
%doc %{_texmfdistdir}/doc/latex/umoline/README
%doc %{_texmfdistdir}/doc/latex/umoline/umoline-man.tex
%doc %{_texmfdistdir}/doc/latex/umoline/umoline.pdf
#- source
%doc %{_texmfdistdir}/source/latex/umoline/umoline.dtx
%doc %{_texmfdistdir}/source/latex/umoline/umoline.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
