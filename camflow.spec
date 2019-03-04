Summary: Install all CamFlow dependencies.
Name: camflow
Version: 0.8.4
Release: 1
Group: audit/camflow
License: GPLv2
Source: %{expand:%%(pwd)}
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-%{release}
Requires: camconfd = 0.4.4
Requires: camflowd = 0.2.3
Requires: camflow-cli = 0.1.13
Requires: kernel = 4.20.13camflow0.5.3
Requires: kernel-headers = 4.20.13camflow0.5.3
Requires: kernel-devel = 4.20.13camflow0.5.3
Requires: libprovenance = 0.4.6

%description
%{summary}

%prep

%clean
rm -r -f "$RPM_BUILD_ROOT"

%files
