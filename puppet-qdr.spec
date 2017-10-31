%{!?upstream_version: %global upstream_version %{commit}}
%if 0%{?dlrn}
%define upstream_name openstack-qdr
%else
%define upstream_name puppet-qdr
%endif
%global commit dcd40cae919d2359fdce002f1edecc462eb25d18
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-qdr
Version:                0.2.0
Release:                1%{?alphatag}%{?dist}
Summary:                Installs, configures, and managed Qpid dispatch router
License:                ASL 2.0

URL:                    https://git.openstack.org/cgit/openstack/%{name}

Source0:                https://github.com/openstack/%{name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 0.2.0-1.dcd40cagit
- Pike update 0.2.0 (dcd40cae919d2359fdce002f1edecc462eb25d18)

