# revision 19085
# category Package
# catalog-ctan /macros/latex/contrib/umoline
# catalog-date 2007-01-20 15:20:16 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-umoline
Version:	20070120
Release:	1
Summary:	Underline text allowing line breaking
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umoline
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides commands \Underline, \Midline and \Overline for
underlining, striking out, and overlining their text arguments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
