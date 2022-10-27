%global _date 20210910

Name:		libedit
Version:	3.1
Release:	29
Summary:	The NetBSD Editline library
License:	BSD
URL:		http://www.thrysoee.dk/editline/

Source0:	https://www.thrysoee.dk/editline/%{name}-%{_date}-%{version}.tar.gz
BuildRequires:	gcc, ncurses-devel

%description
Libedit is the automatic tool and libtoolized port of the NetBSD Editline library.
It provides generic line editing, history, and markup functions similar to
those in GNU Readline.

%package devel
Summary:	libedit's development files
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel%{?_isa}

%description devel
libedit's development files

%package help
Summary:	Help information for user

%description help
Help information for user

%prep
%autosetup -n %{name}-%{_date}-%{version}

# below for fixing issue of rpmlint
iconv -f ISO8859-1 -t UTF-8 -o ChangeLog.utf-8 ChangeLog
touch -r ChangeLog ChangeLog.utf-8
mv -f ChangeLog.utf-8 ChangeLog

# delete nroff macro
sed -i 's,\\\*\[Gt\],>,' doc/editline.3.roff

%build
%configure --disable-static --disable-silent-rules
sed -i "s/lncurses/ltinfo/" src/Makefile
sed -i "s/ -lncurses//" libedit.pc
%make_build

%install
%make_install
%ldconfig_scriptlets

%files
%doc COPYING ChangeLog THANKS
%{_libdir}/libedit.so.*

%files devel
%{_includedir}/histedit.h
%{_includedir}/editline/readline.h
%{_libdir}/libedit.so
%{_libdir}/pkgconfig/libedit.pc
%exclude %{_libdir}/*.la

%files help
%doc examples/fileman.c examples/tc1.c examples/wtc1.c
%{_mandir}/man3/*
%{_mandir}/man5/editrc.5*
%{_mandir}/man7/*
%exclude %{_mandir}/man3/history.3*

%changelog
* Tue Oct 25 2022 yanglongkang<yanglongkang@h-partners.com> - 3.1-29
- Type: bugfix
- ID: NA
- SUG: NA
- DESC: rebuild for next release

* Tue Nov 30 2021 panxiaohe<panxiaohe@huawei.com> - 3.1-28
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update version to 20210910-3.1 

* Tue Jul 28 2020 yang_zhuang_zhuang<yangzhuangzhuang1@huawei.com> - 3.1-27
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update version to 20191231-3.1

* Tue Dec 31 2019 hanxinke<hanxinke@huawei.com> - 3.1-26
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update source package

* Wed Sep 4 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.1-25
- Package init
