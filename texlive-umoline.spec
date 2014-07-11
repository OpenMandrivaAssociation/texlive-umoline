# revision 19085
# category Package
# catalog-ctan /macros/latex/contrib/umoline
# catalog-date 2007-01-20 15:20:16 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-umoline
Version:	20070120
Release:	8
Summary:	Underline text allowing line breaking
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umoline
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070120-2
+ Revision: 757252
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070120-1
+ Revision: 719842
- texlive-umoline
- texlive-umoline
- texlive-umoline

