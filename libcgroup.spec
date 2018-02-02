#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcgroup
Version  : 0.41
Release  : 17
URL      : http://downloads.sourceforge.net/libcg/libcgroup-0.41.tar.bz2
Source0  : http://downloads.sourceforge.net/libcg/libcgroup-0.41.tar.bz2
Summary  : Tools and libraries to control and monitor control groups
Group    : Development/Tools
License  : LGPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: libcgroup-bin
Requires: libcgroup-lib
Requires: libcgroup-doc
BuildRequires : Linux-PAM-dev
BuildRequires : bison
BuildRequires : flex

%description
Control groups infrastructure. The tools and library help manipulate, control,
administrate and monitor control groups and the associated controllers.

%package bin
Summary: bin components for the libcgroup package.
Group: Binaries

%description bin
bin components for the libcgroup package.


%package dev
Summary: dev components for the libcgroup package.
Group: Development
Requires: libcgroup-lib
Requires: libcgroup-bin

%description dev
dev components for the libcgroup package.


%package doc
Summary: doc components for the libcgroup package.
Group: Documentation

%description doc
doc components for the libcgroup package.


%package lib
Summary: lib components for the libcgroup package.
Group: Libraries

%description lib
lib components for the libcgroup package.


%prep
%setup -q -n libcgroup-0.41

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/security/pam_cgroup.so
/usr/lib64/security/pam_cgroup.so.0
/usr/lib64/security/pam_cgroup.so.0.0.0
