%define git 1
%define prerel 43fdda4
%define ver 0.9.9
%define gitday 20111902

Summary:	PCMan File Manager
Name:		pcmanfm
Release:	%mkrel 3
URL:		http://pcmanfm.sourceforge.net/

%if %git
Version:	%{ver}.git%{gitday}
Source0:	%{name}-%{prerel}.tar.gz
%else
Version:	%{ver}
Source0:	%{name}-%{version}.tar.gz
%endif
Patch0:		pcmanfm-0.9.8-mdv-default-config.patch
#Patch1:		pcmanfm_multi.patch
License:	GPLv2+
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel pkgconfig
BuildRequires:	intltool desktop-file-utils
%if %git
BuildRequires:	libfm-devel = 0.1.15.git%{gitday}
%else
BuildRequires:	libfm-devel >= 0.1.15
%endif
Requires:	shared-mime-info gksu
Requires:	gnome-icon-theme xinitrc_dbus
Suggests:	gvfs
Conflicts:	lxde-common < 0.5.0

%description
PCMan File Manager is an extremely fast and lightweight file manager which
features tabbed browsing and user-friendly interface.

%prep
%if %git
%setup -q -n %{name}-%{prerel}
%else
%setup -q -n %{name}
%endif

#rm src/single-inst.c
#rm src/single-inst.h
%patch0 -p1
#patch1 -p1

%build
./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

# clean .desktop file
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="System;FileTools" \
  --remove-mime-type="x-directory/normal" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}/default/pcmanfm.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
