%define git 0
%define prerel 19e957a
%define ver 1.0.1
%define gitday 20112007

Summary:	PCMan File Manager
Name:		pcmanfm
Release:	1
URL:		http://pcmanfm.sourceforge.net/

%if %git
Version:	%{ver}.git%{gitday}
Source0:	%{name}-%{prerel}.tar.gz
%else
Version:	%{ver}
Source0:	http://dfn.dl.sourceforge.net/sourceforge/pcmanfm/%{name}-%{version}.tar.gz
%endif
Patch0:		pcmanfm-0.9.8-mdv-default-config.patch        

#Patches from ALT Linux
#Patch2:		pcmanfm2-alt-fix-pseudotransparency.patch
#Patch3:		pcmanfm2-opencwd.patch
#Patch4:		pcmanfm2-temp-close-unmount-fix.patch
#Patch5:		pcmanfm2-delete-win-on-close.patch

#Patch6:		pcmanfm-0.9.10-nav_get_history.patch
#Patch7:		pcmanfm-0.9.10-rightclick.patch

License:	GPLv2+
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	intltool desktop-file-utils
%if %git
BuildRequires:	libfm-devel = 0.1.15.git%{gitday}
%else
BuildRequires:	libfm-devel = %{version}
%endif
Requires:	shared-mime-info gksu
Requires:	gnome-icon-theme
Suggests:	gvfs
Conflicts:	lxde-common < 0.5.0

%description
PCMan File Manager is an extremely fast and lightweight file manager which
features tabbed browsing and user-friendly interface.

%prep
%if %git
%setup -q -n %{name}-%{prerel}
%else
%setup -q
%endif

%apply_patches

%build
#./autogen.sh
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
%{_datadir}/applications/%{name}-desktop-pref.desktop
%{_datadir}/man/man1/pcmanfm.1.xz


%changelog
* Tue May 31 2012 akdengi <akdengi> 0.9.10-3
- fix rightclick folder crash

