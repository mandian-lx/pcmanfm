Summary:	PCMan File Manager
Name:		pcmanfm
Version:	0.9.8
Release:	%mkrel 1
URL:		http://pcmanfm.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		pcmanfm-0.9.8-mdv-default-config.patch
License:	GPLv2+
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel pkgconfig
BuildRequires:	intltool desktop-file-utils
BuildRequires:	libfm-devel >= 0.1.14
Requires:	shared-mime-info
Requires:	gnome-icon-theme
Suggests:	gvfs
Conflicts:	lxde-common < 0.5.5

%description
PCMan File Manager is an extremely fast and lightweight file manager which
features tabbed browsing and user-friendly interface.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

# clean .desktop file
desktop-file-install --vendor="" \
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
