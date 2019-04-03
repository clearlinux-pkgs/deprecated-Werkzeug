#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-Werkzeug
Version  : 0.14.1
Release  : 63
URL      : http://pypi.debian.net/Werkzeug/Werkzeug-0.14.1.tar.gz
Source0  : http://pypi.debian.net/Werkzeug/Werkzeug-0.14.1.tar.gz
Summary  : The comprehensive WSGI web application library.
Group    : Development/Tools
License  : BSD-3-Clause OFL-1.1
Requires: deprecated-Werkzeug-license = %{version}-%{release}
Requires: deprecated-Werkzeug-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
=================
Werkzeug Examples
=================
This directory contains various example applications and example code of
Werkzeug powered applications.

%package legacypython
Summary: legacypython components for the deprecated-Werkzeug package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-Werkzeug package.


%package license
Summary: license components for the deprecated-Werkzeug package.
Group: Default

%description license
license components for the deprecated-Werkzeug package.


%package python
Summary: python components for the deprecated-Werkzeug package.
Group: Default
Provides: deprecated-werkzeug-python

%description python
python components for the deprecated-Werkzeug package.


%prep
%setup -q -n Werkzeug-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554330404
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-Werkzeug
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-Werkzeug/LICENSE
cp werkzeug/debug/shared/FONT_LICENSE %{buildroot}/usr/share/package-licenses/deprecated-Werkzeug/werkzeug_debug_shared_FONT_LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-Werkzeug/LICENSE
/usr/share/package-licenses/deprecated-Werkzeug/werkzeug_debug_shared_FONT_LICENSE

%files python
%defattr(-,root,root,-)
