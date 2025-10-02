Name:           proxy-api
Version:        1.0
Release:        1%{?dist}
Summary:        Proxy API Service with Redis caching

License:        MIT
URL:            https://github.com/your-company/proxy-api
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-flask python3-redis python3-requests python3-PyYAML redis

%description
Proxy API service with Redis caching capabilities. Provides caching layer for backend services.

%prep
%setup -q

%build
# No build step needed for Python script

%install
# Create directories
install -d %{buildroot}%{_sysconfdir}/proxy-api
install -d %{buildroot}%{_libdir}/proxy-api
install -d %{buildroot}%{_unitdir}

# Install configuration files
install -m 644 etc/proxy-api/config.yaml %{buildroot}%{_sysconfdir}/proxy-api/

# Install application files
install -m 755 usr/lib/proxy-api/proxy-api.py %{buildroot}%{_libdir}/proxy-api/

# Install systemd service file
install -m 644 lib/systemd/system/proxy-api.service %{buildroot}%{_unitdir}/

%pre
# Pre-install script
getent group proxy-api >/dev/null || groupadd -r proxy-api
getent passwd proxy-api >/dev/null || useradd -r -g proxy-api -d /usr/lib/proxy-api -s /sbin/nologin -c "Proxy API Service" proxy-api

%post
# Post-install script
systemctl daemon-reload >/dev/null 2>&1 || :

%preun
# Pre-uninstall script
if [ $1 -eq 0 ]; then
    systemctl --no-reload disable proxy-api.service >/dev/null 2>&1 || :
    systemctl stop proxy-api.service >/dev/null 2>&1 || :
fi

%postun
# Post-uninstall script
systemctl daemon-reload >/dev/null 2>&1 || :

%files
%dir %{_sysconfdir}/proxy-api
%config(noreplace) %{_sysconfdir}/proxy-api/config.yaml
%dir %{_libdir}/proxy-api
%{_libdir}/proxy-api/proxy-api.py
%{_unitdir}/proxy-api.service

%changelog
* Tue Nov 01 2024 Your Name <your.email@company.com> - 1.0-1
- Initial package build