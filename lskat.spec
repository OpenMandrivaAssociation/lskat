Name:		lskat
Version:	15.12.3
Release:	2
Epoch:		1
Summary:	Lieutnant skat
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/lskat/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Requires:	libkdegames-common
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)

%description
Lieutnant Skat (from German "Offiziersskat") is a fun and engaging card game
for two players, where the second player is either live opponent, or a built
in artificial intelligence.

%files
%{_bindir}/lskat                                                                                       
%{_datadir}/applications/kde4/lskat.desktop                                                            
%{_datadir}/apps/lskat                                                                                 
%doc %{_docdir}/*/*/lskat                                                                              
%{_iconsdir}/hicolor/*/apps/lskat.png   

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
