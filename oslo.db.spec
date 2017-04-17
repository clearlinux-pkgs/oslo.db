#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : oslo.db
Version  : 4.21.0
Release  : 54
URL      : https://tarballs.openstack.org/oslo.db/oslo.db-4.21.0.tar.gz
Source0  : https://tarballs.openstack.org/oslo.db/oslo.db-4.21.0.tar.gz
Source99 : https://tarballs.openstack.org/oslo.db/oslo.db-4.21.0.tar.gz.asc
Summary  : Oslo Database library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.db-python
Requires: MySQL-python
Requires: PyMySQL
Requires: SQLAlchemy
Requires: Sphinx
Requires: alembic
Requires: coverage
Requires: debtcollector
Requires: doc8
Requires: eventlet
Requires: fixtures
Requires: hacking
Requires: os-testr
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.utils
Requires: oslosphinx
Requires: oslotest
Requires: pbr
Requires: psycopg2
Requires: python-mock
Requires: python-subunit
Requires: reno
Requires: six
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: testrepository
Requires: testresources
Requires: testscenarios
Requires: testtools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Modify-min_pool_size-default-value.patch

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.db.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the oslo.db package.
Group: Default

%description python
python components for the oslo.db package.


%prep
%setup -q -n oslo.db-4.21.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492457787
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1492457787
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
