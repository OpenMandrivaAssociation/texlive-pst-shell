Name:		texlive-pst-shell
Version:	56070
Release:	1
Summary:	Plotting sea shells
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-shell
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-shell.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-shell.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-shell.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-shell is a PSTricks related package to draw seashells in 3D
view: Argonauta, Epiteonium, Lyria, Turritella, Tonna,
Achatina, Oxystele, Conus, Ammonite, Codakia, Escalaria,
Helcion, Natalina, Planorbis, and Nautilus, all with different
parameters. pst-shell needs pst-solides3d and an up-to-date
PSTricks, which should be part of your local TeX installation,
otherwise get it from a CTAN server.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/pst-shell
%{_texmfdistdir}/tex/latex/pst-shell
%{_texmfdistdir}/tex/generic/pst-shell
%{_texmfdistdir}/dvips/pst-shell
%doc %{_texmfdistdir}/doc/generic/pst-shell

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
