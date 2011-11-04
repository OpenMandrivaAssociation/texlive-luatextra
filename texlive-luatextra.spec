# revision 20747
# category Package
# catalog-ctan /macros/luatex/latex/luatextra
# catalog-date 2010-12-14 15:25:48 +0100
# catalog-license pd
# catalog-version 1.0.1
Name:		texlive-luatextra
Version:	1.0.1
Release:	1
Summary:	Additional macros for Plain TeX and LaTeX in LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luatextra
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatextra.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a coherent extended programming
environment for use with luaTeX. It loads packages fontspec,
luatexbase and lualibs, and provides additional user-level
features and goodies. The package is under development, and its
specification may be expected to change.

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
%{_texmfdistdir}/tex/lualatex/luatextra/luatextra.sty
%doc %{_texmfdistdir}/doc/lualatex/luatextra/News
%doc %{_texmfdistdir}/doc/lualatex/luatextra/README
%doc %{_texmfdistdir}/doc/lualatex/luatextra/luatextra.pdf
%doc %{_texmfdistdir}/doc/lualatex/luatextra/test.tex
#- source
%doc %{_texmfdistdir}/source/lualatex/luatextra/Makefile
%doc %{_texmfdistdir}/source/lualatex/luatextra/luatextra.dtx
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
