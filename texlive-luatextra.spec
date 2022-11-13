Name:		texlive-luatextra
Version:	20747
Release:	1
Summary:	Additional macros for Plain TeX and LaTeX in LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luatextra
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a coherent extended programming
environment for use with luaTeX. It loads packages fontspec,
luatexbase and lualibs, and provides additional user-level
features and goodies. The package is under development, and its
specification may be expected to change.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/luatextra/luatextra.sty
%doc %{_texmfdistdir}/doc/lualatex/luatextra/News
%doc %{_texmfdistdir}/doc/lualatex/luatextra/README
%doc %{_texmfdistdir}/doc/lualatex/luatextra/luatextra.pdf
%doc %{_texmfdistdir}/doc/lualatex/luatextra/test.tex
#- source
%doc %{_texmfdistdir}/source/lualatex/luatextra/Makefile
%doc %{_texmfdistdir}/source/lualatex/luatextra/luatextra.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
