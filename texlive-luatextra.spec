%global tl_name luatextra
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Additional macros for Plain TeX and LaTeX in LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luatextra
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a coherent extended programming environment for use
with LuaTeX. It loads packages fontspec, luatexbase and lualibs, and
provides additional user-level features and goodies. The package is
under development, and its specification may be expected to change.

