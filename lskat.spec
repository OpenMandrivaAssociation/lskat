%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		lskat
Version:	18.12.0
Release:	1
Epoch:		1
Summary:	Lieutenant skat
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/lskat/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	ninja

%description
Lieutenant Skat (from German "Offiziersskat") is a fun and engaging card game
for two players, where the second player is either live opponent, or a built
in artificial intelligence.

%files -f %{name}.lang
%{_sysconfdir}/xdg/lskat.categories
%{_bindir}/lskat
%{_datadir}/applications/org.kde.lskat.desktop
%{_datadir}/lskat
%{_iconsdir}/hicolor/*/apps/lskat.png
%{_datadir}/kxmlgui5/lskat
%{_datadir}/metainfo/org.kde.lskat.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%ninja

%install
%ninja_install -C build
%find_lang %{name} --with-html --all-name
