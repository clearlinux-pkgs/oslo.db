#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.db
Version  : 4.43.0
Release  : 62
URL      : https://tarballs.openstack.org/oslo.db/oslo.db-4.43.0.tar.gz
Source0  : https://tarballs.openstack.org/oslo.db/oslo.db-4.43.0.tar.gz
Source99 : https://tarballs.openstack.org/oslo.db/oslo.db-4.43.0.tar.gz.asc
Summary  : Oslo Database library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.db-license = %{version}-%{release}
Requires: oslo.db-python = %{version}-%{release}
Requires: oslo.db-python3 = %{version}-%{release}
Requires: PyMySQL
Requires: SQLAlchemy
Requires: Sphinx
Requires: alembic
Requires: debtcollector
Requires: doc8
Requires: fixtures
Requires: openstackdocstheme
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.utils
Requires: oslotest
Requires: pbr
Requires: psycopg2
Requires: reno
Requires: six
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: testresources
Requires: testscenarios
BuildRequires : buildreq-distutils3
BuildRequires : pbr
Patch1: 0001-Modify-min_pool_size-default-value.patch

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.db.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the oslo.db package.
Group: Default

%description license
license components for the oslo.db package.


%package python
Summary: python components for the oslo.db package.
Group: Default
Requires: oslo.db-python3 = %{version}-%{release}

%description python
python components for the oslo.db package.


%package python3
Summary: python3 components for the oslo.db package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.db package.


%prep
%setup -q -n oslo.db-4.43.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546552230
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.db
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.db/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.db/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
