Name:		lskat
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Lieutnant skat
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/lskat/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Requires:	libkdegames-common

%description
Lieutnant Skat (from German "Offiziersskat") is a fun and engaging card game
for two players, where the second player is either live opponent, or a built
in artificial intelligence.

%files
%{_kde_bindir}/lskat
%{_kde_applicationsdir}/lskat.desktop
%{_kde_appsdir}/lskat
%{_kde_docdir}/*/*/lskat
%{_kde_iconsdir}/hicolor/*/apps/lskat.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

