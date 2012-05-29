%define git 0
%define prerel 19e957a
%define ver 0.9.10
%define gitday 20112007

Summary:	PCMan File Manager
Name:		pcmanfm
Release:	%mkrel 1
URL:		http://pcmanfm.sourceforge.net/

%if %git
Version:	%{ver}.git%{gitday}
Source0:	%{name}-%{prerel}.tar.gz
%else
Version:	%{ver}
Source0:	%{name}-%{version}.tar.gz
%endif
Patch0:		pcmanfm-0.9.8-mdv-default-config.patch
Patch1:		pcmanfm-0.9.10-win-resize.patch         
#Patches from ALT Linux
Patch2:		pcmanfm2-alt-fix-pseudotransparency.patch
Patch3:		pcmanfm2-opencwd.patch
Patch4:		pcmanfm2-alt-fix-rmb-selection.patch
Patch5:		pcmanfm2-temp-close-unmount-fix.patch
Patch6:		pcmanfm2-delete-win-on-close.patch

License:	GPLv2+
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel pkgconfig
BuildRequires:	intltool desktop-file-utils
%if %git
BuildRequires:	libfm-devel = 0.1.15.git%{gitday}
%else
BuildRequires:	libfm-devel >= 0.1.17
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
%setup -q
%endif

#rm src/single-inst.c
#rm src/single-inst.h
%patch0 -p1

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


%changelog
* Tue Jul 19 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git20112007-1mdv2011.0
+ Revision: 690609
- fix dnd error and update translates

* Thu Jun 16 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git20112006-1
+ Revision: 685701
- use latest libfm API

* Sun Jun 12 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git20111906-1
+ Revision: 684364
- update for new git snapshot

* Sat May 28 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git20111905-1
+ Revision: 681318
- rebuild for new svn snapshot libfm 20111905

* Fri May 06 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git20111904-4
+ Revision: 669782
- new build from git and add selection patch

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.9.git20111902-3
+ Revision: 667000
- mass rebuild

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.9.9.git20111902-2
+ Revision: 640309
- rebuild to obsolete old packages

* Sat Feb 19 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git20111902-1
+ Revision: 638630
+ rebuild (emptylog)

* Thu Feb 17 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.9.git6240436-2
+ Revision: 638240
- switch to 0.9.9 git branch

* Sat Dec 04 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.8-2mdv2011.0
+ Revision: 609297
- add upstream patch to  fix some IPC issues; this should fix pcmanfm
  not opening except one instance

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 0.9.8-1mdv2011.0
+ Revision: 602286
- new versio 0.9.8

* Mon Jul 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.7-0.rc1.3mdv2011.0
+ Revision: 560860
- conflicts with lxde-common < 0.5.5
- svn cp pcmanfm/branches/current to pcmanfm/current, step two of bringing pcmanfm2
  out of the svn branch

* Thu Jul 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.7-0.rc1.2mdv2011.0
+ Revision: 557099
- update to 0.9.7 latest git snapshot, this brings more translations and a couple
  of crash fixes
- drop the rename patch, pcmanfm2 has been renamed to pcmanfm upstream

* Tue Apr 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.5-0.beta3.1mdv2010.1
+ Revision: 539857
- new release, beta3, 0.9.5

* Mon Apr 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.4-0.beta2.2mdv2010.1
+ Revision: 539355
- new git snapshot
- rediff renaming patch
- improve the requires and buildrequires
- clean spec

* Mon Apr 19 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.4-0.beta2.1mdv2010.1
+ Revision: 536563
- new release beta2 0.9.4
- rediff rename patch

* Tue Apr 13 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.3-0.beta.2mdv2010.1
+ Revision: 534499
- new git snapshot
- rediff patch0

* Thu Mar 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.3-0.beta.1mdv2010.1
+ Revision: 525017
- new upstream release 0.9.3 beta

* Wed Mar 17 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9.2-0.alpha.1mdv2010.1
+ Revision: 523665
- add pcmanfm.conf directly from inside the spec
- add pcmanfm.conf to configure default background
- only suggest gvfs
- update to latest git to cope with latest libfm
- add patch from OpenSuse to rename files to pcmanfm2, this will happen upstream
  with final release, but it's better to rename it with the patch to not break
  autostart stuff until then
- new version, 0.9.2 alpha
- remove hal-devel and dbus-glib-devel BR, not needed any more
- BR libfm-devel
- require gvfs
- fix typo in descripion
- fix .desktop file
- remove %%mdkversion < 200900 stuff
- drop old patches, and custom .po file


* Thu Jan 04 2007 Jérôme Soyer <saispo@mandriva.org> 0.3.2.2-1mdv2007.0
+ Revision: 104027
- Add BuildRequires
- New release 0.3.2.2
- Import pcmanfm

* Thu Sep 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.0.2-2mdv2007.0
- add buildrequires libstartup-notification-1_0-devel

* Wed Sep 13 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.0.2-1mdk
- New release 0.3.0.2
- xdg menu

* Fri May 05 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.3-1mdk
- New release 0.2.3

* Fri Apr 21 2006 Austin Acton <austin@mandriva.org> 0.2.2-1mdk
- upload havily modified spec from Shiva Huang <shivahuang@gmail.com>

