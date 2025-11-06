#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		lskat
Version:	25.08.3
Release:	%{?git:0.%{git}.}1
Summary:	Lieutenant skat
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/lskat/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/lskat/-/archive/%{gitbranch}/lskat-%{gitbranchd}.tar.bz2#/lskat-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/lskat-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Phonon4Qt6)

%rename plasma6-lskat

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Lieutenant Skat (from German "Offiziersskat") is a fun and engaging card game
for two players, where the second player is either live opponent, or a built
in artificial intelligence.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/lskat.categories
%{_datadir}/qlogging-categories6/lskat.renamecategories
%{_bindir}/lskat
%{_datadir}/applications/org.kde.lskat.desktop
%{_datadir}/lskat
%{_iconsdir}/hicolor/*/apps/lskat.png
%{_datadir}/metainfo/org.kde.lskat.appdata.xml
