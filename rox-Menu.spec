%define _name ROX-Menu
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Menu is a simple application menu for the ROX Desktop environment
Summary(pl):	ROX-Menu jest prostym rozwijanym menu dla ¶rodowiska ROX
Name:		rox-Menu
Version:	0.3.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.unixdaemons.com/~mindcrisis/projects/rox-menu-source.tar.gz
Patch0:		%{name}-AppRun-fix.patch
URL:		http://www.unixdaemons.com/~mindcrisis/index.cgi?handler=proj_roxmenu
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define   _appsdir  %{_libdir}/ROX-apps

%description
This simple ROX applet lets you launch your most used applications
without opening your wrapper directory. It works like a "K" button on
KDE, and a "foot button" on GNOME desktops.

%description -l pl
Ten prosty aplet ROXa pozwala na uruchamianie najczê¶ciej u¿ywanych
programów bez otwierania katalogu z wrapperami. Wygl±da on tak jak
przycisk "K" w KDE, lub "przycisk-stopa" w GNOME.

%prep
%setup -q -n %{_name}
%patch0 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

install AppI* AppRun $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/Readme $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/ROX-Menu $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

ln -sf AppRun $RPM_BUILD_ROOT%{_appsdir}/%{_name}/AppletRun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/AppletRun
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
