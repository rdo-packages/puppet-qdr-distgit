%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-qdr

Name:                   puppet-qdr
Version:                4.4.0
Release:                1%{?dist}
Summary:                Installs, configures, and managed Qpid dispatch router
License:                ASL 2.0

URL:                    https://git.openstack.org/cgit/openstack/%{name}

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Installs, configures, and managed Qpid dispatch router

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/qdr/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/qdr/



%files
%{_datadir}/openstack-puppet/modules/qdr/


%changelog
* Mon Oct 07 2019 RDO <dev@lists.rdoproject.org> 4.4.0-1
- Update to 4.4.0


