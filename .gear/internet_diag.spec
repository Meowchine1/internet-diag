Name: internet_diag
Version: 0.0.1
Release: alt3

Summary: Active Directory domain environment diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url: https://github.com/Meowchine1/internet-diag

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator


%description
Active Directory domain environment diagnostic tool.

%prep
%setup

%install
install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D alterator/%name.desktop %buildroot%_alterator_datadir/backends/%name.desktop

%files
%_bindir/%name
%_alterator_datadir/backends/%name.*

%changelog
* Tue Oct 31 2023 Ekaterina Voronina <vor@altlinux.org> 0.0.1-alt3
- Initial commit

