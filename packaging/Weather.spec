Name:       Weather	
Summary:    A HTML Weather application
Version:    0.0.1
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  common-apps
BuildRequires:  zip
BuildRequires:  desktop-file-utils

Requires: pkgmgr
Requires: crosswalk
Requires: tizen-extensions-crosswalk
Requires: pkgmgr-server
Requires: model-config-ivi
Requires: tizen-middleware-units
Requires: tizen-platform-config

%description
A HTML Weather application to display public weather info.

%prep
%setup -q -n %{name}-%{version}

%build

make wgtPkg

#make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make install_obs "OBS=1" DESTDIR="%{?buildroot}"

%post
su app -c "pkgcmd -i -t wgt -p /opt/usr/apps/.preinstallWidgets/JLRPOCX035.Weather.wgt -q"

%postun
su app -c "pkgcmd -u -n JLRPOCX035 -q"

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/JLRPOCX035.Weather.wgt

