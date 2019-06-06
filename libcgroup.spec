#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcgroup
Version  : 0.41
Release  : 21
URL      : https://sourceforge.net/projects/libcg/files/libcgroup/v0.41/libcgroup-0.41.tar.bz2
Source0  : https://sourceforge.net/projects/libcg/files/libcgroup/v0.41/libcgroup-0.41.tar.bz2
Summary  : Library that abstracts the control group file system in Linux
Group    : Development/Tools
License  : LGPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: libcgroup-bin = %{version}-%{release}
Requires: libcgroup-lib = %{version}-%{release}
Requires: libcgroup-license = %{version}-%{release}
Requires: libcgroup-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : flex
Patch1: CVE-2018-14348.patch

%description
Control groups infrastructure. The tools and library help manipulate, control,
administrate and monitor control groups and the associated controllers.

%package bin
Summary: bin components for the libcgroup package.
Group: Binaries
Requires: libcgroup-license = %{version}-%{release}

%description bin
bin components for the libcgroup package.


%package dev
Summary: dev components for the libcgroup package.
Group: Development
Requires: libcgroup-lib = %{version}-%{release}
Requires: libcgroup-bin = %{version}-%{release}
Provides: libcgroup-devel = %{version}-%{release}
Requires: libcgroup = %{version}-%{release}
Requires: libcgroup = %{version}-%{release}

%description dev
dev components for the libcgroup package.


%package lib
Summary: lib components for the libcgroup package.
Group: Libraries
Requires: libcgroup-license = %{version}-%{release}

%description lib
lib components for the libcgroup package.


%package license
Summary: license components for the libcgroup package.
Group: Default

%description license
license components for the libcgroup package.


%package man
Summary: man components for the libcgroup package.
Group: Default

%description man
man components for the libcgroup package.


%prep
%setup -q -n libcgroup-0.41
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559831688
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1559831688
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcgroup
cp COPYING %{buildroot}/usr/share/package-licenses/libcgroup/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cgclassify
/usr/bin/cgclear
/usr/bin/cgconfigparser
/usr/bin/cgcreate
/usr/bin/cgdelete
/usr/bin/cgexec
/usr/bin/cgget
/usr/bin/cgrulesengd
/usr/bin/cgset
/usr/bin/cgsnapshot
/usr/bin/lscgroup
/usr/bin/lssubsys

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libcgroup/config.h
/usr/include/libcgroup/error.h
/usr/include/libcgroup/groups.h
/usr/include/libcgroup/init.h
/usr/include/libcgroup/iterators.h
/usr/include/libcgroup/log.h
/usr/include/libcgroup/tasks.h
/usr/lib64/libcgroup.so
/usr/lib64/pkgconfig/libcgroup.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcgroup.so.1
/usr/lib64/libcgroup.so.1.0.41
/usr/lib64/security/pam_cgroup.so
/usr/lib64/security/pam_cgroup.so.0
/usr/lib64/security/pam_cgroup.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcgroup/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cgclassify.1
/usr/share/man/man1/cgclear.1
/usr/share/man/man1/cgcreate.1
/usr/share/man/man1/cgdelete.1
/usr/share/man/man1/cgexec.1
/usr/share/man/man1/cgget.1
/usr/share/man/man1/cgset.1
/usr/share/man/man1/cgsnapshot.1
/usr/share/man/man1/lscgroup.1
/usr/share/man/man1/lssubsys.1
/usr/share/man/man5/cgconfig.conf.5
/usr/share/man/man5/cgred.conf.5
/usr/share/man/man5/cgrules.conf.5
/usr/share/man/man8/cgconfigparser.8
/usr/share/man/man8/cgrulesengd.8
