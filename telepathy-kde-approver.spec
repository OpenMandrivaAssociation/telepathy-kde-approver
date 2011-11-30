%define rel 1

Summary:       KDE Channel Approver for Telepathy
Name:          telepathy-kde-approver
Version:       0.2.0
Release:       %mkrel %{rel}
Url:           https://projects.kde.org/projects/playground/network/telepathy/telepathy-approver
Source0:       ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:       GPLv2+
Group:         Graphical desktop/KDE
BuildRequires: kdelibs4-devel
BuildRequires: telepathy-qt4-devel
Provides: telepathy-approver = %version-%release
Obsoletes: telepathy-approver < 0.2.0-0

%description
KDE Channel Approver for Telepathy.

%files -f %{name}.lang
%{_kde_libdir}/kde4/kded_telepathy_kde_approver.so
%{_kde_configdir}/telepathy_kde_approverrc
%{_kde_services}/kded/telepathy_kde_approver.desktop

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang %name


