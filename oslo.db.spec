#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : oslo.db
Version  : 4.14.0
Release  : 49
URL      : http://tarballs.openstack.org/oslo.db/oslo.db-4.14.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.db/oslo.db-4.14.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.db/oslo.db-4.14.0.tar.gz.asc
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
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Mako
BuildRequires : MySQL-python
BuildRequires : Pygments
BuildRequires : SQLAlchemy
BuildRequires : Sphinx-python
BuildRequires : Tempita
BuildRequires : alembic
BuildRequires : configparser-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : decorator
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : nose
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : psycopg2
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : sqlalchemy-migrate
BuildRequires : sqlparse
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python
Patch1: 0001-Modify-min_pool_size-default-value.patch

%description
===============================================
oslo.db -- OpenStack Database Pattern Library
===============================================

%package python
Summary: python components for the oslo.db package.
Group: Default

%description python
python components for the oslo.db package.


%prep
%setup -q -n oslo.db-4.14.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489031953
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1489031953
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
