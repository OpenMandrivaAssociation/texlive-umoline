%global tl_name umoline
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Underline text allowing line breaking
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/umoline
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umoline.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides commands \Underline, \Midline and \Overline for underlining,
striking out, and overlining their text arguments.

