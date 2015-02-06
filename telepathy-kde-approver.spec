%define srcname ktp-approver

Summary:	KDE Channel Approver for Telepathy
Name:		telepathy-kde-approver
Version:	0.5.1
Release:	2
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-approver
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging 
BuildRequires:	pkgconfig(TelepathyQt4)
BuildRequires:	kdelibs4-devel

Obsoletes:	telepathy-approver < 0.2.0-0

%description
KDE Channel Approver for Telepathy.

%files -f kded_ktp_approver.lang
%{_kde_libdir}/kde4/kded_ktp_approver.so
%{_kde_configdir}/ktp_approverrc
%{_kde_services}/kded/ktp_approver.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Approver.service

#------------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang kded_ktp_approver
