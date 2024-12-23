%define oname Bottles

Name:       bottles
Version:    51.17
Release:    1
License:    GPLv3+
Summary:    Easily manage Wine prefix in a new way
URL:        https://github.com/bottlesdevs/Bottles
Source0:    https://github.com/bottlesdevs/Bottles/archive/%{version}/%{oname}-%{version}.tar.gz
# Revert this insanity. Please don't port deviation from windows to linux. Flatpak is an option, not a requirement.
Patch0:     if-you-want-flatpak-everywhere-switch-to-windows-and-dont-broke-linux.patch

BuildRequires: appstream-util
BuildRequires: gettext
BuildRequires: meson
BuildRequires: python
BuildRequires: python-gobject3
BuildRequires: python-gi
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libhandy-1)
BuildArch:  noarch

Requires: python3dist(patool)
Requires: python3dist(pathvalidate)
Requires: python3dist(pefile)
Requires: python3dist(pillow)
Requires: python3dist(pyyaml)
Requires: python3dist(chardet)
Requires: python3dist(urllib3)
Requires: python3dist(icoextract)
Requires: python3dist(idna)
Requires: python3dist(certifi)
Requires: python3dist(requests)
Requires: python3dist(markdown)
Requires: python3dist(maturin)
Requires: python3dist(notify2)
Requires: python3dist(orjson)
Requires: python3dist(fvs)
Requires: python3dist(vkbasalt-cli)
Requires: %{_lib}yaml0_2
Requires: %{_lib}adwaita1_0
Requires: %{_lib}portal1
Requires: %{_lib}curl-gnutls4
Requires: %{_lib}gnutls
Requires: %{_lib}gnutlsxx
#32bit
Requires: libgnutls
Requires: libgnutlsxx
Requires: gnutls
Requires: python-gobject3
Requires: python-gi
Requires: imagemagick
Requires: sassc
Requires: gtk+3.0
Requires: gtk4
Requires: gobject-introspection
Requires: 7zip
Requires: cabextract
Requires: libhandy-common
Requires: vulkan-loader
Requires: vulkan-tools
Requires: xdpyinfo
Requires: webkit
Requires: vte3

#Missing
#vmtouch

#Typelibs
Requires: typelib(Adw)
Requires: typelib(Gdk)
Requires: typelib(GdkX11)
Requires: typelib(Gtk)
Requires: typelib(Notify)
Requires: typelib(Pango)
Requires: typelib(Handy)
Requires: typelib(WebKit2)

# For 32-bit apps/games we need 32-bit compat gamemode but 32bit it is not available yet in Cooker.
# Let's add 32 bit later
Recommends: gamemode
Suggests: wine
#TBC

%description
Easily manage Wine prefix in a new way! (Run Windows software and games on
Linux).

Features:

  * Create bottles based on environments (a set of rule and dependencies for
    better software compatibility)
  * Access to a customizable environment for all your experiments
  * Run every executable (.exe/.msi) in your bottles, using the context menu
    in your file manager
  * Integrated management and storage for executable file arguments
  * Support for custom environment variables
  * Simplified DLL overrides
  * On-the-fly runner change for any Bottle
  * Various optimizations for better gaming performance (esync, fsync, dxvk,
    cache, shader compiler, offload .. and much more.)
  * Tweak different wine prefix settings, without leaving Bottles
  * Automated dxvk installation
  * Automatic installation and management of Wine and Proton runners
  * System for checking runner updates for the bottle and automatic repair in
    case of breakage
  * Integrated Dependencies installer with compatibility check based on a
    community-driver repository
  * Detection of installed programs
  * Integrated Task manager for wine processes
  * Easy access to ProtonDB and WineHQ for support
  * Configurations update system across Bottles versions
  * Backup bottles as configuration file or full archive
  * Import backup archive
  * Importer from Bottles v1 (and other wineprefix manager)
  * Bottles versioning (experimental)
  * .. and much more that you can find by installing Bottles!


%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
    
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
%{_bindir}/bottles-cli
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml
