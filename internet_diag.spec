Name: internet-diag
Version: 0.2.5
Release: alt3

Summary: Active Directory domain environment diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url:

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: shellcheck

Requires: alterator-interface-diag1

%description
Active Directory domain environment diagnostic tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name
sed -i 's/@VERSION@/%version/g' %name.man

%install
install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D %name.man %buildroot%_mandir/man1/%name.1
install -p -D alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D alterator/%name.desktop %buildroot%_alterator_datadir/backends/%name.desktop

%check
shellcheck -e SC1090,SC1091,SC2004,SC2015,SC2034,SC2086,SC2154,SC2001,SC2120,SC2119 %name

%files
%_bindir/%name
%_mandir/man1/%name.*
%_alterator_datadir/backends/%name.*

%changelog
