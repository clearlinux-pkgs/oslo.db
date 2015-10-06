#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.db
Version  : 2.6.0
Release  : 26
URL      : http://tarballs.openstack.org/oslo.db/oslo.db-2.6.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.db/oslo.db-2.6.0.tar.gz
Summary  : Oslo Database library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.db-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Mako
BuildRequires : MySQL-python
BuildRequires : Pygments
BuildRequires : SQLAlchemy
BuildRequires : Sphinx-python
BuildRequires : Tempita
BuildRequires : alembic
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
BuildRequires : posix_ipc
BuildRequires : psycopg2
BuildRequires : py-python
BuildRequires : pyflakes-python
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
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : wrapt-python
Patch1: 0001-Modify-min_pool_size-default-value.patch

%description
=========
oslo.db
=========
.. image:: https://img.shields.io/pypi/v/oslo.db.svg
:target: https://pypi.python.org/pypi/oslo.db/
:alt: Latest Version

%package python
Summary: python components for the oslo.db package.
Group: Default
Requires: iso8601-python
Requires: oslo.utils-python
Requires: oslo.i18n-python
Requires: Babel-python
Requires: six-python

%description python
python components for the oslo.db package.


%prep
%setup -q -n oslo.db-2.6.0
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
