%global tl_name pst-shell
%global tl_revision 79376

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04
Release:	%{tl_revision}.1
Summary:	Plotting sea shells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-shell
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-shell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-shell.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
pst-shell is a PSTricks related package to draw seashells in 3D view:
Argonauta, Epiteonium, Lyria, Turritella, Tonna, Achatina, Oxystele,
Conus, Ammonite, Codakia, Escalaria, Helcion, Natalina, Planorbis, and
Nautilus, all with different parameters. pst-shell needs pst-solides3d
and an up-to-date PSTricks, which should be part of your local TeX
installation, otherwise get it from a CTAN server.

