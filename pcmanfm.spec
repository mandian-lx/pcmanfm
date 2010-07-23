%define prerel rc1
%define git git20110722

Summary:	PCMan File Manager
Name:		pcmanfm
Version:	0.9.7
Release:	%mkrel -c %prerel 2
URL:		http://pcmanfm.sourceforge.net/
Source0:	%{name}-%{version}-%git.tar.gz
License:	GPLv2+
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel pkgconfig
BuildRequires:	intltool desktop-file-utils
BuildRequires:	libfm-devel >= 0.1.12
Requires:	shared-mime-info
Requires:	gnome-icon-theme
Suggests:	gvfs

%description
PCMan File Manager is an extremely fast and lightweight file manager which
features tabbed browsing and user-friendly interface.

%prep
%setup -q

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

#install default .conf file
mkdir -p %{buildroot}%{_sysconfdir}/xdg/pcmanfm

cat > %{buildroot}%{_sysconfdir}/xdg/pcmanfm/pcmanfm.conf << EOF
[desktop]
wallpaper_mode=1
wallpaper=/usr/share/mdk/backgrounds/default.jpg
EOF

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}/%{name}.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
