Summary: Install all CamFlow dependencies.
Name: camflow
Version: 0.5.1
Release: 1
Group: audit/camflow
License: GPLv2
Source: %{expand:%%(pwd)}
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-%{release}
Requires: camconfd = 0.4.0
Requires: camflowd = 0.1.8
Requires: camflow-cli = 0.1.7
Requires: kernel = 4.14.9camflow0.3.9
Requires: kernel-headers = 4.14.9camflow0.3.9
Requires: kernel-devel = 4.14.9camflow0.3.9
Requires: libprovenance = 0.3.9

%description
%{summary}

%prep

%clean
rm -r -f "$RPM_BUILD_ROOT"

%files
