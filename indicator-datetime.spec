Summary:	A very simple clock indicator
Name:		indicator-datetime
Version:	0.3.1
Release:	1
License:	GPLv3
Url:		http://launchpad.net/indicator-datetime
Group:		Graphical desktop/GNOME
Source0:	http://launchpad.net/indicator-datetime/0.3/%{version}/+download/%{name}-%{version}.tar.gz
Source1:	time-admin.svg 

BuildRequires:	intltool
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(geoclue)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-window-settings-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedataserverui-3.0)
BuildRequires:	pkgconfig(libgnome-control-center)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libido3-0.1)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(unique-3.0)

%description
This indicator displays a very simple clock on the panel and offers appointment
integration through evolution.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

# Installing missing time-admin icon required for desktop file
# afaict the name for the icon changed but still missing md
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/preferences-system-time.svg

find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_libexecdir}/indicator-datetime-service
%{_libdir}/control-center-1/
%{_libdir}/indicators3/
%{_datadir}/applications/indicator-datetime-preferences.desktop
%{_datadir}/dbus-1/services/indicator-datetime.service
%{_datadir}/glib-2.0/schemas/com.canonical.indicator.datetime.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/time-admin.svg
%{_datadir}/indicator-datetime/

